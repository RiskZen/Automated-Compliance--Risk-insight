"""Global state management for GRC Platform"""
import reflex as rx
from typing import List, Dict
import uuid
from datetime import datetime
from .database import db_service
from .ai_service import ai_service

class GRCState(rx.State):
    """Global state for the entire GRC application"""
    
    # Data
    frameworks: List[Dict] = []
    unified_controls: List[Dict] = []
    policies: List[Dict] = []
    control_tests: List[Dict] = []
    issues: List[Dict] = []
    risks: List[Dict] = []
    kris: List[Dict] = []
    kcis: List[Dict] = []
    
    # UI State
    loading: bool = False
    current_page: str = "dashboard"
    
    # Dashboard stats
    stats: Dict = {
        "enabled_frameworks": 0,
        "total_unified_controls": 0,
        "control_effectiveness": 0,
        "open_issues": 0,
        "total_risks": 0,
        "avg_residual_risk": 0
    }
    
    async def load_all_data(self):
        """Load all data from database"""
        self.loading = True
        yield
        
        self.frameworks = await db_service.get_frameworks()
        self.unified_controls = await db_service.get_unified_controls()
        self.policies = await db_service.get_policies()
        self.control_tests = await db_service.get_control_tests()
        self.issues = await db_service.get_issues()
        self.risks = await db_service.get_risks()
        self.kris = await db_service.get_kris()
        self.kcis = await db_service.get_kcis()
        self.stats = await db_service.get_dashboard_stats()
        
        self.loading = False
        yield
    
    def set_page(self, page: str):
        """Change current page"""
        self.current_page = page

class FrameworkState(GRCState):
    """State for framework management"""
    
    async def toggle_framework(self, framework_id: str):
        """Enable/disable a framework"""
        framework = next((f for f in self.frameworks if f["id"] == framework_id), None)
        if framework:
            new_status = not framework.get("enabled", False)
            await db_service.toggle_framework(framework_id, new_status)
            await self.load_all_data()
            yield rx.toast.success(f"Framework {'enabled' if new_status else 'disabled'}")

class ControlState(GRCState):
    """State for control management"""
    
    # Form fields
    new_control_ccf_id: str = ""
    new_control_name: str = ""
    new_control_description: str = ""
    new_control_type: str = "Preventive"
    new_control_frequency: str = "Continuous"
    new_control_owner: str = ""
    show_create_form: bool = False
    
    def toggle_create_form(self):
        self.show_create_form = not self.show_create_form
    
    async def create_control(self):
        """Create new unified control"""
        if not self.new_control_name or not self.new_control_ccf_id:
            yield rx.toast.error("Please fill required fields")
            return
        
        control = {
            "id": str(uuid.uuid4()),
            "ccf_id": self.new_control_ccf_id,
            "name": self.new_control_name,
            "description": self.new_control_description,
            "control_type": self.new_control_type,
            "frequency": self.new_control_frequency,
            "owner": self.new_control_owner,
            "mapped_framework_controls": [],
            "mapped_policies": [],
            "automation_possible": False,
            "created_at": datetime.utcnow().isoformat()
        }
        
        await db_service.create_unified_control(control)
        
        # Reset form
        self.new_control_ccf_id = ""
        self.new_control_name = ""
        self.new_control_description = ""
        self.new_control_owner = ""
        self.show_create_form = False
        
        await self.load_all_data()
        yield rx.toast.success("Control created successfully")

class PolicyState(GRCState):
    """State for policy management"""
    
    new_policy_id: str = ""
    new_policy_name: str = ""
    new_policy_description: str = ""
    new_policy_category: str = "Security"
    new_policy_owner: str = ""
    show_policy_form: bool = False
    
    def toggle_policy_form(self):
        self.show_policy_form = not self.show_policy_form
    
    async def create_policy(self):
        """Create new policy"""
        if not self.new_policy_name or not self.new_policy_id:
            yield rx.toast.error("Please fill required fields")
            return
        
        policy = {
            "id": str(uuid.uuid4()),
            "policy_id": self.new_policy_id,
            "name": self.new_policy_name,
            "description": self.new_policy_description,
            "category": self.new_policy_category,
            "owner": self.new_policy_owner,
            "status": "Active",
            "created_at": datetime.utcnow().isoformat()
        }
        
        await db_service.create_policy(policy)
        
        # Reset form
        self.new_policy_id = ""
        self.new_policy_name = ""
        self.new_policy_description = ""
        self.new_policy_owner = ""
        self.show_policy_form = False
        
        await self.load_all_data()
        yield rx.toast.success("Policy created successfully")

class RiskState(GRCState):
    """State for risk management"""
    
    new_risk_name: str = ""
    new_risk_description: str = ""
    new_risk_category: str = "Operational"
    new_risk_inherent: float = 5.0
    new_risk_residual: float = 3.0
    new_risk_owner: str = ""
    show_risk_form: bool = False
    ai_suggestions: List[Dict] = []
    show_ai_suggestions: bool = False
    loading_ai: bool = False
    
    def toggle_risk_form(self):
        self.show_risk_form = not self.show_risk_form
    
    async def get_ai_risk_suggestions(self):
        """Get AI-powered risk suggestions from Gemini"""
        self.loading_ai = True
        yield
        
        suggestions = await ai_service.get_risk_suggestions("General")
        self.ai_suggestions = suggestions
        self.show_ai_suggestions = True
        self.loading_ai = False
        
        yield rx.toast.success("AI suggestions generated")
    
    def use_ai_suggestion(self, suggestion: Dict):
        """Use an AI-suggested risk"""
        self.new_risk_name = suggestion.get("name", "")
        self.new_risk_description = suggestion.get("description", "")
        self.new_risk_category = suggestion.get("category", "Operational")
        self.new_risk_inherent = float(suggestion.get("inherent_score", 5.0))
        self.new_risk_residual = float(suggestion.get("inherent_score", 5.0)) * 0.6
        self.show_ai_suggestions = False
        self.show_risk_form = True
    
    async def create_risk(self):
        """Create new risk"""
        if not self.new_risk_name:
            yield rx.toast.error("Please fill required fields")
            return
        
        risk = {
            "id": str(uuid.uuid4()),
            "name": self.new_risk_name,
            "description": self.new_risk_description,
            "category": self.new_risk_category,
            "inherent_risk_score": self.new_risk_inherent,
            "residual_risk_score": self.new_risk_residual,
            "status": "Active",
            "owner": self.new_risk_owner,
            "kri_ids": [],
            "linked_control_ids": [],
            "created_at": datetime.utcnow().isoformat()
        }
        
        await db_service.create_risk(risk)
        
        # Reset form
        self.new_risk_name = ""
        self.new_risk_description = ""
        self.new_risk_owner = ""
        self.show_risk_form = False
        
        await self.load_all_data()
        yield rx.toast.success("Risk created successfully")
