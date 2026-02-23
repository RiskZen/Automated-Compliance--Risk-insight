"""Database service for MongoDB operations - Synchronous version"""
from pymongo import MongoClient
from typing import List, Dict, Optional
import os
from dotenv import load_dotenv
import hashlib
from datetime import datetime

# Load .env from the reflex-grc directory
load_dotenv("/app/reflex-grc/.env")

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "grc_reflex_db")

print(f"[DB] Connecting to MongoDB: {MONGO_URL}, DB: {DB_NAME}")


def hash_password(password: str) -> str:
    """Simple password hashing"""
    return hashlib.sha256(password.encode()).hexdigest()


class DatabaseService:
    _instance = None
    _client = None
    _db = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if DatabaseService._client is None:
            DatabaseService._client = MongoClient(MONGO_URL)
            DatabaseService._db = DatabaseService._client[DB_NAME]
            print(f"[DB] Connected to database: {DB_NAME}")
    
    @property
    def db(self):
        return DatabaseService._db
    
    # ========== AUTH ==========
    def get_user_by_email(self, email: str) -> Optional[Dict]:
        return self._db.users.find_one({"email": email}, {"_id": 0})
    
    def verify_user(self, email: str, password: str) -> Optional[Dict]:
        user = self.get_user_by_email(email)
        if user and user.get("password") == hash_password(password):
            return {k: v for k, v in user.items() if k != "password"}
        return None
    
    def create_user(self, user: Dict):
        user["password"] = hash_password(user["password"])
        self._db.users.insert_one(user)
    
    # ========== FRAMEWORKS ==========
    def get_frameworks(self) -> List[Dict]:
        cursor = self._db.frameworks.find({}, {"_id": 0})
        return list(cursor)
    
    def toggle_framework(self, framework_id: str, enabled: bool):
        self._db.frameworks.update_one(
            {"id": framework_id},
            {"$set": {"enabled": enabled}}
        )
        self.log_audit("system", "system@grc.local", "UPDATE", "Framework", 
                      f"{'Enabled' if enabled else 'Disabled'} framework: {framework_id}")
    
    # ========== UNIFIED CONTROLS ==========
    def get_unified_controls(self) -> List[Dict]:
        cursor = self._db.unified_controls.find({}, {"_id": 0})
        return list(cursor)
    
    def create_unified_control(self, control: Dict):
        self._db.unified_controls.insert_one(control)
    
    # ========== POLICIES ==========
    def get_policies(self) -> List[Dict]:
        cursor = self._db.policies.find({}, {"_id": 0})
        return list(cursor)
    
    def create_policy(self, policy: Dict):
        self._db.policies.insert_one(policy)
    
    # ========== CONNECTORS ==========
    def get_connectors(self) -> List[Dict]:
        cursor = self._db.connectors.find({}, {"_id": 0})
        return list(cursor)
    
    def update_connector_status(self, connector_id: str, status: str):
        self._db.connectors.update_one(
            {"id": connector_id},
            {"$set": {"status": status, "last_sync": datetime.utcnow().isoformat() if status == "Connected" else None}}
        )
    
    # ========== CONTROL TESTS ==========
    def get_control_tests(self) -> List[Dict]:
        cursor = self._db.control_tests.find({}, {"_id": 0})
        return list(cursor)
    
    def create_control_test(self, test: Dict):
        self._db.control_tests.insert_one(test)
    
    # ========== ISSUES ==========
    def get_issues(self) -> List[Dict]:
        cursor = self._db.issues.find({}, {"_id": 0})
        return list(cursor)
    
    def create_issue(self, issue: Dict):
        self._db.issues.insert_one(issue)
    
    def update_issue_status(self, issue_id: str, status: str):
        self._db.issues.update_one(
            {"id": issue_id},
            {"$set": {"status": status}}
        )
    
    # ========== RISKS ==========
    def get_risks(self) -> List[Dict]:
        cursor = self._db.risks.find({}, {"_id": 0})
        return list(cursor)
    
    def create_risk(self, risk: Dict):
        self._db.risks.insert_one(risk)
    
    # ========== KRIs ==========
    def get_kris(self) -> List[Dict]:
        cursor = self._db.kris.find({}, {"_id": 0})
        return list(cursor)
    
    def create_kri(self, kri: Dict):
        self._db.kris.insert_one(kri)
    
    # ========== KCIs ==========
    def get_kcis(self) -> List[Dict]:
        cursor = self._db.kcis.find({}, {"_id": 0})
        return list(cursor)
    
    def create_kci(self, kci: Dict):
        self._db.kcis.insert_one(kci)
    
    # ========== AI MODELS ==========
    def get_ai_models(self) -> List[Dict]:
        cursor = self._db.ai_models.find({}, {"_id": 0})
        return list(cursor)
    
    def create_ai_model(self, model: Dict):
        self._db.ai_models.insert_one(model)
    
    def update_ai_model(self, model_id: str, updates: Dict):
        self._db.ai_models.update_one(
            {"id": model_id},
            {"$set": updates}
        )
    
    # ========== AI ASSESSMENTS ==========
    def get_ai_assessments(self) -> List[Dict]:
        cursor = self._db.ai_assessments.find({}, {"_id": 0})
        return list(cursor)
    
    def create_ai_assessment(self, assessment: Dict):
        self._db.ai_assessments.insert_one(assessment)
    
    # ========== AUDIT LOGS ==========
    def get_audit_logs(self, limit: int = 100) -> List[Dict]:
        cursor = self._db.audit_logs.find({}, {"_id": 0}).sort("timestamp", -1).limit(limit)
        return list(cursor)
    
    def log_audit(self, user_id: str, user_email: str, action: str, resource: str, details: str, ip_address: str = "system"):
        import uuid
        log = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "user_id": user_id,
            "user_email": user_email,
            "action": action,
            "resource": resource,
            "details": details,
            "ip_address": ip_address
        }
        self._db.audit_logs.insert_one(log)
    
    # ========== DASHBOARD STATS ==========
    def get_dashboard_stats(self) -> Dict:
        frameworks = self.get_frameworks()
        controls = self.get_unified_controls()
        tests = self.get_control_tests()
        issues = self.get_issues()
        risks = self.get_risks()
        ai_models = self.get_ai_models()
        
        passed_tests = [t for t in tests if t.get("result") == "Pass"]
        control_effectiveness = (len(passed_tests) / len(tests) * 100) if tests else 0
        
        open_issues = [i for i in issues if i.get("status") not in ["Resolved", "Closed"]]
        
        avg_risk = sum(r.get("residual_risk_score", 0) for r in risks) / len(risks) if risks else 0
        
        # AI stats
        production_models = [m for m in ai_models if m.get("status") == "Production"]
        high_risk_models = [m for m in ai_models if m.get("risk_level") in ["High", "Critical"]]
        
        return {
            "enabled_frameworks": len([f for f in frameworks if f.get("enabled")]),
            "total_unified_controls": len(controls),
            "control_effectiveness": round(control_effectiveness, 1),
            "total_tests": len(tests),
            "passed_tests": len(passed_tests),
            "open_issues": len(open_issues),
            "total_issues": len(issues),
            "total_risks": len(risks),
            "avg_residual_risk": round(avg_risk, 2),
            "total_ai_models": len(ai_models),
            "production_ai_models": len(production_models),
            "high_risk_ai_models": len(high_risk_models)
        }


# Global database instance
db_service = DatabaseService()
