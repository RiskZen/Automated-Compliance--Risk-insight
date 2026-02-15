"""Global state management for GRC Platform"""
import reflex as rx
from typing import List, Dict, Any
import uuid
from datetime import datetime
from .database import db_service
from .ai_service import ai_service


class GRCState(rx.State):
    """Global state for the entire GRC application"""
    
    # Data - using list[dict[str, Any]] for proper typing
    frameworks: list[dict[str, Any]] = []
    unified_controls: list[dict[str, Any]] = []
    policies: list[dict[str, Any]] = []
    control_tests: list[dict[str, Any]] = []
    issues: list[dict[str, Any]] = []
    risks: list[dict[str, Any]] = []
    kris: list[dict[str, Any]] = []
    kcis: list[dict[str, Any]] = []
    
    # UI State
    loading: bool = False
    current_page: str = "dashboard"
    
    # Dashboard stats
    enabled_frameworks: int = 0
    total_unified_controls: int = 0
    control_effectiveness: float = 0
    total_tests: int = 0
    passed_tests: int = 0
    open_issues: int = 0
    total_issues: int = 0
    total_risks: int = 0
    avg_residual_risk: float = 0
    
    def load_all_data(self):
        """Load all data from database"""
        self.loading = True
        
        try:
            self.frameworks = db_service.get_frameworks()
            self.unified_controls = db_service.get_unified_controls()
            self.policies = db_service.get_policies()
            self.control_tests = db_service.get_control_tests()
            self.issues = db_service.get_issues()
            self.risks = db_service.get_risks()
            self.kris = db_service.get_kris()
            self.kcis = db_service.get_kcis()
            
            # Calculate stats
            stats = db_service.get_dashboard_stats()
            self.enabled_frameworks = stats.get("enabled_frameworks", 0)
            self.total_unified_controls = stats.get("total_unified_controls", 0)
            self.control_effectiveness = stats.get("control_effectiveness", 0)
            self.total_tests = stats.get("total_tests", 0)
            self.passed_tests = stats.get("passed_tests", 0)
            self.open_issues = stats.get("open_issues", 0)
            self.total_issues = stats.get("total_issues", 0)
            self.total_risks = stats.get("total_risks", 0)
            self.avg_residual_risk = stats.get("avg_residual_risk", 0)
            
            print(f"[DEBUG] Loaded {len(self.frameworks)} frameworks, {len(self.unified_controls)} controls")
        except Exception as e:
            print(f"[ERROR] Failed to load data: {e}")
            import traceback
            traceback.print_exc()
        
        self.loading = False
    
    def set_page(self, page: str):
        """Change current page"""
        self.current_page = page


class FrameworkState(GRCState):
    """State for framework management"""
    
    def toggle_framework(self, framework_id: str):
        """Enable/disable a framework"""
        framework = next((f for f in self.frameworks if f["id"] == framework_id), None)
        if framework:
            new_status = not framework.get("enabled", False)
            db_service.toggle_framework(framework_id, new_status)
            self.load_all_data()
            return rx.toast.success(f"Framework {'enabled' if new_status else 'disabled'}")


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
    
    # Expanded control IDs for viewing mapping details
    expanded_controls: list[str] = []
    
    # Selected control for mapping details view
    selected_control_id: str = ""
    selected_control_mappings: dict[str, Any] = {}
    
    # Setters for form fields
    def set_new_control_ccf_id(self, value: str):
        self.new_control_ccf_id = value
    
    def set_new_control_name(self, value: str):
        self.new_control_name = value
    
    def set_new_control_description(self, value: str):
        self.new_control_description = value
    
    def set_new_control_type(self, value: str):
        self.new_control_type = value
    
    def set_new_control_owner(self, value: str):
        self.new_control_owner = value
    
    def toggle_create_form(self):
        self.show_create_form = not self.show_create_form
    
    def toggle_control_details(self, control_id: str):
        """Toggle expand/collapse for a control's mapping details"""
        if control_id in self.expanded_controls:
            self.expanded_controls = [c for c in self.expanded_controls if c != control_id]
            if self.selected_control_id == control_id:
                self.selected_control_id = ""
                self.selected_control_mappings = {}
        else:
            self.expanded_controls = self.expanded_controls + [control_id]
            self.selected_control_id = control_id
            # Find control and set mapping data
            for ctrl in self.unified_controls:
                if ctrl.get("id") == control_id:
                    self.selected_control_mappings = {
                        "ccf_id": ctrl.get("ccf_id", ""),
                        "name": ctrl.get("name", ""),
                        "control_type": ctrl.get("control_type", ""),
                        "framework_controls_count": len(ctrl.get("mapped_framework_controls", [])),
                        "policies_count": len(ctrl.get("mapped_policies", [])),
                        "framework_controls_text": self._format_framework_controls(ctrl.get("mapped_framework_controls", [])),
                        "policies_text": self._format_policies(ctrl.get("mapped_policies", [])),
                        "automation_possible": ctrl.get("automation_possible", False)
                    }
                    break
    
    def _format_framework_controls(self, controls: list) -> str:
        """Format framework controls for display"""
        if not controls:
            return "No framework controls mapped"
        lines = []
        for fc in controls:
            lines.append(f"• {fc.get('framework', '')} - {fc.get('control_id', '')}: {fc.get('control_name', '')}")
        return "\n".join(lines)
    
    def _format_policies(self, policies: list) -> str:
        """Format policies for display"""
        if not policies:
            return "No policies mapped"
        lines = []
        for pol in policies:
            lines.append(f"• {pol.get('policy_id', '')}: {pol.get('policy_name', '')}")
        return "\n".join(lines)
    
    def is_control_expanded(self, control_id: str) -> bool:
        """Check if a control is expanded"""
        return control_id in self.expanded_controls
    
    def create_control(self):
        """Create new unified control"""
        if not self.new_control_name or not self.new_control_ccf_id:
            return rx.toast.error("Please fill required fields")
        
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
        
        db_service.create_unified_control(control)
        
        # Reset form
        self.new_control_ccf_id = ""
        self.new_control_name = ""
        self.new_control_description = ""
        self.new_control_owner = ""
        self.show_create_form = False
        
        self.load_all_data()
        return rx.toast.success("Control created successfully")


class PolicyState(GRCState):
    """State for policy management"""
    
    new_policy_id: str = ""
    new_policy_name: str = ""
    new_policy_description: str = ""
    new_policy_category: str = "Security"
    new_policy_owner: str = ""
    show_policy_form: bool = False
    
    # Setters
    def set_new_policy_id(self, value: str):
        self.new_policy_id = value
    
    def set_new_policy_name(self, value: str):
        self.new_policy_name = value
    
    def set_new_policy_description(self, value: str):
        self.new_policy_description = value
    
    def set_new_policy_owner(self, value: str):
        self.new_policy_owner = value
    
    def toggle_policy_form(self):
        self.show_policy_form = not self.show_policy_form
    
    def create_policy(self):
        """Create new policy"""
        if not self.new_policy_name or not self.new_policy_id:
            return rx.toast.error("Please fill required fields")
        
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
        
        db_service.create_policy(policy)
        
        # Reset form
        self.new_policy_id = ""
        self.new_policy_name = ""
        self.new_policy_description = ""
        self.new_policy_owner = ""
        self.show_policy_form = False
        
        self.load_all_data()
        return rx.toast.success("Policy created successfully")


class RiskState(GRCState):
    """State for risk management"""
    
    new_risk_name: str = ""
    new_risk_description: str = ""
    new_risk_category: str = "Operational"
    new_risk_inherent: float = 5.0
    new_risk_residual: float = 3.0
    new_risk_owner: str = ""
    show_risk_form: bool = False
    ai_suggestions: list[dict[str, Any]] = []
    show_ai_suggestions: bool = False
    loading_ai: bool = False
    
    def toggle_risk_form(self):
        self.show_risk_form = not self.show_risk_form
    
    def get_ai_risk_suggestions(self):
        """Get AI-powered risk suggestions from Gemini"""
        self.loading_ai = True
        
        suggestions = ai_service.get_risk_suggestions("General")
        self.ai_suggestions = suggestions
        self.show_ai_suggestions = True
        self.loading_ai = False
        
        return rx.toast.success("AI suggestions generated")
    
    def use_ai_suggestion(self, suggestion: dict):
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
