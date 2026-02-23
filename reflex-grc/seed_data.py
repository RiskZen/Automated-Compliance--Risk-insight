"""Seed script to populate GRC database with comprehensive data"""
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import uuid
import hashlib

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "grc_reflex_db")

def hash_password(password: str) -> str:
    """Simple password hashing"""
    return hashlib.sha256(password.encode()).hexdigest()

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
    db.users.delete_many({})
    db.ai_models.delete_many({})
    db.ai_assessments.delete_many({})
    db.audit_logs.delete_many({})
    db.connectors.delete_many({})
    
    # ========== USERS ==========
    print("👤 Seeding Users...")
    users = [
        {
            "id": "user-admin",
            "email": "admin@grcplatform.com",
            "password": hash_password("admin123"),
            "name": "Admin User",
            "role": "admin",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "user-auditor",
            "email": "auditor@grcplatform.com",
            "password": hash_password("auditor123"),
            "name": "John Auditor",
            "role": "auditor",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "user-analyst",
            "email": "analyst@grcplatform.com",
            "password": hash_password("analyst123"),
            "name": "Jane Analyst",
            "role": "analyst",
            "created_at": datetime.utcnow().isoformat()
        }
    ]
    db.users.insert_many(users)
    
    # ========== FRAMEWORKS ==========
    print("📦 Seeding Frameworks...")
    frameworks = [
        {
            "id": "fw-iso27001",
            "name": "ISO 27001:2022",
            "description": "International standard for information security management systems (ISMS)",
            "version": "2022",
            "category": "Security",
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
            "id": "fw-iso42001",
            "name": "ISO 42001:2023",
            "description": "Artificial Intelligence Management System (AIMS) - Standard for responsible AI governance",
            "version": "2023",
            "category": "AI Governance",
            "enabled": True,
            "total_controls": 39,
            "controls": [
                {"id": "AI.4.1", "name": "AI Policy", "description": "Establish AI policy aligned with organizational objectives"},
                {"id": "AI.5.1", "name": "AI Risk Assessment", "description": "Identify and assess AI-related risks"},
                {"id": "AI.6.1", "name": "AI System Lifecycle", "description": "Manage AI systems throughout their lifecycle"},
                {"id": "AI.7.1", "name": "Data for AI", "description": "Ensure quality and governance of AI training data"},
                {"id": "AI.8.1", "name": "AI Transparency", "description": "Maintain transparency in AI decision-making"},
                {"id": "AI.9.1", "name": "Human Oversight", "description": "Ensure appropriate human oversight of AI systems"},
            ]
        },
        {
            "id": "fw-pcidss",
            "name": "PCI-DSS v4.0",
            "description": "Payment Card Industry Data Security Standard for protecting cardholder data",
            "version": "4.0",
            "category": "Financial",
            "enabled": True,
            "total_controls": 64,
            "controls": [
                {"id": "1.1", "name": "Network Security Controls", "description": "Install and maintain network security controls"},
                {"id": "2.1", "name": "Secure Configurations", "description": "Apply secure configurations to all system components"},
                {"id": "3.1", "name": "Protect Stored Account Data", "description": "Protect stored account data"},
                {"id": "4.1", "name": "Encrypt Transmission", "description": "Protect cardholder data with strong cryptography during transmission"},
                {"id": "5.1", "name": "Anti-Malware", "description": "Protect all systems against malware"},
            ]
        },
        {
            "id": "fw-soc2",
            "name": "SOC 2 Type II",
            "description": "Service Organization Control 2 - Trust Services Criteria",
            "version": "2017",
            "category": "Security",
            "enabled": True,
            "total_controls": 61,
            "controls": [
                {"id": "CC1.1", "name": "COSO Principle 1", "description": "Demonstrates commitment to integrity and ethical values"},
                {"id": "CC2.1", "name": "COSO Principle 2", "description": "Board exercises oversight responsibility"},
                {"id": "CC6.1", "name": "Logical Access Security", "description": "Restricts logical access to systems"},
                {"id": "CC7.1", "name": "System Operations", "description": "Monitors system components"},
            ]
        },
        {
            "id": "fw-nist",
            "name": "NIST CSF 2.0",
            "description": "National Institute of Standards and Technology Cybersecurity Framework",
            "version": "2.0",
            "category": "Security",
            "enabled": False,
            "total_controls": 108,
            "controls": [
                {"id": "GV.OC", "name": "Organizational Context", "description": "Understanding organizational mission and stakeholder expectations"},
                {"id": "ID.AM", "name": "Asset Management", "description": "Identify and manage data, hardware, software"},
                {"id": "PR.AC", "name": "Access Control", "description": "Manage access permissions and authorizations"},
                {"id": "DE.CM", "name": "Continuous Monitoring", "description": "Monitor systems and assets"},
                {"id": "RS.CO", "name": "Communications", "description": "Response activities coordinated with stakeholders"},
            ]
        },
        {
            "id": "fw-gdpr",
            "name": "GDPR",
            "description": "General Data Protection Regulation - EU data privacy law",
            "version": "2018",
            "category": "Privacy",
            "enabled": False,
            "total_controls": 99,
            "controls": [
                {"id": "Art.5", "name": "Data Processing Principles", "description": "Lawfulness, fairness, and transparency"},
                {"id": "Art.6", "name": "Lawful Basis", "description": "Lawfulness of processing"},
                {"id": "Art.17", "name": "Right to Erasure", "description": "Right to be forgotten"},
                {"id": "Art.25", "name": "Privacy by Design", "description": "Data protection by design and by default"},
                {"id": "Art.32", "name": "Security of Processing", "description": "Implement appropriate technical measures"},
            ]
        },
        {
            "id": "fw-mas-trm",
            "name": "MAS TRM Guidelines",
            "description": "Monetary Authority of Singapore - Technology Risk Management Guidelines",
            "version": "2021",
            "category": "Financial",
            "enabled": True,
            "total_controls": 85,
            "controls": [
                {"id": "TRM.3", "name": "Technology Risk Governance", "description": "Board and senior management oversight of technology risks"},
                {"id": "TRM.4", "name": "Technology Risk Management Framework", "description": "Establish comprehensive risk management framework"},
                {"id": "TRM.5", "name": "IT Project Management", "description": "Robust project management practices"},
                {"id": "TRM.6", "name": "Software Development", "description": "Secure software development lifecycle"},
                {"id": "TRM.7", "name": "IT Service Management", "description": "IT service management processes"},
                {"id": "TRM.9", "name": "Cyber Security", "description": "Cyber security operations and monitoring"},
                {"id": "TRM.11", "name": "Data Security", "description": "Protection of customer and critical data"},
            ]
        },
        {
            "id": "fw-rbi",
            "name": "RBI IT Framework",
            "description": "Reserve Bank of India - Information Technology Framework for Banks",
            "version": "2023",
            "category": "Financial",
            "enabled": True,
            "total_controls": 78,
            "controls": [
                {"id": "RBI.2", "name": "IT Governance", "description": "Board approved IT strategy and governance"},
                {"id": "RBI.3", "name": "IT Infrastructure", "description": "Robust and scalable IT infrastructure"},
                {"id": "RBI.4", "name": "IS Audit", "description": "Information Systems audit framework"},
                {"id": "RBI.5", "name": "Cyber Security", "description": "Cyber security framework and SOC"},
                {"id": "RBI.6", "name": "IT Risk Management", "description": "IT risk assessment and management"},
                {"id": "RBI.7", "name": "Business Continuity", "description": "Business continuity planning and DR"},
                {"id": "RBI.8", "name": "Customer Data Protection", "description": "Data privacy and protection measures"},
            ]
        }
    ]
    db.frameworks.insert_many(frameworks)
    
    # ========== UNIFIED CONTROLS (CCF) ==========
    print("🎯 Seeding Unified Controls...")
    unified_controls = [
        {
            "id": "ctrl-001",
            "ccf_id": "CCF-AC-001",
            "name": "Access Control Policy",
            "description": "Establish and maintain access control policies",
            "control_type": "Preventive",
            "frequency": "Annual",
            "owner": "Security Team",
            "status": "Effective",
            "mapped_framework_controls": [
                {"framework": "ISO 27001:2022", "control_id": "A.5.1", "control_name": "Policies for information security"},
                {"framework": "PCI-DSS v4.0", "control_id": "1.1", "control_name": "Network Security Controls"},
                {"framework": "SOC 2 Type II", "control_id": "CC6.1", "control_name": "Logical Access Security"},
                {"framework": "MAS TRM Guidelines", "control_id": "TRM.3", "control_name": "Technology Risk Governance"},
                {"framework": "RBI IT Framework", "control_id": "RBI.2", "control_name": "IT Governance"}
            ],
            "mapped_policies": [
                {"policy_id": "POL-001", "policy_name": "Information Security Policy"},
                {"policy_id": "POL-002", "policy_name": "Access Control Policy"}
            ]
        },
        {
            "id": "ctrl-002",
            "ccf_id": "CCF-AC-002",
            "name": "User Access Management",
            "description": "Manage user access rights throughout the user lifecycle",
            "control_type": "Preventive",
            "frequency": "Quarterly",
            "owner": "IT Operations",
            "status": "Effective",
            "mapped_framework_controls": [
                {"framework": "ISO 27001:2022", "control_id": "A.8.2", "control_name": "Privileged access rights"},
                {"framework": "PCI-DSS v4.0", "control_id": "2.1", "control_name": "Secure Configurations"},
                {"framework": "MAS TRM Guidelines", "control_id": "TRM.9", "control_name": "Cyber Security"},
                {"framework": "RBI IT Framework", "control_id": "RBI.5", "control_name": "Cyber Security"}
            ],
            "mapped_policies": [
                {"policy_id": "POL-002", "policy_name": "Access Control Policy"}
            ]
        },
        {
            "id": "ctrl-003",
            "ccf_id": "CCF-DP-001",
            "name": "Data Protection",
            "description": "Protect sensitive data at rest and in transit",
            "control_type": "Preventive",
            "frequency": "Continuous",
            "owner": "Security Team",
            "status": "Effective",
            "mapped_framework_controls": [
                {"framework": "PCI-DSS v4.0", "control_id": "3.1", "control_name": "Protect Stored Account Data"},
                {"framework": "PCI-DSS v4.0", "control_id": "4.1", "control_name": "Encrypt Transmission"},
                {"framework": "GDPR", "control_id": "Art.32", "control_name": "Security of Processing"},
                {"framework": "MAS TRM Guidelines", "control_id": "TRM.11", "control_name": "Data Security"},
                {"framework": "RBI IT Framework", "control_id": "RBI.8", "control_name": "Customer Data Protection"}
            ],
            "mapped_policies": [
                {"policy_id": "POL-003", "policy_name": "Data Protection Policy"}
            ]
        },
        {
            "id": "ctrl-004",
            "ccf_id": "CCF-AI-001",
            "name": "AI Governance",
            "description": "Govern AI systems throughout their lifecycle with risk management",
            "control_type": "Preventive",
            "frequency": "Quarterly",
            "owner": "AI Ethics Board",
            "status": "Needs Improvement",
            "mapped_framework_controls": [
                {"framework": "ISO 42001:2023", "control_id": "AI.4.1", "control_name": "AI Policy"},
                {"framework": "ISO 42001:2023", "control_id": "AI.5.1", "control_name": "AI Risk Assessment"},
                {"framework": "ISO 42001:2023", "control_id": "AI.6.1", "control_name": "AI System Lifecycle"}
            ],
            "mapped_policies": [
                {"policy_id": "POL-006", "policy_name": "AI Governance Policy"}
            ]
        },
        {
            "id": "ctrl-005",
            "ccf_id": "CCF-AI-002",
            "name": "AI Transparency & Explainability",
            "description": "Ensure AI decisions are transparent and explainable to stakeholders",
            "control_type": "Detective",
            "frequency": "Per Model",
            "owner": "AI Ethics Board",
            "status": "Partially Effective",
            "mapped_framework_controls": [
                {"framework": "ISO 42001:2023", "control_id": "AI.8.1", "control_name": "AI Transparency"},
                {"framework": "ISO 42001:2023", "control_id": "AI.9.1", "control_name": "Human Oversight"}
            ],
            "mapped_policies": [
                {"policy_id": "POL-006", "policy_name": "AI Governance Policy"},
                {"policy_id": "POL-007", "policy_name": "AI Ethics Policy"}
            ]
        },
        {
            "id": "ctrl-006",
            "ccf_id": "CCF-VM-001",
            "name": "Vulnerability Management",
            "description": "Identify, assess, and remediate security vulnerabilities",
            "control_type": "Detective",
            "frequency": "Weekly",
            "owner": "Security Team",
            "status": "Effective",
            "mapped_framework_controls": [
                {"framework": "PCI-DSS v4.0", "control_id": "5.1", "control_name": "Anti-Malware"},
                {"framework": "NIST CSF 2.0", "control_id": "DE.CM", "control_name": "Continuous Monitoring"},
                {"framework": "MAS TRM Guidelines", "control_id": "TRM.9", "control_name": "Cyber Security"}
            ],
            "mapped_policies": [
                {"policy_id": "POL-004", "policy_name": "Vulnerability Management Policy"}
            ]
        },
        {
            "id": "ctrl-007",
            "ccf_id": "CCF-BC-001",
            "name": "Business Continuity",
            "description": "Ensure business continuity and disaster recovery capabilities",
            "control_type": "Corrective",
            "frequency": "Annual",
            "owner": "IT Operations",
            "status": "Effective",
            "mapped_framework_controls": [
                {"framework": "ISO 27001:2022", "control_id": "A.5.2", "control_name": "Information security roles"},
                {"framework": "SOC 2 Type II", "control_id": "CC7.1", "control_name": "System Operations"},
                {"framework": "MAS TRM Guidelines", "control_id": "TRM.7", "control_name": "IT Service Management"},
                {"framework": "RBI IT Framework", "control_id": "RBI.7", "control_name": "Business Continuity"}
            ],
            "mapped_policies": [
                {"policy_id": "POL-005", "policy_name": "Business Continuity Policy"}
            ]
        }
    ]
    db.unified_controls.insert_many(unified_controls)
    
    # ========== POLICIES ==========
    print("📜 Seeding Policies...")
    policies = [
        {
            "id": "POL-001",
            "policy_id": "POL-001",
            "name": "Information Security Policy",
            "description": "Overarching policy defining the organization's approach to information security",
            "category": "Security",
            "owner": "CISO",
            "status": "Active",
            "last_reviewed": "2024-01-15",
            "next_review": "2025-01-15",
            "mapped_controls": [
                {"control_id": "ctrl-001", "ccf_id": "CCF-AC-001", "control_name": "Access Control Policy"},
                {"control_id": "ctrl-006", "ccf_id": "CCF-VM-001", "control_name": "Vulnerability Management"}
            ],
            "mapped_frameworks": ["ISO 27001:2022", "SOC 2 Type II", "NIST CSF 2.0"]
        },
        {
            "id": "POL-002",
            "policy_id": "POL-002",
            "name": "Access Control Policy",
            "description": "Policy governing user access to systems and data",
            "category": "Security",
            "owner": "Security Team",
            "status": "Active",
            "last_reviewed": "2024-02-01",
            "next_review": "2025-02-01",
            "mapped_controls": [
                {"control_id": "ctrl-001", "ccf_id": "CCF-AC-001", "control_name": "Access Control Policy"},
                {"control_id": "ctrl-002", "ccf_id": "CCF-AC-002", "control_name": "User Access Management"}
            ],
            "mapped_frameworks": ["ISO 27001:2022", "PCI-DSS v4.0", "MAS TRM Guidelines", "RBI IT Framework"]
        },
        {
            "id": "POL-003",
            "policy_id": "POL-003",
            "name": "Data Protection Policy",
            "description": "Policy for protecting sensitive and personal data",
            "category": "Privacy",
            "owner": "DPO",
            "status": "Active",
            "last_reviewed": "2024-03-01",
            "next_review": "2025-03-01",
            "mapped_controls": [
                {"control_id": "ctrl-003", "ccf_id": "CCF-DP-001", "control_name": "Data Protection"}
            ],
            "mapped_frameworks": ["GDPR", "PCI-DSS v4.0", "MAS TRM Guidelines", "RBI IT Framework"]
        },
        {
            "id": "POL-004",
            "policy_id": "POL-004",
            "name": "Vulnerability Management Policy",
            "description": "Policy for identifying and remediating security vulnerabilities",
            "category": "Security",
            "owner": "Security Team",
            "status": "Active",
            "last_reviewed": "2024-01-20",
            "next_review": "2025-01-20",
            "mapped_controls": [
                {"control_id": "ctrl-006", "ccf_id": "CCF-VM-001", "control_name": "Vulnerability Management"}
            ],
            "mapped_frameworks": ["ISO 27001:2022", "PCI-DSS v4.0", "MAS TRM Guidelines"]
        },
        {
            "id": "POL-005",
            "policy_id": "POL-005",
            "name": "Business Continuity Policy",
            "description": "Policy ensuring business continuity and disaster recovery",
            "category": "Operations",
            "owner": "IT Operations",
            "status": "Active",
            "last_reviewed": "2024-02-15",
            "next_review": "2025-02-15",
            "mapped_controls": [
                {"control_id": "ctrl-007", "ccf_id": "CCF-BC-001", "control_name": "Business Continuity"}
            ],
            "mapped_frameworks": ["ISO 27001:2022", "SOC 2 Type II", "MAS TRM Guidelines", "RBI IT Framework"]
        },
        {
            "id": "POL-006",
            "policy_id": "POL-006",
            "name": "AI Governance Policy",
            "description": "Policy governing the development, deployment, and use of AI systems",
            "category": "AI Governance",
            "owner": "AI Ethics Board",
            "status": "Active",
            "last_reviewed": "2024-06-01",
            "next_review": "2025-06-01",
            "mapped_controls": [
                {"control_id": "ctrl-004", "ccf_id": "CCF-AI-001", "control_name": "AI Governance"},
                {"control_id": "ctrl-005", "ccf_id": "CCF-AI-002", "control_name": "AI Transparency & Explainability"}
            ],
            "mapped_frameworks": ["ISO 42001:2023"]
        },
        {
            "id": "POL-007",
            "policy_id": "POL-007",
            "name": "AI Ethics Policy",
            "description": "Ethical guidelines for AI development and deployment",
            "category": "AI Governance",
            "owner": "AI Ethics Board",
            "status": "Active",
            "last_reviewed": "2024-06-01",
            "next_review": "2025-06-01",
            "mapped_controls": [
                {"control_id": "ctrl-005", "ccf_id": "CCF-AI-002", "control_name": "AI Transparency & Explainability"}
            ],
            "mapped_frameworks": ["ISO 42001:2023"]
        }
    ]
    db.policies.insert_many(policies)
    
    # ========== CONNECTORS (Automated Testing) ==========
    print("🔌 Seeding Connectors...")
    connectors = [
        {
            "id": "conn-aws",
            "name": "AWS Security Hub",
            "type": "cloud",
            "provider": "AWS",
            "status": "Connected",
            "last_sync": datetime.utcnow().isoformat(),
            "controls_covered": ["CCF-AC-001", "CCF-DP-001", "CCF-VM-001"],
            "config": {"region": "us-east-1", "account_id": "***hidden***"}
        },
        {
            "id": "conn-github",
            "name": "GitHub Security",
            "type": "code",
            "provider": "GitHub",
            "status": "Connected",
            "last_sync": datetime.utcnow().isoformat(),
            "controls_covered": ["CCF-VM-001"],
            "config": {"org": "your-org", "repos": ["main-app", "api-service"]}
        },
        {
            "id": "conn-okta",
            "name": "Okta Identity",
            "type": "identity",
            "provider": "Okta",
            "status": "Disconnected",
            "last_sync": None,
            "controls_covered": ["CCF-AC-001", "CCF-AC-002"],
            "config": {}
        },
        {
            "id": "conn-azure",
            "name": "Azure Security Center",
            "type": "cloud",
            "provider": "Azure",
            "status": "Disconnected",
            "last_sync": None,
            "controls_covered": ["CCF-AC-001", "CCF-DP-001"],
            "config": {}
        }
    ]
    db.connectors.insert_many(connectors)
    
    # ========== CONTROL TESTS ==========
    print("🧪 Seeding Control Tests...")
    control_tests = [
        {
            "id": str(uuid.uuid4()),
            "control_id": "ctrl-001",
            "control_ccf_id": "CCF-AC-001",
            "test_type": "Automated",
            "connector_id": "conn-aws",
            "test_date": (datetime.utcnow() - timedelta(days=1)).strftime("%Y-%m-%d"),
            "tester": "AWS Security Hub",
            "result": "Pass",
            "evidence": "aws-security-hub-report-2024.pdf",
            "notes": "All IAM policies compliant with least privilege principle",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "control_id": "ctrl-002",
            "control_ccf_id": "CCF-AC-002",
            "test_type": "Manual",
            "connector_id": None,
            "test_date": (datetime.utcnow() - timedelta(days=7)).strftime("%Y-%m-%d"),
            "tester": "John Auditor",
            "result": "Pass",
            "evidence": "access-review-q4-2024.xlsx",
            "notes": "Quarterly access review completed. 3 stale accounts removed.",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "control_id": "ctrl-003",
            "control_ccf_id": "CCF-DP-001",
            "test_type": "Automated",
            "connector_id": "conn-aws",
            "test_date": (datetime.utcnow() - timedelta(days=2)).strftime("%Y-%m-%d"),
            "tester": "AWS Security Hub",
            "result": "Pass",
            "evidence": "encryption-status-report.json",
            "notes": "All S3 buckets encrypted, RDS encryption enabled",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "control_id": "ctrl-004",
            "control_ccf_id": "CCF-AI-001",
            "test_type": "Manual",
            "connector_id": None,
            "test_date": (datetime.utcnow() - timedelta(days=14)).strftime("%Y-%m-%d"),
            "tester": "Jane Analyst",
            "result": "Partial",
            "evidence": "ai-governance-assessment.pdf",
            "notes": "AI inventory complete but risk assessments pending for 2 models",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "control_id": "ctrl-006",
            "control_ccf_id": "CCF-VM-001",
            "test_type": "Automated",
            "connector_id": "conn-github",
            "test_date": datetime.utcnow().strftime("%Y-%m-%d"),
            "tester": "GitHub Dependabot",
            "result": "Fail",
            "evidence": "dependabot-alerts.json",
            "notes": "3 critical vulnerabilities found in dependencies",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "control_id": "ctrl-007",
            "control_ccf_id": "CCF-BC-001",
            "test_type": "Manual",
            "connector_id": None,
            "test_date": (datetime.utcnow() - timedelta(days=30)).strftime("%Y-%m-%d"),
            "tester": "John Auditor",
            "result": "Pass",
            "evidence": "dr-test-results-2024.pdf",
            "notes": "Annual DR test successful. RTO: 2 hours, RPO: 15 minutes",
            "created_at": datetime.utcnow().isoformat()
        }
    ]
    db.control_tests.insert_many(control_tests)
    
    # ========== ISSUES ==========
    print("⚠️  Seeding Issues...")
    issues = [
        {
            "id": str(uuid.uuid4()),
            "title": "Critical vulnerabilities in npm packages",
            "description": "GitHub Dependabot found 3 critical CVEs in production dependencies",
            "severity": "Critical",
            "status": "Open",
            "control_id": "ctrl-006",
            "assigned_to": "Security Team",
            "due_date": (datetime.utcnow() + timedelta(days=3)).strftime("%Y-%m-%d"),
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "title": "AI Model risk assessment overdue",
            "description": "Risk assessment for Customer Churn Prediction model is 30 days overdue",
            "severity": "High",
            "status": "In Progress",
            "control_id": "ctrl-004",
            "assigned_to": "AI Ethics Board",
            "due_date": (datetime.utcnow() + timedelta(days=7)).strftime("%Y-%m-%d"),
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "title": "MFA not enforced for admin accounts",
            "description": "2 admin accounts found without MFA enabled",
            "severity": "High",
            "status": "Open",
            "control_id": "ctrl-002",
            "assigned_to": "IT Operations",
            "due_date": (datetime.utcnow() + timedelta(days=1)).strftime("%Y-%m-%d"),
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "title": "Policy review overdue",
            "description": "Information Security Policy review is 2 months overdue",
            "severity": "Medium",
            "status": "Resolved",
            "control_id": "ctrl-001",
            "assigned_to": "CISO",
            "due_date": (datetime.utcnow() - timedelta(days=10)).strftime("%Y-%m-%d"),
            "created_at": datetime.utcnow().isoformat()
        }
    ]
    db.issues.insert_many(issues)
    
    # ========== RISKS ==========
    print("🎲 Seeding Risks...")
    risks = [
        {
            "id": "risk-001",
            "name": "Data Breach Risk",
            "description": "Risk of unauthorized access to sensitive customer data",
            "category": "Security",
            "inherent_risk_score": 9,
            "residual_risk_score": 4,
            "status": "Active",
            "owner": "CISO",
            "treatment": "Mitigate",
            "kri_ids": ["kri-001", "kri-002"],
            "linked_control_ids": ["ctrl-001", "ctrl-002", "ctrl-003"],
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "risk-002",
            "name": "AI Bias Risk",
            "description": "Risk of AI models producing biased or unfair outcomes",
            "category": "AI Governance",
            "inherent_risk_score": 8,
            "residual_risk_score": 6,
            "status": "Active",
            "owner": "AI Ethics Board",
            "treatment": "Mitigate",
            "kri_ids": ["kri-003"],
            "linked_control_ids": ["ctrl-004", "ctrl-005"],
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "risk-003",
            "name": "Regulatory Non-Compliance",
            "description": "Risk of failing to meet regulatory requirements (MAS, RBI)",
            "category": "Compliance",
            "inherent_risk_score": 8,
            "residual_risk_score": 3,
            "status": "Active",
            "owner": "Compliance Officer",
            "treatment": "Mitigate",
            "kri_ids": ["kri-004"],
            "linked_control_ids": ["ctrl-001", "ctrl-003"],
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "risk-004",
            "name": "Business Continuity Risk",
            "description": "Risk of extended service disruption affecting business operations",
            "category": "Operations",
            "inherent_risk_score": 7,
            "residual_risk_score": 2,
            "status": "Active",
            "owner": "IT Operations",
            "treatment": "Mitigate",
            "kri_ids": ["kri-005"],
            "linked_control_ids": ["ctrl-007"],
            "created_at": datetime.utcnow().isoformat()
        }
    ]
    db.risks.insert_many(risks)
    
    # ========== KRIs ==========
    print("📊 Seeding KRIs...")
    kris = [
        {
            "id": "kri-001",
            "name": "Failed Login Attempts",
            "description": "Number of failed login attempts per day",
            "risk_id": "risk-001",
            "threshold_green": 100,
            "threshold_yellow": 500,
            "threshold_red": 1000,
            "current_value": 87,
            "unit": "Count",
            "frequency": "Daily",
            "owner": "Security Team",
            "kci_ids": ["kci-001"],
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "kri-002",
            "name": "Unpatched Critical Vulnerabilities",
            "description": "Number of unpatched critical vulnerabilities older than 7 days",
            "risk_id": "risk-001",
            "threshold_green": 0,
            "threshold_yellow": 3,
            "threshold_red": 5,
            "current_value": 3,
            "unit": "Count",
            "frequency": "Weekly",
            "owner": "Security Team",
            "kci_ids": ["kci-002"],
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "kri-003",
            "name": "AI Model Drift Score",
            "description": "Average drift score across production AI models",
            "risk_id": "risk-002",
            "threshold_green": 5,
            "threshold_yellow": 15,
            "threshold_red": 25,
            "current_value": 12,
            "unit": "Percentage",
            "frequency": "Weekly",
            "owner": "AI Ethics Board",
            "kci_ids": ["kci-003"],
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "kri-004",
            "name": "Overdue Compliance Tasks",
            "description": "Number of compliance tasks past due date",
            "risk_id": "risk-003",
            "threshold_green": 0,
            "threshold_yellow": 5,
            "threshold_red": 10,
            "current_value": 2,
            "unit": "Count",
            "frequency": "Weekly",
            "owner": "Compliance Officer",
            "kci_ids": ["kci-004"],
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "kri-005",
            "name": "System Uptime",
            "description": "Percentage of system uptime in the last 30 days",
            "risk_id": "risk-004",
            "threshold_green": 99,
            "threshold_yellow": 97,
            "threshold_red": 95,
            "current_value": 99.7,
            "unit": "Percentage",
            "frequency": "Monthly",
            "owner": "IT Operations",
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
            "name": "Access Review Completion Rate",
            "description": "Percentage of scheduled access reviews completed on time",
            "kri_id": "kri-001",
            "control_id": "ctrl-002",
            "threshold_green": 95,
            "threshold_yellow": 85,
            "threshold_red": 75,
            "current_value": 98,
            "unit": "Percentage",
            "frequency": "Quarterly",
            "owner": "IT Operations",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "kci-002",
            "name": "Patch Compliance Rate",
            "description": "Percentage of systems patched within SLA",
            "kri_id": "kri-002",
            "control_id": "ctrl-006",
            "threshold_green": 95,
            "threshold_yellow": 85,
            "threshold_red": 75,
            "current_value": 89,
            "unit": "Percentage",
            "frequency": "Weekly",
            "owner": "Security Team",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "kci-003",
            "name": "AI Model Monitoring Coverage",
            "description": "Percentage of production AI models with active monitoring",
            "kri_id": "kri-003",
            "control_id": "ctrl-004",
            "threshold_green": 100,
            "threshold_yellow": 90,
            "threshold_red": 80,
            "current_value": 85,
            "unit": "Percentage",
            "frequency": "Monthly",
            "owner": "AI Ethics Board",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "kci-004",
            "name": "Policy Acknowledgment Rate",
            "description": "Percentage of employees who acknowledged security policies",
            "kri_id": "kri-004",
            "control_id": "ctrl-001",
            "threshold_green": 95,
            "threshold_yellow": 85,
            "threshold_red": 75,
            "current_value": 97,
            "unit": "Percentage",
            "frequency": "Annual",
            "owner": "Compliance Officer",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "kci-005",
            "name": "DR Test Success Rate",
            "description": "Percentage of DR tests meeting RTO/RPO objectives",
            "kri_id": "kri-005",
            "control_id": "ctrl-007",
            "threshold_green": 100,
            "threshold_yellow": 90,
            "threshold_red": 80,
            "current_value": 100,
            "unit": "Percentage",
            "frequency": "Annual",
            "owner": "IT Operations",
            "created_at": datetime.utcnow().isoformat()
        }
    ]
    db.kcis.insert_many(kcis)
    
    # ========== AI MODELS REGISTRY ==========
    print("🤖 Seeding AI Models...")
    ai_models = [
        {
            "id": "ai-model-001",
            "name": "Customer Churn Prediction",
            "type": "Classification",
            "version": "2.1.0",
            "status": "Production",
            "risk_level": "High",
            "owner": "Data Science Team",
            "department": "Marketing",
            "purpose": "Predict customer churn probability for retention campaigns",
            "data_sources": ["CRM", "Transaction History", "Support Tickets"],
            "training_data_size": "2.5M records",
            "last_trained": "2024-11-15",
            "accuracy": 0.89,
            "fairness_score": 0.82,
            "explainability_score": 0.75,
            "has_human_oversight": True,
            "pii_involved": True,
            "automated_decisions": False,
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "ai-model-002",
            "name": "Fraud Detection Engine",
            "type": "Anomaly Detection",
            "version": "3.0.2",
            "status": "Production",
            "risk_level": "Critical",
            "owner": "Security Team",
            "department": "Finance",
            "purpose": "Real-time fraud detection for financial transactions",
            "data_sources": ["Transaction System", "User Behavior Analytics"],
            "training_data_size": "50M records",
            "last_trained": "2024-12-01",
            "accuracy": 0.94,
            "fairness_score": 0.88,
            "explainability_score": 0.65,
            "has_human_oversight": True,
            "pii_involved": True,
            "automated_decisions": True,
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "ai-model-003",
            "name": "Resume Screening Assistant",
            "type": "NLP Classification",
            "version": "1.5.0",
            "status": "Testing",
            "risk_level": "High",
            "owner": "HR Tech Team",
            "department": "Human Resources",
            "purpose": "Screen and rank job applications based on requirements",
            "data_sources": ["Resume Database", "Job Descriptions"],
            "training_data_size": "500K records",
            "last_trained": "2024-10-20",
            "accuracy": 0.85,
            "fairness_score": 0.72,
            "explainability_score": 0.80,
            "has_human_oversight": True,
            "pii_involved": True,
            "automated_decisions": False,
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "ai-model-004",
            "name": "Demand Forecasting",
            "type": "Time Series",
            "version": "4.2.1",
            "status": "Production",
            "risk_level": "Medium",
            "owner": "Analytics Team",
            "department": "Supply Chain",
            "purpose": "Forecast product demand for inventory optimization",
            "data_sources": ["Sales Data", "Market Trends", "Weather Data"],
            "training_data_size": "10M records",
            "last_trained": "2024-11-30",
            "accuracy": 0.91,
            "fairness_score": None,
            "explainability_score": 0.90,
            "has_human_oversight": False,
            "pii_involved": False,
            "automated_decisions": True,
            "created_at": datetime.utcnow().isoformat()
        }
    ]
    db.ai_models.insert_many(ai_models)
    
    # ========== AI RISK ASSESSMENTS ==========
    print("📋 Seeding AI Assessments...")
    ai_assessments = [
        {
            "id": "assess-001",
            "model_id": "ai-model-001",
            "model_name": "Customer Churn Prediction",
            "assessment_date": "2024-11-20",
            "assessor": "AI Ethics Board",
            "status": "Completed",
            "overall_risk": "Medium",
            "bias_risk": "Medium",
            "privacy_risk": "High",
            "security_risk": "Low",
            "transparency_risk": "Medium",
            "findings": [
                "Model shows slight bias towards certain age groups",
                "PII data handling needs stronger encryption",
                "Model explanations need improvement for customer-facing use"
            ],
            "recommendations": [
                "Implement age-based fairness constraints in next training",
                "Enable field-level encryption for PII columns",
                "Deploy SHAP explanations for customer service team"
            ],
            "next_review": "2025-05-20",
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "assess-002",
            "model_id": "ai-model-002",
            "model_name": "Fraud Detection Engine",
            "assessment_date": "2024-12-05",
            "assessor": "AI Ethics Board",
            "status": "Completed",
            "overall_risk": "High",
            "bias_risk": "Low",
            "privacy_risk": "High",
            "security_risk": "Medium",
            "transparency_risk": "High",
            "findings": [
                "High volume of automated decisions with financial impact",
                "Explainability is limited for complex fraud patterns",
                "Strong need for human review process for edge cases"
            ],
            "recommendations": [
                "Implement mandatory human review for transactions >$10K",
                "Add rule-based explainability layer",
                "Quarterly bias audits for protected groups"
            ],
            "next_review": "2025-03-05",
            "created_at": datetime.utcnow().isoformat()
        }
    ]
    db.ai_assessments.insert_many(ai_assessments)
    
    # ========== AUDIT LOGS ==========
    print("📝 Seeding Audit Logs...")
    audit_logs = [
        {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "user_id": "user-admin",
            "user_email": "admin@grcplatform.com",
            "action": "LOGIN",
            "resource": "System",
            "details": "Successful login from IP 192.168.1.100",
            "ip_address": "192.168.1.100"
        },
        {
            "id": str(uuid.uuid4()),
            "timestamp": (datetime.utcnow() - timedelta(hours=2)).isoformat(),
            "user_id": "user-admin",
            "user_email": "admin@grcplatform.com",
            "action": "UPDATE",
            "resource": "Framework",
            "details": "Enabled framework: ISO 42001:2023",
            "ip_address": "192.168.1.100"
        },
        {
            "id": str(uuid.uuid4()),
            "timestamp": (datetime.utcnow() - timedelta(hours=5)).isoformat(),
            "user_id": "user-auditor",
            "user_email": "auditor@grcplatform.com",
            "action": "CREATE",
            "resource": "Control Test",
            "details": "Created control test for CCF-AC-002",
            "ip_address": "192.168.1.105"
        },
        {
            "id": str(uuid.uuid4()),
            "timestamp": (datetime.utcnow() - timedelta(days=1)).isoformat(),
            "user_id": "user-analyst",
            "user_email": "analyst@grcplatform.com",
            "action": "VIEW",
            "resource": "AI Model",
            "details": "Viewed AI Model: Fraud Detection Engine",
            "ip_address": "192.168.1.110"
        }
    ]
    db.audit_logs.insert_many(audit_logs)
    
    print("\n" + "="*50)
    print("✅ Database seeding completed!")
    print("="*50)
    print(f"👤 Users: {len(users)}")
    print(f"📦 Frameworks: {len(frameworks)}")
    print(f"🎯 Unified Controls: {len(unified_controls)}")
    print(f"📜 Policies: {len(policies)}")
    print(f"🔌 Connectors: {len(connectors)}")
    print(f"🧪 Control Tests: {len(control_tests)}")
    print(f"⚠️  Issues: {len(issues)}")
    print(f"🎲 Risks: {len(risks)}")
    print(f"📊 KRIs: {len(kris)}")
    print(f"🎯 KCIs: {len(kcis)}")
    print(f"🤖 AI Models: {len(ai_models)}")
    print(f"📋 AI Assessments: {len(ai_assessments)}")
    print(f"📝 Audit Logs: {len(audit_logs)}")
    print("="*50)
    print("\n📌 Test Users:")
    print("   Admin: admin@grcplatform.com / admin123")
    print("   Auditor: auditor@grcplatform.com / auditor123")
    print("   Analyst: analyst@grcplatform.com / analyst123")
    print("="*50)
    
    client.close()

if __name__ == "__main__":
    seed_database()
