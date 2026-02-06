from fastapi import FastAPI, APIRouter, HTTPException
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Dict
import uuid
from datetime import datetime, timezone
from emergentintegrations.llm.chat import LlmChat, UserMessage
import json

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

app = FastAPI()
api_router = APIRouter(prefix="/api")

EMERGENT_LLM_KEY = os.environ.get('EMERGENT_LLM_KEY')

class Risk(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    category: str
    inherent_risk_score: float
    residual_risk_score: float
    status: str
    owner: str
    kris: List[str] = []
    linked_controls: List[str] = []
    ai_insights: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Control(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    ccf_id: str
    internal_policy: str
    control_type: str
    frequency: str
    owner: str
    health_score: float
    status: str
    linked_risks: List[str] = []
    kcis: List[str] = []
    last_tested: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class KRI(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    risk_id: str
    current_value: float
    threshold: float
    status: str
    trend: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class KCI(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    kri_id: str
    control_id: str
    current_value: float
    target: float
    status: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Evidence(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    control_id: str
    evidence_type: str
    description: str
    collected_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    automated: bool
    status: str

class AIAnalysisRequest(BaseModel):
    analysis_type: str
    context: Dict

class AIAnalysisResponse(BaseModel):
    analysis: str
    recommendations: List[str]

async def get_ai_analysis(prompt: str) -> str:
    try:
        chat = LlmChat(
            api_key=EMERGENT_LLM_KEY,
            session_id=str(uuid.uuid4()),
            system_message="You are a GRC (Governance, Risk, and Compliance) expert AI assistant. Provide strategic, actionable insights."
        ).with_model("openai", "gpt-4o")
        
        user_message = UserMessage(text=prompt)
        response = await chat.send_message(user_message)
        return response
    except Exception as e:
        logging.error(f"AI analysis error: {str(e)}")
        return "AI analysis temporarily unavailable"

@api_router.get("/")
async def root():
    return {"message": "GRC Intelligence Platform API"}

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

@api_router.get("/controls", response_model=List[Control])
async def get_controls():
    controls = await db.controls.find({}, {"_id": 0}).to_list(1000)
    for control in controls:
        if isinstance(control.get('created_at'), str):
            control['created_at'] = datetime.fromisoformat(control['created_at'])
    return controls

@api_router.post("/controls", response_model=Control)
async def create_control(control: Control):
    control_dict = control.model_dump()
    control_dict['created_at'] = control_dict['created_at'].isoformat()
    await db.controls.insert_one(control_dict)
    return control

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

@api_router.get("/evidence", response_model=List[Evidence])
async def get_evidence():
    evidence = await db.evidence.find({}, {"_id": 0}).to_list(1000)
    for ev in evidence:
        if isinstance(ev.get('collected_at'), str):
            ev['collected_at'] = datetime.fromisoformat(ev['collected_at'])
    return evidence

@api_router.post("/evidence", response_model=Evidence)
async def create_evidence(evidence: Evidence):
    evidence_dict = evidence.model_dump()
    evidence_dict['collected_at'] = evidence_dict['collected_at'].isoformat()
    await db.evidence.insert_one(evidence_dict)
    return evidence

@api_router.post("/ai/analyze", response_model=AIAnalysisResponse)
async def analyze_with_ai(request: AIAnalysisRequest):
    try:
        if request.analysis_type == "control_health_impact":
            prompt = f"""Analyze how control health impacts risk rating:
Context: {json.dumps(request.context)}

Provide:
1. Impact analysis of control health on risk score
2. Specific recommendations to improve control effectiveness
3. Priority actions

Format as JSON with 'analysis' and 'recommendations' keys."""
        
        elif request.analysis_type == "risk_kri_mapping":
            prompt = f"""Analyze Risk-KRI-KCI relationships:
Context: {json.dumps(request.context)}

Provide:
1. Analysis of KRI effectiveness for risk monitoring
2. Recommendations for KCI improvements
3. Automated monitoring suggestions

Format as JSON with 'analysis' and 'recommendations' keys."""
        
        elif request.analysis_type == "ccf_mapping":
            prompt = f"""Map CCF controls to internal policy:
Context: {json.dumps(request.context)}

Provide:
1. Mapping analysis and coverage gaps
2. Recommendations for policy alignment
3. Automation opportunities

Format as JSON with 'analysis' and 'recommendations' keys."""
        
        else:
            prompt = f"""Analyze GRC data:
Context: {json.dumps(request.context)}

Provide strategic insights and actionable recommendations.
Format as JSON with 'analysis' and 'recommendations' keys."""
        
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
                recommendations=["Review analysis for specific action items"]
            )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@api_router.post("/seed-data")
async def seed_data():
    await db.risks.delete_many({})
    await db.controls.delete_many({})
    await db.kris.delete_many({})
    await db.kcis.delete_many({})
    await db.evidence.delete_many({})
    
    sample_risks = [
        {"id": "r1", "name": "Data Breach", "description": "Unauthorized access to sensitive customer data", "category": "Cybersecurity", "inherent_risk_score": 8.5, "residual_risk_score": 4.2, "status": "Active", "owner": "CISO", "kris": ["kri1", "kri2"], "linked_controls": ["c1", "c2"], "ai_insights": "High priority - implement MFA", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "r2", "name": "Regulatory Non-Compliance", "description": "Failure to meet GDPR requirements", "category": "Compliance", "inherent_risk_score": 7.8, "residual_risk_score": 3.5, "status": "Active", "owner": "CCO", "kris": ["kri3"], "linked_controls": ["c3", "c4"], "ai_insights": "Review privacy policies quarterly", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "r3", "name": "Third-Party Risk", "description": "Vendor security vulnerabilities", "category": "Operational", "inherent_risk_score": 7.2, "residual_risk_score": 4.0, "status": "Active", "owner": "Procurement", "kris": ["kri4"], "linked_controls": ["c5"], "ai_insights": "Implement vendor risk scoring", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "r4", "name": "Insider Threat", "description": "Malicious or negligent employee actions", "category": "Security", "inherent_risk_score": 6.8, "residual_risk_score": 3.8, "status": "Active", "owner": "HR/Security", "kris": ["kri5"], "linked_controls": ["c6"], "ai_insights": "Enhanced monitoring needed", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "r5", "name": "Business Continuity", "description": "System downtime affecting operations", "category": "Operational", "inherent_risk_score": 8.0, "residual_risk_score": 3.2, "status": "Active", "owner": "CTO", "kris": ["kri6"], "linked_controls": ["c7"], "ai_insights": "DR tests quarterly", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "r6", "name": "Financial Fraud", "description": "Fraudulent transactions or embezzlement", "category": "Financial", "inherent_risk_score": 7.5, "residual_risk_score": 2.8, "status": "Active", "owner": "CFO", "kris": ["kri7"], "linked_controls": ["c8"], "ai_insights": "Implement real-time alerts", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "r7", "name": "Ransomware Attack", "description": "Encryption of critical systems", "category": "Cybersecurity", "inherent_risk_score": 9.0, "residual_risk_score": 4.5, "status": "Active", "owner": "CISO", "kris": ["kri8"], "linked_controls": ["c9"], "ai_insights": "Backup verification critical", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "r8", "name": "Privacy Violation", "description": "Unauthorized data processing", "category": "Privacy", "inherent_risk_score": 7.0, "residual_risk_score": 3.0, "status": "Active", "owner": "DPO", "kris": ["kri9"], "linked_controls": ["c10"], "ai_insights": "Update consent mechanisms", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "r9", "name": "Supply Chain Disruption", "description": "Critical supplier failure", "category": "Operational", "inherent_risk_score": 6.5, "residual_risk_score": 3.5, "status": "Active", "owner": "COO", "kris": ["kri10"], "linked_controls": ["c11"], "ai_insights": "Diversify supplier base", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "r10", "name": "Reputational Damage", "description": "Negative publicity affecting brand", "category": "Strategic", "inherent_risk_score": 7.8, "residual_risk_score": 4.2, "status": "Active", "owner": "CMO", "kris": [], "linked_controls": ["c12"], "ai_insights": "Social media monitoring", "created_at": datetime.now(timezone.utc).isoformat()},
    ]
    
    sample_controls = [
        {"id": "c1", "name": "Multi-Factor Authentication", "description": "Enforce MFA for all user accounts", "ccf_id": "CCF-AC-001", "internal_policy": "POL-SEC-100", "control_type": "Preventive", "frequency": "Continuous", "owner": "IT Security", "health_score": 92.0, "status": "Effective", "linked_risks": ["r1"], "kcis": ["kci1"], "last_tested": "2026-01-10", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "c2", "name": "Encryption at Rest", "description": "Encrypt all stored sensitive data", "ccf_id": "CCF-DS-002", "internal_policy": "POL-DATA-200", "control_type": "Preventive", "frequency": "Continuous", "owner": "IT Security", "health_score": 88.0, "status": "Effective", "linked_risks": ["r1"], "kcis": ["kci2"], "last_tested": "2026-01-08", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "c3", "name": "Privacy Impact Assessment", "description": "Conduct PIA for new data processing", "ccf_id": "CCF-PR-003", "internal_policy": "POL-PRIV-150", "control_type": "Detective", "frequency": "Quarterly", "owner": "Privacy Office", "health_score": 85.0, "status": "Effective", "linked_risks": ["r2"], "kcis": ["kci3"], "last_tested": "2026-01-05", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "c4", "name": "GDPR Compliance Review", "description": "Quarterly GDPR compliance audit", "ccf_id": "CCF-CM-004", "internal_policy": "POL-COMP-300", "control_type": "Detective", "frequency": "Quarterly", "owner": "Compliance", "health_score": 90.0, "status": "Effective", "linked_risks": ["r2"], "kcis": ["kci4"], "last_tested": "2026-01-03", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "c5", "name": "Vendor Security Assessment", "description": "Annual vendor security review", "ccf_id": "CCF-TP-005", "internal_policy": "POL-VEND-400", "control_type": "Detective", "frequency": "Annual", "owner": "Procurement", "health_score": 78.0, "status": "Needs Improvement", "linked_risks": ["r3"], "kcis": ["kci5"], "last_tested": "2025-12-15", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "c6", "name": "Access Review", "description": "Quarterly user access review", "ccf_id": "CCF-AC-006", "internal_policy": "POL-IAM-250", "control_type": "Detective", "frequency": "Quarterly", "owner": "IT Security", "health_score": 82.0, "status": "Effective", "linked_risks": ["r4"], "kcis": ["kci6"], "last_tested": "2026-01-01", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "c7", "name": "Disaster Recovery Test", "description": "Quarterly DR plan testing", "ccf_id": "CCF-BC-007", "internal_policy": "POL-BC-500", "control_type": "Corrective", "frequency": "Quarterly", "owner": "IT Operations", "health_score": 95.0, "status": "Effective", "linked_risks": ["r5"], "kcis": ["kci7"], "last_tested": "2026-01-12", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "c8", "name": "Transaction Monitoring", "description": "Real-time fraud detection", "ccf_id": "CCF-FM-008", "internal_policy": "POL-FIN-600", "control_type": "Detective", "frequency": "Continuous", "owner": "Finance", "health_score": 93.0, "status": "Effective", "linked_risks": ["r6"], "kcis": ["kci8"], "last_tested": "2026-01-13", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "c9", "name": "Backup Verification", "description": "Daily backup integrity checks", "ccf_id": "CCF-BC-009", "internal_policy": "POL-BKP-700", "control_type": "Preventive", "frequency": "Daily", "owner": "IT Operations", "health_score": 89.0, "status": "Effective", "linked_risks": ["r7"], "kcis": ["kci9"], "last_tested": "2026-01-14", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "c10", "name": "Consent Management", "description": "User consent tracking system", "ccf_id": "CCF-PR-010", "internal_policy": "POL-PRIV-180", "control_type": "Preventive", "frequency": "Continuous", "owner": "Privacy Office", "health_score": 87.0, "status": "Effective", "linked_risks": ["r8"], "kcis": ["kci10"], "last_tested": "2026-01-11", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "c11", "name": "Supplier Diversification", "description": "Multiple supplier strategy", "ccf_id": "CCF-TP-011", "internal_policy": "POL-PROC-450", "control_type": "Preventive", "frequency": "Annual", "owner": "Procurement", "health_score": 75.0, "status": "Needs Improvement", "linked_risks": ["r9"], "kcis": [], "last_tested": "2025-12-20", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "c12", "name": "Social Media Monitoring", "description": "Brand reputation tracking", "ccf_id": "CCF-CM-012", "internal_policy": "POL-COM-800", "control_type": "Detective", "frequency": "Continuous", "owner": "Marketing", "health_score": 80.0, "status": "Effective", "linked_risks": ["r10"], "kcis": [], "last_tested": "2026-01-09", "created_at": datetime.now(timezone.utc).isoformat()},
    ]
    
    sample_kris = [
        {"id": "kri1", "name": "Failed Login Attempts", "description": "Number of failed login attempts per hour", "risk_id": "r1", "current_value": 45.0, "threshold": 100.0, "status": "Normal", "trend": "Stable", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "kri2", "name": "Data Access Violations", "description": "Unauthorized data access attempts", "risk_id": "r1", "current_value": 12.0, "threshold": 50.0, "status": "Normal", "trend": "Decreasing", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "kri3", "name": "Compliance Gaps", "description": "Number of open compliance findings", "risk_id": "r2", "current_value": 8.0, "threshold": 20.0, "status": "Normal", "trend": "Stable", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "kri4", "name": "Vendor Security Score", "description": "Average vendor security rating", "risk_id": "r3", "current_value": 72.0, "threshold": 80.0, "status": "Warning", "trend": "Stable", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "kri5", "name": "Privileged Access Usage", "description": "Abnormal privileged account activity", "risk_id": "r4", "current_value": 15.0, "threshold": 30.0, "status": "Normal", "trend": "Stable", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "kri6", "name": "System Uptime", "description": "Percentage of system availability", "risk_id": "r5", "current_value": 99.8, "threshold": 99.0, "status": "Normal", "trend": "Stable", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "kri7", "name": "Suspicious Transactions", "description": "Flagged transactions per day", "risk_id": "r6", "current_value": 5.0, "threshold": 20.0, "status": "Normal", "trend": "Decreasing", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "kri8", "name": "Malware Detections", "description": "Malware incidents per week", "risk_id": "r7", "current_value": 3.0, "threshold": 10.0, "status": "Normal", "trend": "Stable", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "kri9", "name": "Privacy Complaints", "description": "Privacy-related complaints per month", "risk_id": "r8", "current_value": 2.0, "threshold": 10.0, "status": "Normal", "trend": "Stable", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "kri10", "name": "Supplier Lead Time", "description": "Average supplier delivery delay (days)", "risk_id": "r9", "current_value": 4.0, "threshold": 7.0, "status": "Normal", "trend": "Increasing", "created_at": datetime.now(timezone.utc).isoformat()},
    ]
    
    sample_kcis = [
        {"id": "kci1", "name": "MFA Adoption Rate", "description": "Percentage of users with MFA enabled", "kri_id": "kri1", "control_id": "c1", "current_value": 98.0, "target": 100.0, "status": "On Track", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "kci2", "name": "Encryption Coverage", "description": "Percentage of data encrypted", "kri_id": "kri2", "control_id": "c2", "current_value": 95.0, "target": 100.0, "status": "On Track", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "kci3", "name": "PIA Completion Rate", "description": "PIAs completed on time", "kri_id": "kri3", "control_id": "c3", "current_value": 90.0, "target": 95.0, "status": "On Track", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "kci4", "name": "GDPR Audit Findings", "description": "Number of GDPR audit findings", "kri_id": "kri3", "control_id": "c4", "current_value": 3.0, "target": 0.0, "status": "Needs Attention", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "kci5", "name": "Vendor Assessments", "description": "Vendors assessed annually", "kri_id": "kri4", "control_id": "c5", "current_value": 85.0, "target": 100.0, "status": "Needs Attention", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "kci6", "name": "Access Review Completion", "description": "Quarterly reviews completed", "kri_id": "kri5", "control_id": "c6", "current_value": 92.0, "target": 100.0, "status": "On Track", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "kci7", "name": "DR Test Success Rate", "description": "Successful DR tests", "kri_id": "kri6", "control_id": "c7", "current_value": 100.0, "target": 100.0, "status": "Excellent", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "kci8", "name": "Fraud Detection Rate", "description": "Fraudulent transactions detected", "kri_id": "kri7", "control_id": "c8", "current_value": 99.0, "target": 98.0, "status": "Excellent", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "kci9", "name": "Backup Success Rate", "description": "Successful backups percentage", "kri_id": "kri8", "control_id": "c9", "current_value": 99.5, "target": 99.0, "status": "Excellent", "created_at": datetime.now(timezone.utc).isoformat()},
        {"id": "kci10", "name": "Consent Tracking", "description": "User consents properly tracked", "kri_id": "kri9", "control_id": "c10", "current_value": 97.0, "target": 100.0, "status": "On Track", "created_at": datetime.now(timezone.utc).isoformat()},
    ]
    
    sample_evidence = [
        {"id": "e1", "control_id": "c1", "evidence_type": "Log Report", "description": "MFA enrollment logs", "collected_at": datetime.now(timezone.utc).isoformat(), "automated": True, "status": "Collected"},
        {"id": "e2", "control_id": "c2", "evidence_type": "Scan Report", "description": "Encryption verification scan", "collected_at": datetime.now(timezone.utc).isoformat(), "automated": True, "status": "Collected"},
        {"id": "e3", "control_id": "c3", "evidence_type": "Assessment Report", "description": "Q4 2025 PIA report", "collected_at": datetime.now(timezone.utc).isoformat(), "automated": False, "status": "Collected"},
        {"id": "e4", "control_id": "c7", "evidence_type": "Test Results", "description": "DR test results Q1 2026", "collected_at": datetime.now(timezone.utc).isoformat(), "automated": True, "status": "Collected"},
    ]
    
    await db.risks.insert_many(sample_risks)
    await db.controls.insert_many(sample_controls)
    await db.kris.insert_many(sample_kris)
    await db.kcis.insert_many(sample_kcis)
    await db.evidence.insert_many(sample_evidence)
    
    return {"message": "Sample data seeded successfully"}

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