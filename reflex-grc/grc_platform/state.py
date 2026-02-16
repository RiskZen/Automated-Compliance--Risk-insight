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
    
    def create_risk(self):
        """Create new risk"""
        if not self.new_risk_name:
            return rx.toast.error("Please fill required fields")
        
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
        
        db_service.create_risk(risk)
        
        # Reset form
        self.new_risk_name = ""
        self.new_risk_description = ""
        self.new_risk_owner = ""
        self.show_risk_form = False
        
        self.load_all_data()
        return rx.toast.success("Risk created successfully")



class TestingState(GRCState):
    """State for control testing management"""
    
    new_test_control_id: str = ""
    new_test_date: str = ""
    new_test_tester: str = ""
    new_test_result: str = "Pass"
    new_test_evidence: str = ""
    new_test_notes: str = ""
    show_test_form: bool = False
    
    def set_new_test_control_id(self, value: str):
        self.new_test_control_id = value
    
    def set_new_test_date(self, value: str):
        self.new_test_date = value
    
    def set_new_test_tester(self, value: str):
        self.new_test_tester = value
    
    def set_new_test_result(self, value: str):
        self.new_test_result = value
    
    def set_new_test_evidence(self, value: str):
        self.new_test_evidence = value
    
    def set_new_test_notes(self, value: str):
        self.new_test_notes = value
    
    def toggle_test_form(self):
        self.show_test_form = not self.show_test_form
    
    def create_control_test(self):
        """Create new control test"""
        if not self.new_test_control_id or not self.new_test_tester:
            return rx.toast.error("Please fill required fields")
        
        # Find control ccf_id
        control = next((c for c in self.unified_controls if c["id"] == self.new_test_control_id), None)
        ccf_id = control.get("ccf_id", "") if control else ""
        
        test = {
            "id": str(uuid.uuid4()),
            "control_id": self.new_test_control_id,
            "control_ccf_id": ccf_id,
            "test_date": self.new_test_date or datetime.utcnow().strftime("%Y-%m-%d"),
            "tester": self.new_test_tester,
            "result": self.new_test_result,
            "evidence": self.new_test_evidence,
            "notes": self.new_test_notes,
            "created_at": datetime.utcnow().isoformat()
        }
        
        db_service.create_control_test(test)
        
        # Reset form
        self.new_test_control_id = ""
        self.new_test_date = ""
        self.new_test_tester = ""
        self.new_test_result = "Pass"
        self.new_test_evidence = ""
        self.new_test_notes = ""
        self.show_test_form = False
        
        self.load_all_data()
        return rx.toast.success("Control test recorded successfully")


class IssueState(GRCState):
    """State for issue management"""
    
    new_issue_title: str = ""
    new_issue_description: str = ""
    new_issue_severity: str = "Medium"
    new_issue_control_id: str = ""
    new_issue_assigned_to: str = ""
    new_issue_due_date: str = ""
    show_issue_form: bool = False
    
    def set_new_issue_title(self, value: str):
        self.new_issue_title = value
    
    def set_new_issue_description(self, value: str):
        self.new_issue_description = value
    
    def set_new_issue_severity(self, value: str):
        self.new_issue_severity = value
    
    def set_new_issue_control_id(self, value: str):
        self.new_issue_control_id = value
    
    def set_new_issue_assigned_to(self, value: str):
        self.new_issue_assigned_to = value
    
    def set_new_issue_due_date(self, value: str):
        self.new_issue_due_date = value
    
    def toggle_issue_form(self):
        self.show_issue_form = not self.show_issue_form
    
    def create_issue(self):
        """Create new issue"""
        if not self.new_issue_title:
            return rx.toast.error("Please fill required fields")
        
        issue = {
            "id": str(uuid.uuid4()),
            "title": self.new_issue_title,
            "description": self.new_issue_description,
            "severity": self.new_issue_severity,
            "status": "Open",
            "control_id": self.new_issue_control_id,
            "assigned_to": self.new_issue_assigned_to,
            "due_date": self.new_issue_due_date,
            "created_at": datetime.utcnow().isoformat()
        }
        
        db_service.create_issue(issue)
        
        # Reset form
        self.new_issue_title = ""
        self.new_issue_description = ""
        self.new_issue_severity = "Medium"
        self.new_issue_control_id = ""
        self.new_issue_assigned_to = ""
        self.new_issue_due_date = ""
        self.show_issue_form = False
        
        self.load_all_data()
        return rx.toast.success("Issue created successfully")
    
    def update_issue_status(self, issue_id: str, new_status: str):
        """Update issue status"""
        db_service.update_issue_status(issue_id, new_status)
        self.load_all_data()
        return rx.toast.success(f"Issue marked as {new_status}")


class KRIState(GRCState):
    """State for KRI management"""
    
    new_kri_name: str = ""
    new_kri_description: str = ""
    new_kri_risk_id: str = ""
    new_kri_threshold_green: int = 0
    new_kri_threshold_yellow: int = 5
    new_kri_threshold_red: int = 10
    new_kri_current_value: int = 0
    new_kri_unit: str = "Count"
    new_kri_frequency: str = "Monthly"
    new_kri_owner: str = ""
    show_kri_form: bool = False
    
    def set_new_kri_name(self, value: str):
        self.new_kri_name = value
    
    def set_new_kri_description(self, value: str):
        self.new_kri_description = value
    
    def set_new_kri_risk_id(self, value: str):
        self.new_kri_risk_id = value
    
    def set_new_kri_threshold_green(self, value: str):
        self.new_kri_threshold_green = int(value) if value else 0
    
    def set_new_kri_threshold_yellow(self, value: str):
        self.new_kri_threshold_yellow = int(value) if value else 5
    
    def set_new_kri_threshold_red(self, value: str):
        self.new_kri_threshold_red = int(value) if value else 10
    
    def set_new_kri_current_value(self, value: str):
        self.new_kri_current_value = int(value) if value else 0
    
    def set_new_kri_unit(self, value: str):
        self.new_kri_unit = value
    
    def set_new_kri_frequency(self, value: str):
        self.new_kri_frequency = value
    
    def set_new_kri_owner(self, value: str):
        self.new_kri_owner = value
    
    def toggle_kri_form(self):
        self.show_kri_form = not self.show_kri_form
    
    def create_kri(self):
        """Create new KRI"""
        if not self.new_kri_name or not self.new_kri_risk_id:
            return rx.toast.error("Please fill required fields")
        
        kri = {
            "id": str(uuid.uuid4()),
            "name": self.new_kri_name,
            "description": self.new_kri_description,
            "risk_id": self.new_kri_risk_id,
            "threshold_green": self.new_kri_threshold_green,
            "threshold_yellow": self.new_kri_threshold_yellow,
            "threshold_red": self.new_kri_threshold_red,
            "current_value": self.new_kri_current_value,
            "unit": self.new_kri_unit,
            "frequency": self.new_kri_frequency,
            "owner": self.new_kri_owner,
            "kci_ids": [],
            "created_at": datetime.utcnow().isoformat()
        }
        
        db_service.create_kri(kri)
        
        # Reset form
        self.new_kri_name = ""
        self.new_kri_description = ""
        self.new_kri_risk_id = ""
        self.new_kri_threshold_green = 0
        self.new_kri_threshold_yellow = 5
        self.new_kri_threshold_red = 10
        self.new_kri_current_value = 0
        self.new_kri_owner = ""
        self.show_kri_form = False
        
        self.load_all_data()
        return rx.toast.success("KRI created successfully")


class KCIState(GRCState):
    """State for KCI management"""
    
    new_kci_name: str = ""
    new_kci_description: str = ""
    new_kci_kri_id: str = ""
    new_kci_control_id: str = ""
    new_kci_threshold_green: int = 95
    new_kci_threshold_yellow: int = 85
    new_kci_threshold_red: int = 75
    new_kci_current_value: int = 100
    new_kci_unit: str = "Percentage"
    new_kci_frequency: str = "Monthly"
    new_kci_owner: str = ""
    show_kci_form: bool = False
    
    def set_new_kci_name(self, value: str):
        self.new_kci_name = value
    
    def set_new_kci_description(self, value: str):
        self.new_kci_description = value
    
    def set_new_kci_kri_id(self, value: str):
        self.new_kci_kri_id = value
    
    def set_new_kci_control_id(self, value: str):
        self.new_kci_control_id = value
    
    def set_new_kci_threshold_green(self, value: str):
        self.new_kci_threshold_green = int(value) if value else 95
    
    def set_new_kci_threshold_yellow(self, value: str):
        self.new_kci_threshold_yellow = int(value) if value else 85
    
    def set_new_kci_threshold_red(self, value: str):
        self.new_kci_threshold_red = int(value) if value else 75
    
    def set_new_kci_current_value(self, value: str):
        self.new_kci_current_value = int(value) if value else 100
    
    def set_new_kci_unit(self, value: str):
        self.new_kci_unit = value
    
    def set_new_kci_frequency(self, value: str):
        self.new_kci_frequency = value
    
    def set_new_kci_owner(self, value: str):
        self.new_kci_owner = value
    
    def toggle_kci_form(self):
        self.show_kci_form = not self.show_kci_form
    
    def create_kci(self):
        """Create new KCI"""
        if not self.new_kci_name or not self.new_kci_kri_id:
            return rx.toast.error("Please fill required fields")
        
        kci = {
            "id": str(uuid.uuid4()),
            "name": self.new_kci_name,
            "description": self.new_kci_description,
            "kri_id": self.new_kci_kri_id,
            "control_id": self.new_kci_control_id,
            "threshold_green": self.new_kci_threshold_green,
            "threshold_yellow": self.new_kci_threshold_yellow,
            "threshold_red": self.new_kci_threshold_red,
            "current_value": self.new_kci_current_value,
            "unit": self.new_kci_unit,
            "frequency": self.new_kci_frequency,
            "owner": self.new_kci_owner,
            "created_at": datetime.utcnow().isoformat()
        }
        
        db_service.create_kci(kci)
        
        # Reset form
        self.new_kci_name = ""
        self.new_kci_description = ""
        self.new_kci_kri_id = ""
        self.new_kci_control_id = ""
        self.new_kci_threshold_green = 95
        self.new_kci_threshold_yellow = 85
        self.new_kci_threshold_red = 75
        self.new_kci_current_value = 100
        self.new_kci_owner = ""
        self.show_kci_form = False
        
        self.load_all_data()
        return rx.toast.success("KCI created successfully")


class HeatmapState(GRCState):
    """State for risk heatmap visualization"""
    
    # Computed properties for heatmap data
    def get_risk_matrix_data(self) -> list[dict[str, Any]]:
        """Get risk data formatted for matrix heatmap"""
        matrix_data = []
        for risk in self.risks:
            impact = min(int(risk.get("inherent_risk_score", 5)), 10)
            likelihood = min(int(risk.get("residual_risk_score", 5) / risk.get("inherent_risk_score", 5) * 10) if risk.get("inherent_risk_score", 0) > 0 else 5, 10)
            matrix_data.append({
                "name": risk.get("name", ""),
                "impact": impact,
                "likelihood": likelihood,
                "score": risk.get("residual_risk_score", 0),
                "category": risk.get("category", "")
            })
        return matrix_data
