"""Database service for MongoDB operations - Synchronous version"""
from pymongo import MongoClient
from typing import List, Dict, Optional
import os
from dotenv import load_dotenv

# Load .env from the reflex-grc directory
load_dotenv("/app/reflex-grc/.env")

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "grc_reflex_db")

print(f"[DB] Connecting to MongoDB: {MONGO_URL}, DB: {DB_NAME}")


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
    
    # Frameworks - Using sync pymongo
    def get_frameworks(self) -> List[Dict]:
        cursor = self._db.frameworks.find({}, {"_id": 0})
        return list(cursor)
    
    def toggle_framework(self, framework_id: str, enabled: bool):
        self._db.frameworks.update_one(
            {"id": framework_id},
            {"$set": {"enabled": enabled}}
        )
    
    # Unified Controls
    def get_unified_controls(self) -> List[Dict]:
        cursor = self._db.unified_controls.find({}, {"_id": 0})
        return list(cursor)
    
    def create_unified_control(self, control: Dict):
        self._db.unified_controls.insert_one(control)
    
    # Policies
    def get_policies(self) -> List[Dict]:
        cursor = self._db.policies.find({}, {"_id": 0})
        return list(cursor)
    
    def create_policy(self, policy: Dict):
        self._db.policies.insert_one(policy)
    
    # Control Tests
    def get_control_tests(self) -> List[Dict]:
        cursor = self._db.control_tests.find({}, {"_id": 0})
        return list(cursor)
    
    def create_control_test(self, test: Dict):
        self._db.control_tests.insert_one(test)
    
    # Issues
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
    
    # Risks
    def get_risks(self) -> List[Dict]:
        cursor = self._db.risks.find({}, {"_id": 0})
        return list(cursor)
    
    def create_risk(self, risk: Dict):
        self._db.risks.insert_one(risk)
    
    # KRIs
    def get_kris(self) -> List[Dict]:
        cursor = self._db.kris.find({}, {"_id": 0})
        return list(cursor)
    
    def create_kri(self, kri: Dict):
        self._db.kris.insert_one(kri)
    
    # KCIs
    def get_kcis(self) -> List[Dict]:
        cursor = self._db.kcis.find({}, {"_id": 0})
        return list(cursor)
    
    def create_kci(self, kci: Dict):
        self._db.kcis.insert_one(kci)
    
    # Dashboard Stats
    def get_dashboard_stats(self) -> Dict:
        frameworks = self.get_frameworks()
        controls = self.get_unified_controls()
        tests = self.get_control_tests()
        issues = self.get_issues()
        risks = self.get_risks()
        
        passed_tests = [t for t in tests if t.get("result") == "Pass"]
        control_effectiveness = (len(passed_tests) / len(tests) * 100) if tests else 0
        
        open_issues = [i for i in issues if i.get("status") not in ["Resolved", "Closed"]]
        
        avg_risk = sum(r.get("residual_risk_score", 0) for r in risks) / len(risks) if risks else 0
        
        return {
            "enabled_frameworks": len([f for f in frameworks if f.get("enabled")]),
            "total_unified_controls": len(controls),
            "control_effectiveness": round(control_effectiveness, 1),
            "total_tests": len(tests),
            "passed_tests": len(passed_tests),
            "open_issues": len(open_issues),
            "total_issues": len(issues),
            "total_risks": len(risks),
            "avg_residual_risk": round(avg_risk, 2)
        }


# Global database instance
db_service = DatabaseService()
