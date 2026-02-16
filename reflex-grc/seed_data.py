"""Seed script to populate GRC database with sample data including mappings"""
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime
import uuid

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "grc_reflex_db")

def seed_database():
    """Seed the database with comprehensive GRC data"""
    client = MongoClient(MONGO_URL)
    db = client[DB_NAME]
    
    print("🗑️  Clearing existing data...")
    db.frameworks.delete_many({})
    db.unified_controls.delete_many({})
    db.policies.delete_many({})
    db.control_tests.delete_many({})
    db.issues.delete_many({})
    db.risks.delete_many({})
    db.kris.delete_many({})
    db.kcis.delete_many({})
    
    # ========== FRAMEWORKS ==========
    print("📦 Seeding Frameworks...")
    frameworks = [
        {
            "id": "fw-iso27001",
            "name": "ISO 27001:2022",
            "description": "International standard for information security management systems (ISMS)",
            "version": "2022",
            "enabled": True,
            "total_controls": 93,
            "controls": [
                {"id": "A.5.1", "name": "Policies for information security", "description": "Management direction for information security"},
                {"id": "A.5.2", "name": "Information security roles", "description": "Segregation of duties"},
                {"id": "A.8.1", "name": "User endpoint devices", "description": "Protection of endpoint devices"},
                {"id": "A.8.2", "name": "Privileged access rights", "description": "Restriction of privileged access"},
                {"id": "A.8.3", "name": "Information access restriction", "description": "Access to information restricted"},
            ]
        },
        {
            "id": "fw-pcidss",
            "name": "PCI-DSS v4.0",
            "description": "Payment Card Industry Data Security Standard for protecting cardholder data",
            "version": "4.0",
            "enabled": True,
            "total_controls": 78,
            "controls": [
                {"id": "1.1.1", "name": "Network security controls", "description": "Firewalls and network segmentation"},
                {"id": "3.4.1", "name": "PAN is rendered unreadable", "description": "Encryption of cardholder data"},
                {"id": "7.2.1", "name": "Access control system", "description": "Restrict access based on need to know"},
                {"id": "8.3.1", "name": "Strong authentication", "description": "Multi-factor authentication"},
                {"id": "10.2.1", "name": "Audit logs enabled", "description": "Logging of access to cardholder data"},
            ]
        },
        {
            "id": "fw-soc2",
            "name": "SOC 2 Type II",
            "description": "Service Organization Control 2 - Trust Services Criteria",
            "version": "2017",
            "enabled": True,
            "total_controls": 64,
            "controls": [
                {"id": "CC6.1", "name": "Logical access security", "description": "Logical access security software"},
                {"id": "CC6.2", "name": "New user registration", "description": "Prior to issuing system credentials"},
                {"id": "CC6.3", "name": "Access removal", "description": "Removes access when no longer required"},
                {"id": "CC7.1", "name": "Monitoring activities", "description": "Detect and monitor security events"},
                {"id": "CC7.2", "name": "Anomaly detection", "description": "Monitor for anomalies and indicators"},
            ]
        },
        {
            "id": "fw-nist",
            "name": "NIST CSF 2.0",
            "description": "NIST Cybersecurity Framework for managing cybersecurity risk",
            "version": "2.0",
            "enabled": False,
            "total_controls": 108,
            "controls": [
                {"id": "ID.AM-1", "name": "Asset inventory", "description": "Physical devices and systems inventoried"},
                {"id": "PR.AC-1", "name": "Identity management", "description": "Identities and credentials issued"},
                {"id": "DE.CM-1", "name": "Network monitoring", "description": "Network monitored to detect events"},
            ]
        },
        {
            "id": "fw-gdpr",
            "name": "GDPR",
            "description": "General Data Protection Regulation for EU data privacy",
            "version": "2018",
            "enabled": False,
            "total_controls": 45,
            "controls": [
                {"id": "Art.25", "name": "Data protection by design", "description": "Privacy by design and default"},
                {"id": "Art.32", "name": "Security of processing", "description": "Appropriate technical measures"},
                {"id": "Art.33", "name": "Breach notification", "description": "Notify supervisory authority"},
            ]
        }
    ]
    db.frameworks.insert_many(frameworks)
    
    # ========== POLICIES ==========
    print("📜 Seeding Policies...")
    policies = [
        {
            "id": "pol-001",
            "policy_id": "POL-SEC-100",
            "name": "Information Security Policy",
            "description": "Establishes the security management framework and responsibilities",
            "category": "Security",
            "owner": "CISO",
            "status": "Active",
            "version": "3.0",
            "last_review": "2024-01-15",
            "next_review": "2025-01-15",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "pol-002",
            "policy_id": "POL-ACC-200",
            "name": "Access Control Policy",
            "description": "Defines rules for granting, reviewing, and revoking access to systems",
            "category": "Access Control",
            "owner": "IT Director",
            "status": "Active",
            "version": "2.5",
            "last_review": "2024-02-20",
            "next_review": "2025-02-20",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "pol-003",
            "policy_id": "POL-DAT-300",
            "name": "Data Protection Policy",
            "description": "Guidelines for handling, storing, and transmitting sensitive data",
            "category": "Data Protection",
            "owner": "DPO",
            "status": "Active",
            "version": "4.0",
            "last_review": "2024-03-10",
            "next_review": "2025-03-10",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "pol-004",
            "policy_id": "POL-INC-400",
            "name": "Incident Response Policy",
            "description": "Procedures for detecting, reporting, and responding to security incidents",
            "category": "Security",
            "owner": "Security Operations",
            "status": "Active",
            "version": "2.0",
            "last_review": "2024-01-05",
            "next_review": "2025-01-05",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "pol-005",
            "policy_id": "POL-VEN-500",
            "name": "Vendor Management Policy",
            "description": "Standards for evaluating and managing third-party vendors",
            "category": "Vendor Management",
            "owner": "Procurement",
            "status": "Active",
            "version": "1.5",
            "last_review": "2024-04-01",
            "next_review": "2025-04-01",
            "created_at": datetime.utcnow().isoformat()
        }
    ]
    db.policies.insert_many(policies)
    
    # ========== UNIFIED CONTROLS (CCF) with MAPPINGS ==========
    print("🎯 Seeding Unified Controls with Mappings...")
    unified_controls = [
        {
            "id": "ctrl-001",
            "ccf_id": "CCF-AC-001",
            "name": "Access Control Management",
            "description": "Ensure access to systems is properly managed, reviewed, and revoked when necessary",
            "control_type": "Preventive",
            "frequency": "Continuous",
            "owner": "IT Security",
            "automation_possible": True,
            "mapped_framework_controls": [
                {"framework": "ISO 27001:2022", "control_id": "A.8.2", "control_name": "Privileged access rights"},
                {"framework": "ISO 27001:2022", "control_id": "A.8.3", "control_name": "Information access restriction"},
                {"framework": "PCI-DSS v4.0", "control_id": "7.2.1", "control_name": "Access control system"},
                {"framework": "SOC 2", "control_id": "CC6.1", "control_name": "Logical access security"},
                {"framework": "SOC 2", "control_id": "CC6.3", "control_name": "Access removal"}
            ],
            "mapped_policies": [
                {"policy_id": "POL-ACC-200", "policy_name": "Access Control Policy"},
                {"policy_id": "POL-SEC-100", "policy_name": "Information Security Policy"}
            ],
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "ctrl-002",
            "ccf_id": "CCF-AU-002",
            "name": "Authentication & MFA",
            "description": "Implement strong authentication including multi-factor authentication for sensitive systems",
            "control_type": "Preventive",
            "frequency": "Continuous",
            "owner": "IT Security",
            "automation_possible": True,
            "mapped_framework_controls": [
                {"framework": "PCI-DSS v4.0", "control_id": "8.3.1", "control_name": "Strong authentication"},
                {"framework": "SOC 2", "control_id": "CC6.2", "control_name": "New user registration"},
                {"framework": "ISO 27001:2022", "control_id": "A.8.2", "control_name": "Privileged access rights"}
            ],
            "mapped_policies": [
                {"policy_id": "POL-ACC-200", "policy_name": "Access Control Policy"}
            ],
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "ctrl-003",
            "ccf_id": "CCF-EN-003",
            "name": "Data Encryption",
            "description": "Encrypt sensitive data at rest and in transit using industry-standard algorithms",
            "control_type": "Preventive",
            "frequency": "Continuous",
            "owner": "IT Security",
            "automation_possible": True,
            "mapped_framework_controls": [
                {"framework": "PCI-DSS v4.0", "control_id": "3.4.1", "control_name": "PAN is rendered unreadable"},
                {"framework": "ISO 27001:2022", "control_id": "A.8.1", "control_name": "User endpoint devices"}
            ],
            "mapped_policies": [
                {"policy_id": "POL-DAT-300", "policy_name": "Data Protection Policy"}
            ],
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "ctrl-004",
            "ccf_id": "CCF-LG-004",
            "name": "Security Logging & Monitoring",
            "description": "Collect, analyze, and retain security logs for threat detection and forensics",
            "control_type": "Detective",
            "frequency": "Continuous",
            "owner": "Security Operations",
            "automation_possible": True,
            "mapped_framework_controls": [
                {"framework": "PCI-DSS v4.0", "control_id": "10.2.1", "control_name": "Audit logs enabled"},
                {"framework": "SOC 2", "control_id": "CC7.1", "control_name": "Monitoring activities"},
                {"framework": "SOC 2", "control_id": "CC7.2", "control_name": "Anomaly detection"}
            ],
            "mapped_policies": [
                {"policy_id": "POL-INC-400", "policy_name": "Incident Response Policy"},
                {"policy_id": "POL-SEC-100", "policy_name": "Information Security Policy"}
            ],
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "ctrl-005",
            "ccf_id": "CCF-NW-005",
            "name": "Network Security",
            "description": "Implement network segmentation, firewalls, and intrusion detection/prevention",
            "control_type": "Preventive",
            "frequency": "Continuous",
            "owner": "Network Operations",
            "automation_possible": True,
            "mapped_framework_controls": [
                {"framework": "PCI-DSS v4.0", "control_id": "1.1.1", "control_name": "Network security controls"},
                {"framework": "ISO 27001:2022", "control_id": "A.8.1", "control_name": "User endpoint devices"}
            ],
            "mapped_policies": [
                {"policy_id": "POL-SEC-100", "policy_name": "Information Security Policy"}
            ],
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "ctrl-006",
            "ccf_id": "CCF-IS-006",
            "name": "Information Security Governance",
            "description": "Establish security policies, roles, and management oversight for the security program",
            "control_type": "Preventive",
            "frequency": "Annual",
            "owner": "CISO",
            "automation_possible": False,
            "mapped_framework_controls": [
                {"framework": "ISO 27001:2022", "control_id": "A.5.1", "control_name": "Policies for information security"},
                {"framework": "ISO 27001:2022", "control_id": "A.5.2", "control_name": "Information security roles"}
            ],
            "mapped_policies": [
                {"policy_id": "POL-SEC-100", "policy_name": "Information Security Policy"},
                {"policy_id": "POL-ACC-200", "policy_name": "Access Control Policy"},
                {"policy_id": "POL-DAT-300", "policy_name": "Data Protection Policy"},
                {"policy_id": "POL-INC-400", "policy_name": "Incident Response Policy"},
                {"policy_id": "POL-VEN-500", "policy_name": "Vendor Management Policy"}
            ],
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "ctrl-007",
            "ccf_id": "CCF-VM-007",
            "name": "Vendor Risk Assessment",
            "description": "Assess and monitor security risks from third-party vendors and service providers",
            "control_type": "Preventive",
            "frequency": "Quarterly",
            "owner": "Vendor Management",
            "automation_possible": False,
            "mapped_framework_controls": [],
            "mapped_policies": [
                {"policy_id": "POL-VEN-500", "policy_name": "Vendor Management Policy"}
            ],
            "created_at": datetime.utcnow().isoformat()
        }
    ]
    db.unified_controls.insert_many(unified_controls)
    
    # ========== CONTROL TESTS ==========
    print("✅ Seeding Control Tests...")
    control_tests = [
        {
            "id": str(uuid.uuid4()),
            "control_id": "ctrl-001",
            "control_ccf_id": "CCF-AC-001",
            "test_date": "2024-11-15",
            "tester": "John Smith",
            "result": "Pass",
            "evidence": "access_review_nov2024.xlsx",
            "notes": "All access reviews completed on schedule. No unauthorized access found.",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "control_id": "ctrl-002",
            "control_ccf_id": "CCF-AU-002",
            "test_date": "2024-11-10",
            "tester": "Sarah Johnson",
            "result": "Pass",
            "evidence": "mfa_audit_report.pdf",
            "notes": "MFA enabled for 100% of admin accounts. Regular user adoption at 95%.",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "control_id": "ctrl-003",
            "control_ccf_id": "CCF-EN-003",
            "test_date": "2024-11-12",
            "tester": "Mike Chen",
            "result": "Pass",
            "evidence": "encryption_scan_results.csv",
            "notes": "AES-256 encryption verified for all databases and storage.",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "control_id": "ctrl-004",
            "control_ccf_id": "CCF-LG-004",
            "test_date": "2024-11-14",
            "tester": "Emily Davis",
            "result": "Fail",
            "evidence": "logging_gap_analysis.docx",
            "notes": "ISSUE: Some legacy systems not sending logs to SIEM. Remediation in progress.",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "control_id": "ctrl-005",
            "control_ccf_id": "CCF-NW-005",
            "test_date": "2024-11-08",
            "tester": "David Wilson",
            "result": "Pass",
            "evidence": "network_pen_test_2024.pdf",
            "notes": "Penetration test completed. All critical vulnerabilities remediated.",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "control_id": "ctrl-006",
            "control_ccf_id": "CCF-IS-006",
            "test_date": "2024-10-20",
            "tester": "Lisa Brown",
            "result": "Pass",
            "evidence": "policy_review_minutes.pdf",
            "notes": "Annual policy review completed. All policies current and approved by board.",
            "created_at": datetime.utcnow().isoformat()
        }
    ]
    db.control_tests.insert_many(control_tests)
    
    # ========== ISSUES ==========
    print("⚠️  Seeding Issues...")
    issues = [
        {
            "id": str(uuid.uuid4()),
            "title": "Legacy systems not integrated with SIEM",
            "description": "Several legacy applications are not sending security logs to the central SIEM platform",
            "severity": "High",
            "status": "Open",
            "control_id": "ctrl-004",
            "assigned_to": "IT Infrastructure Team",
            "due_date": "2024-12-31",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "title": "MFA adoption below target for regular users",
            "description": "MFA adoption for regular users is at 95%, below the 100% target",
            "severity": "Medium",
            "status": "In Progress",
            "control_id": "ctrl-002",
            "assigned_to": "IT Security",
            "due_date": "2025-01-15",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "title": "Vendor security assessment backlog",
            "description": "15 vendors pending security assessment due to resource constraints",
            "severity": "Medium",
            "status": "Open",
            "control_id": "ctrl-007",
            "assigned_to": "Vendor Management",
            "due_date": "2025-02-28",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "title": "Outdated firewall rules",
            "description": "Network firewall rules audit revealed 50+ outdated rules that need cleanup",
            "severity": "Low",
            "status": "Resolved",
            "control_id": "ctrl-005",
            "assigned_to": "Network Operations",
            "due_date": "2024-11-01",
            "resolution_date": "2024-10-28",
            "resolution_notes": "All outdated rules removed and documented",
            "created_at": datetime.utcnow().isoformat()
        }
    ]
    db.issues.insert_many(issues)
    
    # ========== RISKS ==========
    print("📊 Seeding Risks...")
    risks = [
        {
            "id": "risk-001",
            "name": "Data Breach from External Attack",
            "description": "Unauthorized access to sensitive customer data through cyber attack",
            "category": "Cybersecurity",
            "inherent_risk_score": 9.0,
            "residual_risk_score": 4.5,
            "status": "Active",
            "owner": "CISO",
            "treatment": "Mitigate",
            "kri_ids": ["kri-001", "kri-002"],
            "linked_control_ids": ["ctrl-001", "ctrl-002", "ctrl-003", "ctrl-004", "ctrl-005"],
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "risk-002",
            "name": "Regulatory Non-Compliance",
            "description": "Failure to meet PCI-DSS or other regulatory requirements leading to fines",
            "category": "Compliance",
            "inherent_risk_score": 8.0,
            "residual_risk_score": 3.0,
            "status": "Active",
            "owner": "Compliance Officer",
            "treatment": "Mitigate",
            "kri_ids": ["kri-003"],
            "linked_control_ids": ["ctrl-001", "ctrl-003", "ctrl-006"],
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "risk-003",
            "name": "Third-Party Vendor Security Breach",
            "description": "Security incident at a vendor causing exposure of company data",
            "category": "Operational",
            "inherent_risk_score": 7.5,
            "residual_risk_score": 5.0,
            "status": "Active",
            "owner": "Vendor Management",
            "treatment": "Mitigate",
            "kri_ids": ["kri-004"],
            "linked_control_ids": ["ctrl-007"],
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "risk-004",
            "name": "Insider Threat",
            "description": "Malicious or negligent actions by employees causing data loss or system damage",
            "category": "Security",
            "inherent_risk_score": 7.0,
            "residual_risk_score": 4.0,
            "status": "Active",
            "owner": "HR & Security",
            "treatment": "Mitigate",
            "kri_ids": ["kri-005"],
            "linked_control_ids": ["ctrl-001", "ctrl-004"],
            "created_at": datetime.utcnow().isoformat()
        }
    ]
    db.risks.insert_many(risks)
    
    # ========== KRIs ==========
    print("📈 Seeding KRIs...")
    kris = [
        {
            "id": "kri-001",
            "name": "Number of Critical Vulnerabilities",
            "description": "Count of critical vulnerabilities in production systems",
            "risk_id": "risk-001",
            "threshold_green": 0,
            "threshold_yellow": 5,
            "threshold_red": 10,
            "current_value": 3,
            "unit": "Count",
            "frequency": "Weekly",
            "owner": "IT Security",
            "kci_ids": ["kci-001"],
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "kri-002",
            "name": "Security Incidents Per Month",
            "description": "Number of security incidents detected per month",
            "risk_id": "risk-001",
            "threshold_green": 5,
            "threshold_yellow": 15,
            "threshold_red": 30,
            "current_value": 8,
            "unit": "Count",
            "frequency": "Monthly",
            "owner": "Security Operations",
            "kci_ids": ["kci-002"],
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "kri-003",
            "name": "Compliance Score",
            "description": "Overall compliance posture score across all frameworks",
            "risk_id": "risk-002",
            "threshold_green": 95,
            "threshold_yellow": 85,
            "threshold_red": 75,
            "current_value": 92,
            "unit": "Percentage",
            "frequency": "Monthly",
            "owner": "Compliance",
            "kci_ids": ["kci-003"],
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "kri-004",
            "name": "Vendor Assessment Completion Rate",
            "description": "Percentage of vendors with current security assessments",
            "risk_id": "risk-003",
            "threshold_green": 100,
            "threshold_yellow": 85,
            "threshold_red": 70,
            "current_value": 78,
            "unit": "Percentage",
            "frequency": "Quarterly",
            "owner": "Vendor Management",
            "kci_ids": ["kci-004"],
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "kri-005",
            "name": "Privileged Access Violations",
            "description": "Number of unauthorized privileged access attempts",
            "risk_id": "risk-004",
            "threshold_green": 0,
            "threshold_yellow": 3,
            "threshold_red": 10,
            "current_value": 1,
            "unit": "Count",
            "frequency": "Weekly",
            "owner": "IT Security",
            "kci_ids": ["kci-005"],
            "created_at": datetime.utcnow().isoformat()
        }
    ]
    db.kris.insert_many(kris)
    
    # ========== KCIs ==========
    print("🎯 Seeding KCIs...")
    kcis = [
        {
            "id": "kci-001",
            "name": "Patch Compliance Rate",
            "description": "Percentage of systems with critical patches applied within SLA",
            "kri_id": "kri-001",
            "control_id": "ctrl-005",
            "threshold_green": 98,
            "threshold_yellow": 90,
            "threshold_red": 80,
            "current_value": 96,
            "unit": "Percentage",
            "frequency": "Weekly",
            "owner": "IT Operations",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "kci-002",
            "name": "Mean Time to Detect (MTTD)",
            "description": "Average time to detect security incidents",
            "kri_id": "kri-002",
            "control_id": "ctrl-004",
            "threshold_green": 60,
            "threshold_yellow": 120,
            "threshold_red": 240,
            "current_value": 45,
            "unit": "Minutes",
            "frequency": "Monthly",
            "owner": "Security Operations",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "kci-003",
            "name": "Control Test Pass Rate",
            "description": "Percentage of controls passing their tests",
            "kri_id": "kri-003",
            "control_id": "ctrl-006",
            "threshold_green": 95,
            "threshold_yellow": 85,
            "threshold_red": 75,
            "current_value": 83,
            "unit": "Percentage",
            "frequency": "Quarterly",
            "owner": "Internal Audit",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "kci-004",
            "name": "Vendor Due Diligence Completion",
            "description": "Percentage of new vendors completing security questionnaire",
            "kri_id": "kri-004",
            "control_id": "ctrl-007",
            "threshold_green": 100,
            "threshold_yellow": 90,
            "threshold_red": 75,
            "current_value": 100,
            "unit": "Percentage",
            "frequency": "Monthly",
            "owner": "Vendor Management",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "kci-005",
            "name": "Access Review Completion",
            "description": "Percentage of access reviews completed on time",
            "kri_id": "kri-005",
            "control_id": "ctrl-001",
            "threshold_green": 100,
            "threshold_yellow": 95,
            "threshold_red": 85,
            "current_value": 100,
            "unit": "Percentage",
            "frequency": "Quarterly",
            "owner": "IT Security",
            "created_at": datetime.utcnow().isoformat()
        }
    ]
    db.kcis.insert_many(kcis)
    
    print("\n✨ Database seeding complete!")
    print("=" * 50)
    print(f"📦 Frameworks: {len(frameworks)}")
    print(f"📜 Policies: {len(policies)}")
    print(f"🎯 Unified Controls: {len(unified_controls)}")
    print(f"✅ Control Tests: {len(control_tests)}")
    print(f"⚠️  Issues: {len(issues)}")
    print(f"📊 Risks: {len(risks)}")
    print(f"📈 KRIs: {len(kris)}")
    print(f"🎯 KCIs: {len(kcis)}")
    print("=" * 50)
    
    client.close()

if __name__ == "__main__":
    seed_database()
