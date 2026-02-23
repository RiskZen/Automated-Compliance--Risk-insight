"""Global state management for GRC Platform"""
import reflex as rx
from typing import List, Dict, Any
import uuid
from datetime import datetime
from .database import db_service


class AuthState(rx.State):
    """Authentication state"""
    
    is_authenticated: bool = False
    current_user: dict[str, Any] = {}
    login_email: str = ""
    login_password: str = ""
    login_error: str = ""
    
    def set_login_email(self, value: str):
        self.login_email = value
        self.login_error = ""
    
    def set_login_password(self, value: str):
        self.login_password = value
        self.login_error = ""
    
    def login(self):
        """Attempt to login"""
        if not self.login_email or not self.login_password:
            self.login_error = "Please enter email and password"
            return
        
        user = db_service.verify_user(self.login_email, self.login_password)
        if user:
            self.current_user = user
            self.is_authenticated = True
            self.login_error = ""
            self.login_email = ""
            self.login_password = ""
            db_service.log_audit(user["id"], user["email"], "LOGIN", "System", "User logged in")
            return rx.redirect("/")
        else:
            self.login_error = "Invalid email or password"
    
    def logout(self):
        """Logout user"""
        if self.current_user:
            db_service.log_audit(self.current_user.get("id", ""), self.current_user.get("email", ""), 
                               "LOGOUT", "System", "User logged out")
        self.is_authenticated = False
        self.current_user = {}
        return rx.redirect("/login")
    
    def check_auth(self):
        """Check if user is authenticated"""
        if not self.is_authenticated:
            return rx.redirect("/login")


class GRCState(AuthState):
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
    connectors: list[dict[str, Any]] = []
    ai_models: list[dict[str, Any]] = []
    ai_assessments: list[dict[str, Any]] = []
    audit_logs: list[dict[str, Any]] = []
    
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
    total_ai_models: int = 0
    production_ai_models: int = 0
    high_risk_ai_models: int = 0
    
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
            self.connectors = db_service.get_connectors()
            self.ai_models = db_service.get_ai_models()
            self.ai_assessments = db_service.get_ai_assessments()
            self.audit_logs = db_service.get_audit_logs(50)
            
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
            self.total_ai_models = stats.get("total_ai_models", 0)
            self.production_ai_models = stats.get("production_ai_models", 0)
            self.high_risk_ai_models = stats.get("high_risk_ai_models", 0)
            
            print(f"[DEBUG] Loaded {len(self.frameworks)} frameworks, {len(self.unified_controls)} controls, {len(self.ai_models)} AI models")
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
        """Toggle framework enabled status"""
        for fw in self.frameworks:
            if fw["id"] == framework_id:
                new_status = not fw["enabled"]
                db_service.toggle_framework(framework_id, new_status)
                break
        self.load_all_data()
        return rx.toast.success("Framework updated successfully")


class ControlState(GRCState):
    """State for control management"""
    
    selected_control_id: str = ""
    show_control_details: bool = False
    expanded_controls: list[str] = []
    
    def toggle_control_details(self, control_id: str):
        """Toggle control details expansion"""
        if control_id in self.expanded_controls:
            self.expanded_controls = [c for c in self.expanded_controls if c != control_id]
        else:
            self.expanded_controls = self.expanded_controls + [control_id]
    
    def is_control_expanded(self, control_id: str) -> bool:
        return control_id in self.expanded_controls


class PolicyState(GRCState):
    """State for policy management"""
    
    expanded_policies: list[str] = []
    
    def toggle_policy_details(self, policy_id: str):
        """Toggle policy details expansion"""
        if policy_id in self.expanded_policies:
            self.expanded_policies = [p for p in self.expanded_policies if p != policy_id]
        else:
            self.expanded_policies = self.expanded_policies + [policy_id]


class RiskState(GRCState):
    """State for risk management"""
    
    new_risk_name: str = ""
    new_risk_description: str = ""
    new_risk_category: str = "Security"
    new_risk_owner: str = ""
    show_risk_form: bool = False
    
    def set_new_risk_name(self, value: str):
        self.new_risk_name = value
    
    def set_new_risk_description(self, value: str):
        self.new_risk_description = value
    
    def set_new_risk_category(self, value: str):
        self.new_risk_category = value
    
    def set_new_risk_owner(self, value: str):
        self.new_risk_owner = value
    
    def toggle_risk_form(self):
        self.show_risk_form = not self.show_risk_form
    
    def create_risk(self):
        """Create new risk"""
        if not self.new_risk_name:
            return rx.toast.error("Please enter risk name")
        
        risk = {
            "id": str(uuid.uuid4()),
            "name": self.new_risk_name,
            "description": self.new_risk_description,
            "category": self.new_risk_category,
            "inherent_risk_score": 5,
            "residual_risk_score": 3,
            "status": "Active",
            "owner": self.new_risk_owner,
            "treatment": "Mitigate",
            "kri_ids": [],
            "linked_control_ids": [],
            "created_at": datetime.utcnow().isoformat()
        }
        
        db_service.create_risk(risk)
        
        # Reset form
        self.new_risk_name = ""
        self.new_risk_description = ""
        self.new_risk_category = "Security"
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
    new_test_type: str = "Manual"
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
    
    def set_new_test_type(self, value: str):
        self.new_test_type = value
    
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
            "test_type": self.new_test_type,
            "connector_id": None,
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
        self.new_test_type = "Manual"
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
    pass


class AIGovernanceState(GRCState):
    """State for AI Governance module"""
    
    # AI Model form
    new_model_name: str = ""
    new_model_type: str = "Classification"
    new_model_version: str = "1.0.0"
    new_model_status: str = "Development"
    new_model_risk_level: str = "Medium"
    new_model_owner: str = ""
    new_model_department: str = ""
    new_model_purpose: str = ""
    show_model_form: bool = False
    
    # Assessment form
    show_assessment_form: bool = False
    assessment_model_id: str = ""
    assessment_bias_risk: str = "Medium"
    assessment_privacy_risk: str = "Medium"
    assessment_security_risk: str = "Medium"
    assessment_transparency_risk: str = "Medium"
    assessment_findings: str = ""
    assessment_recommendations: str = ""
    
    def set_new_model_name(self, value: str):
        self.new_model_name = value
    
    def set_new_model_type(self, value: str):
        self.new_model_type = value
    
    def set_new_model_version(self, value: str):
        self.new_model_version = value
    
    def set_new_model_status(self, value: str):
        self.new_model_status = value
    
    def set_new_model_risk_level(self, value: str):
        self.new_model_risk_level = value
    
    def set_new_model_owner(self, value: str):
        self.new_model_owner = value
    
    def set_new_model_department(self, value: str):
        self.new_model_department = value
    
    def set_new_model_purpose(self, value: str):
        self.new_model_purpose = value
    
    def toggle_model_form(self):
        self.show_model_form = not self.show_model_form
    
    def create_ai_model(self):
        """Create new AI model"""
        if not self.new_model_name or not self.new_model_owner:
            return rx.toast.error("Please fill required fields")
        
        model = {
            "id": str(uuid.uuid4()),
            "name": self.new_model_name,
            "type": self.new_model_type,
            "version": self.new_model_version,
            "status": self.new_model_status,
            "risk_level": self.new_model_risk_level,
            "owner": self.new_model_owner,
            "department": self.new_model_department,
            "purpose": self.new_model_purpose,
            "data_sources": [],
            "training_data_size": "N/A",
            "last_trained": None,
            "accuracy": None,
            "fairness_score": None,
            "explainability_score": None,
            "has_human_oversight": True,
            "pii_involved": False,
            "automated_decisions": False,
            "created_at": datetime.utcnow().isoformat()
        }
        
        db_service.create_ai_model(model)
        
        # Reset form
        self.new_model_name = ""
        self.new_model_type = "Classification"
        self.new_model_version = "1.0.0"
        self.new_model_status = "Development"
        self.new_model_risk_level = "Medium"
        self.new_model_owner = ""
        self.new_model_department = ""
        self.new_model_purpose = ""
        self.show_model_form = False
        
        self.load_all_data()
        return rx.toast.success("AI Model registered successfully")
    
    def set_assessment_model_id(self, value: str):
        self.assessment_model_id = value
    
    def set_assessment_bias_risk(self, value: str):
        self.assessment_bias_risk = value
    
    def set_assessment_privacy_risk(self, value: str):
        self.assessment_privacy_risk = value
    
    def set_assessment_security_risk(self, value: str):
        self.assessment_security_risk = value
    
    def set_assessment_transparency_risk(self, value: str):
        self.assessment_transparency_risk = value
    
    def set_assessment_findings(self, value: str):
        self.assessment_findings = value
    
    def set_assessment_recommendations(self, value: str):
        self.assessment_recommendations = value
    
    def toggle_assessment_form(self):
        self.show_assessment_form = not self.show_assessment_form
    
    def create_assessment(self):
        """Create new AI assessment"""
        if not self.assessment_model_id:
            return rx.toast.error("Please select a model")
        
        # Find model name
        model = next((m for m in self.ai_models if m["id"] == self.assessment_model_id), None)
        model_name = model.get("name", "") if model else ""
        
        # Calculate overall risk
        risk_scores = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}
        avg_score = (risk_scores.get(self.assessment_bias_risk, 2) + 
                    risk_scores.get(self.assessment_privacy_risk, 2) +
                    risk_scores.get(self.assessment_security_risk, 2) +
                    risk_scores.get(self.assessment_transparency_risk, 2)) / 4
        
        overall_risk = "Low" if avg_score <= 1.5 else "Medium" if avg_score <= 2.5 else "High" if avg_score <= 3.5 else "Critical"
        
        assessment = {
            "id": str(uuid.uuid4()),
            "model_id": self.assessment_model_id,
            "model_name": model_name,
            "assessment_date": datetime.utcnow().strftime("%Y-%m-%d"),
            "assessor": self.current_user.get("name", "Unknown"),
            "status": "Completed",
            "overall_risk": overall_risk,
            "bias_risk": self.assessment_bias_risk,
            "privacy_risk": self.assessment_privacy_risk,
            "security_risk": self.assessment_security_risk,
            "transparency_risk": self.assessment_transparency_risk,
            "findings": [f.strip() for f in self.assessment_findings.split("\n") if f.strip()],
            "recommendations": [r.strip() for r in self.assessment_recommendations.split("\n") if r.strip()],
            "next_review": "",
            "created_at": datetime.utcnow().isoformat()
        }
        
        db_service.create_ai_assessment(assessment)
        
        # Reset form
        self.assessment_model_id = ""
        self.assessment_bias_risk = "Medium"
        self.assessment_privacy_risk = "Medium"
        self.assessment_security_risk = "Medium"
        self.assessment_transparency_risk = "Medium"
        self.assessment_findings = ""
        self.assessment_recommendations = ""
        self.show_assessment_form = False
        
        self.load_all_data()
        return rx.toast.success("AI Assessment created successfully")


class AuditLogState(GRCState):
    """State for audit logs"""
    pass


class ConnectorState(GRCState):
    """State for connector management"""
    
    def toggle_connector(self, connector_id: str, current_status: str):
        """Toggle connector status"""
        new_status = "Disconnected" if current_status == "Connected" else "Connected"
        db_service.update_connector_status(connector_id, new_status)
        self.load_all_data()
        return rx.toast.success(f"Connector {'connected' if new_status == 'Connected' else 'disconnected'}")
