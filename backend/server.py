from fastapi import FastAPI, APIRouter, HTTPException, UploadFile, File
from fastapi.responses import FileResponse
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Dict, Any
import uuid
from datetime import datetime, timezone
from emergentintegrations.llm.chat import LlmChat, UserMessage
import json
import shutil

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

app = FastAPI()
api_router = APIRouter(prefix="/api")

EMERGENT_LLM_KEY = os.environ.get('EMERGENT_LLM_KEY')

# Ensure uploads directory exists
UPLOADS_DIR = Path("/app/backend/uploads")
UPLOADS_DIR.mkdir(exist_ok=True)

# ============ MODELS ============

class Framework(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    version: str
    enabled: bool = False
    total_controls: int = 0
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class FrameworkControl(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    framework_id: str
    control_id: str
    title: str
    description: str
    category: str
    testing_procedure: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class UnifiedControl(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    ccf_id: str
    name: str
    description: str
    control_type: str
    frequency: str
    owner: str
    mapped_framework_controls: List[str] = []
    mapped_policies: List[str] = []
    automation_possible: bool = False
    automation_config: Optional[Dict] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class InternalPolicy(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    policy_id: str
    name: str
    description: str
    category: str
    owner: str
    status: str = "Active"
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ControlTest(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    unified_control_id: str
    test_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    tester: str
    status: str
    result: str
    evidence_ids: List[str] = []
    notes: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Evidence(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    control_test_id: str
    unified_control_id: str
    evidence_type: str
    description: str
    automated: bool
    file_path: Optional[str] = None
    file_name: Optional[str] = None
    collected_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Issue(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    control_test_id: Optional[str] = None
    unified_control_id: str
    severity: str
    status: str
    assigned_to: str
    due_date: Optional[str] = None
    has_exception: bool = False
    exception_details: Optional[Dict] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Risk(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    category: str
    inherent_risk_score: float
    residual_risk_score: float
    status: str = "Active"
    owner: str
    kri_ids: List[str] = []
    linked_control_ids: List[str] = []
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class KRI(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    risk_id: str
    current_value: float
    threshold: float
    unit: str
    status: str
    trend: str
    kci_ids: List[str] = []
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class KCI(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    kri_id: str
    unified_control_id: str
    current_value: float
    target: float
    unit: str
    status: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class AIAnalysisRequest(BaseModel):
    analysis_type: str
    context: Dict[str, Any]

class AIAnalysisResponse(BaseModel):
    analysis: str
    recommendations: List[str]

# ============ AI SERVICE ============

async def get_ai_analysis(prompt: str) -> str:
    try:
        chat = LlmChat(
            api_key=EMERGENT_LLM_KEY,
            session_id=str(uuid.uuid4()),
            system_message="You are a GRC (Governance, Risk, and Compliance) expert AI assistant."
        ).with_model("openai", "gpt-4o")
        
        user_message = UserMessage(text=prompt)
        response = await chat.send_message(user_message)
        return response
    except Exception as e:
        logging.error(f"AI analysis error: {str(e)}")
        return "AI analysis temporarily unavailable"

# ============ FRAMEWORK ENDPOINTS ============

@api_router.get("/frameworks", response_model=List[Framework])
async def get_frameworks():
    frameworks = await db.frameworks.find({}, {"_id": 0}).to_list(1000)
    for fw in frameworks:
        if isinstance(fw.get('created_at'), str):
            fw['created_at'] = datetime.fromisoformat(fw['created_at'])
    return frameworks

@api_router.post("/frameworks", response_model=Framework)
async def create_framework(framework: Framework):
    fw_dict = framework.model_dump()
    fw_dict['created_at'] = fw_dict['created_at'].isoformat()
    await db.frameworks.insert_one(fw_dict)
    return framework

@api_router.patch("/frameworks/{framework_id}/toggle")
async def toggle_framework(framework_id: str, enabled: bool):
    await db.frameworks.update_one(
        {"id": framework_id},
        {"$set": {"enabled": enabled}}
    )
    return {"message": "Framework updated"}

@api_router.get("/framework-controls/{framework_id}", response_model=List[FrameworkControl])
async def get_framework_controls(framework_id: str):
    controls = await db.framework_controls.find({"framework_id": framework_id}, {"_id": 0}).to_list(1000)
    for ctrl in controls:
        if isinstance(ctrl.get('created_at'), str):
            ctrl['created_at'] = datetime.fromisoformat(ctrl['created_at'])
    return controls

# ============ UNIFIED CONTROL ENDPOINTS ============

@api_router.get("/unified-controls", response_model=List[UnifiedControl])
async def get_unified_controls():
    controls = await db.unified_controls.find({}, {"_id": 0}).to_list(1000)
    for ctrl in controls:
        if isinstance(ctrl.get('created_at'), str):
            ctrl['created_at'] = datetime.fromisoformat(ctrl['created_at'])
    return controls

@api_router.post("/unified-controls", response_model=UnifiedControl)
async def create_unified_control(control: UnifiedControl):
    ctrl_dict = control.model_dump()
    ctrl_dict['created_at'] = ctrl_dict['created_at'].isoformat()
    await db.unified_controls.insert_one(ctrl_dict)
    return control

@api_router.patch("/unified-controls/{control_id}/map-framework")
async def map_framework_to_unified(control_id: str, framework_control_ids: List[str]):
    await db.unified_controls.update_one(
        {"id": control_id},
        {"$set": {"mapped_framework_controls": framework_control_ids}}
    )
    return {"message": "Mapping updated"}

@api_router.patch("/unified-controls/{control_id}/map-policy")
async def map_policy_to_unified(control_id: str, policy_ids: List[str]):
    await db.unified_controls.update_one(
        {"id": control_id},
        {"$set": {"mapped_policies": policy_ids}}
    )
    return {"message": "Policy mapping updated"}

# ============ INTERNAL POLICY ENDPOINTS ============

@api_router.get("/policies", response_model=List[InternalPolicy])
async def get_policies():
    policies = await db.policies.find({}, {"_id": 0}).to_list(1000)
    for pol in policies:
        if isinstance(pol.get('created_at'), str):
            pol['created_at'] = datetime.fromisoformat(pol['created_at'])
    return policies

@api_router.post("/policies", response_model=InternalPolicy)
async def create_policy(policy: InternalPolicy):
    pol_dict = policy.model_dump()
    pol_dict['created_at'] = pol_dict['created_at'].isoformat()
    await db.policies.insert_one(pol_dict)
    return policy

# ============ CONTROL TESTING ENDPOINTS ============

@api_router.get("/control-tests", response_model=List[ControlTest])
async def get_control_tests():
    tests = await db.control_tests.find({}, {"_id": 0}).to_list(1000)
    for test in tests:
        if isinstance(test.get('test_date'), str):
            test['test_date'] = datetime.fromisoformat(test['test_date'])
        if isinstance(test.get('created_at'), str):
            test['created_at'] = datetime.fromisoformat(test['created_at'])
    return tests

@api_router.post("/control-tests", response_model=ControlTest)
async def create_control_test(test: ControlTest):
    test_dict = test.model_dump()
    test_dict['test_date'] = test_dict['test_date'].isoformat()
    test_dict['created_at'] = test_dict['created_at'].isoformat()
    await db.control_tests.insert_one(test_dict)
    
    # Auto-create issue if test failed
    if test.result == "Fail":
        control = await db.unified_controls.find_one({"id": test.unified_control_id}, {"_id": 0})
        issue = Issue(
            title=f"Control Test Failed: {control.get('name', 'Unknown')}",
            description=f"Control test failed. Notes: {test.notes or 'No notes provided'}",
            control_test_id=test.id,
            unified_control_id=test.unified_control_id,
            severity="High",
            status="Open",
            assigned_to=test.tester
        )
        issue_dict = issue.model_dump()
        issue_dict['created_at'] = issue_dict['created_at'].isoformat()
        issue_dict['updated_at'] = issue_dict['updated_at'].isoformat()
        await db.issues.insert_one(issue_dict)
    
    return test

# ============ EVIDENCE ENDPOINTS ============

@api_router.get("/evidence", response_model=List[Evidence])
async def get_evidence():
    evidence = await db.evidence.find({}, {"_id": 0}).to_list(1000)
    for ev in evidence:
        if isinstance(ev.get('collected_at'), str):
            ev['collected_at'] = datetime.fromisoformat(ev['collected_at'])
    return evidence

@api_router.post("/evidence/upload")
async def upload_evidence(
    control_test_id: str,
    unified_control_id: str,
    description: str,
    file: UploadFile = File(...)
):
    file_id = str(uuid.uuid4())
    file_path = UPLOADS_DIR / f"{file_id}_{file.filename}"
    
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    evidence = Evidence(
        control_test_id=control_test_id,
        unified_control_id=unified_control_id,
        evidence_type="Manual Upload",
        description=description,
        automated=False,
        file_path=str(file_path),
        file_name=file.filename
    )
    
    ev_dict = evidence.model_dump()
    ev_dict['collected_at'] = ev_dict['collected_at'].isoformat()
    await db.evidence.insert_one(ev_dict)
    
    return {"message": "Evidence uploaded", "evidence_id": evidence.id}

@api_router.post("/evidence/automated")
async def create_automated_evidence(evidence: Evidence):
    ev_dict = evidence.model_dump()
    ev_dict['collected_at'] = ev_dict['collected_at'].isoformat()
    await db.evidence.insert_one(ev_dict)
    return evidence

# ============ ISSUE MANAGEMENT ENDPOINTS ============

@api_router.get("/issues", response_model=List[Issue])
async def get_issues():
    issues = await db.issues.find({}, {"_id": 0}).to_list(1000)
    for issue in issues:
        if isinstance(issue.get('created_at'), str):
            issue['created_at'] = datetime.fromisoformat(issue['created_at'])
        if isinstance(issue.get('updated_at'), str):
            issue['updated_at'] = datetime.fromisoformat(issue['updated_at'])
    return issues

@api_router.post("/issues", response_model=Issue)
async def create_issue(issue: Issue):
    issue_dict = issue.model_dump()
    issue_dict['created_at'] = issue_dict['created_at'].isoformat()
    issue_dict['updated_at'] = issue_dict['updated_at'].isoformat()
    await db.issues.insert_one(issue_dict)
    return issue

@api_router.patch("/issues/{issue_id}/status")
async def update_issue_status(issue_id: str, status: str):
    await db.issues.update_one(
        {"id": issue_id},
        {"$set": {"status": status, "updated_at": datetime.now(timezone.utc).isoformat()}}
    )
    return {"message": "Issue status updated"}

@api_router.patch("/issues/{issue_id}/exception")
async def add_exception(issue_id: str, exception_details: Dict):
    await db.issues.update_one(
        {"id": issue_id},
        {"$set": {
            "has_exception": True,
            "exception_details": exception_details,
            "updated_at": datetime.now(timezone.utc).isoformat()
        }}
    )
    return {"message": "Exception added"}

# ============ RISK MANAGEMENT ENDPOINTS ============

@api_router.get("/risks", response_model=List[Risk])
async def get_risks():
    risks = await db.risks.find({}, {"_id": 0}).to_list(1000)
    for risk in risks:
        if isinstance(risk.get('created_at'), str):
            risk['created_at'] = datetime.fromisoformat(risk['created_at'])
    return risks

@api_router.post("/risks", response_model=Risk)
async def create_risk(risk: Risk):
    risk_dict = risk.model_dump()
    risk_dict['created_at'] = risk_dict['created_at'].isoformat()
    await db.risks.insert_one(risk_dict)
    return risk

@api_router.post("/risks/ai-suggest")
async def ai_suggest_risks(industry: str = "General"):
    prompt = f"""As a GRC expert, suggest top 10 risks for {industry} industry.
Provide in JSON format:
{{
  "risks": [
    {{"name": "Risk Name", "description": "Description", "category": "Category", "inherent_score": 7.5}}
  ]
}}"""
    
    response = await get_ai_analysis(prompt)
    try:
        parsed = json.loads(response)
        return parsed
    except:
        return {"risks": [], "error": "Could not parse AI response"}

# ============ KRI ENDPOINTS ============

@api_router.get("/kris", response_model=List[KRI])
async def get_kris():
    kris = await db.kris.find({}, {"_id": 0}).to_list(1000)
    for kri in kris:
        if isinstance(kri.get('created_at'), str):
            kri['created_at'] = datetime.fromisoformat(kri['created_at'])
    return kris

@api_router.post("/kris", response_model=KRI)
async def create_kri(kri: KRI):
    kri_dict = kri.model_dump()
    kri_dict['created_at'] = kri_dict['created_at'].isoformat()
    await db.kris.insert_one(kri_dict)
    return kri

# ============ KCI ENDPOINTS ============

@api_router.get("/kcis", response_model=List[KCI])
async def get_kcis():
    kcis = await db.kcis.find({}, {"_id": 0}).to_list(1000)
    for kci in kcis:
        if isinstance(kci.get('created_at'), str):
            kci['created_at'] = datetime.fromisoformat(kci['created_at'])
    return kcis

@api_router.post("/kcis", response_model=KCI)
async def create_kci(kci: KCI):
    kci_dict = kci.model_dump()
    kci_dict['created_at'] = kci_dict['created_at'].isoformat()
    await db.kcis.insert_one(kci_dict)
    return kci

# ============ AI ANALYSIS ENDPOINT ============

@api_router.post("/ai/analyze", response_model=AIAnalysisResponse)
async def analyze_with_ai(request: AIAnalysisRequest):
    try:
        prompt = f"""Analyze the following GRC data:
Type: {request.analysis_type}
Context: {json.dumps(request.context, indent=2)}

Provide analysis and recommendations in JSON format:
{{
  "analysis": "Your analysis here",
  "recommendations": ["rec1", "rec2", ...]
}}"""
        
        response = await get_ai_analysis(prompt)
        
        try:
            parsed = json.loads(response)
            return AIAnalysisResponse(
                analysis=parsed.get('analysis', response),
                recommendations=parsed.get('recommendations', [])
            )
        except:
            return AIAnalysisResponse(
                analysis=response,
                recommendations=["Review analysis for action items"]
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============ DASHBOARD ENDPOINT ============

@api_router.get("/dashboard/stats")
async def get_dashboard_stats():
    # Calculate real-time stats from actual data
    frameworks = await db.frameworks.find({"enabled": True}, {"_id": 0}).to_list(100)
    unified_controls = await db.unified_controls.find({}, {"_id": 0}).to_list(1000)
    control_tests = await db.control_tests.find({}, {"_id": 0}).to_list(1000)
    issues = await db.issues.find({}, {"_id": 0}).to_list(1000)
    risks = await db.risks.find({}, {"_id": 0}).to_list(1000)
    
    # Calculate control effectiveness
    passed_tests = [t for t in control_tests if t.get('result') == 'Pass']
    control_effectiveness = (len(passed_tests) / len(control_tests) * 100) if control_tests else 0
    
    # Calculate average risk score
    avg_risk = sum(r.get('residual_risk_score', 0) for r in risks) / len(risks) if risks else 0
    
    # Issue stats
    open_issues = [i for i in issues if i.get('status') not in ['Resolved', 'Closed']]
    
    return {
        "enabled_frameworks": len(frameworks),
        "total_unified_controls": len(unified_controls),
        "control_effectiveness": round(control_effectiveness, 1),
        "total_tests_performed": len(control_tests),
        "passed_tests": len(passed_tests),
        "failed_tests": len(control_tests) - len(passed_tests),
        "open_issues": len(open_issues),
        "total_issues": len(issues),
        "total_risks": len(risks),
        "avg_residual_risk": round(avg_risk, 2)
    }

# ============ SEED DATA ENDPOINT ============

@api_router.post("/seed-production-data")
async def seed_production_data():
    """Seeds the database with production-ready framework and sample data"""
    
    # Clear existing data
    await db.frameworks.delete_many({})
    await db.framework_controls.delete_many({})
    await db.unified_controls.delete_many({})
    await db.policies.delete_many({})
    await db.control_tests.delete_many({})
    await db.evidence.delete_many({})
    await db.issues.delete_many({})
    await db.risks.delete_many({})
    await db.kris.delete_many({})
    await db.kcis.delete_many({})
    
    # Import framework data
    from seed_data import get_frameworks_data, get_sample_data
    
    frameworks_data = get_frameworks_data()
    sample_data = get_sample_data()
    
    # Insert frameworks
    for fw in frameworks_data['frameworks']:
        await db.frameworks.insert_one(fw)
    
    # Insert framework controls
    for ctrl in frameworks_data['framework_controls']:
        await db.framework_controls.insert_one(ctrl)
    
    # Insert sample data
    for uc in sample_data['unified_controls']:
        await db.unified_controls.insert_one(uc)
    
    for pol in sample_data['policies']:
        await db.policies.insert_one(pol)
    
    return {"message": "Production data seeded successfully"}

@api_router.get("/")
async def root():
    return {"message": "GRC Intelligence Platform API - Production Ready"}

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()