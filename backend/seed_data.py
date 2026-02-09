from datetime import datetime, timezone

def get_frameworks_data():
    """Returns actual framework data with real control requirements"""
    
    frameworks = [
        {
            "id": "fw-iso27001",
            "name": "ISO 27001:2022",
            "description": "Information security management system (ISMS) requirements",
            "version": "2022",
            "enabled": False,
            "total_controls": 93,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "fw-pci-dss",
            "name": "PCI DSS v4.0",
            "description": "Payment Card Industry Data Security Standard",
            "version": "4.0",
            "enabled": False,
            "total_controls": 63,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "fw-soc2",
            "name": "SOC 2 Type II",
            "description": "Service Organization Control 2",
            "version": "2017",
            "enabled": False,
            "total_controls": 64,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "fw-nist-csf",
            "name": "NIST Cybersecurity Framework",
            "description": "NIST CSF 2.0",
            "version": "2.0",
            "enabled": False,
            "total_controls": 108,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "fw-gdpr",
            "name": "GDPR",
            "description": "General Data Protection Regulation",
            "version": "2018",
            "enabled": False,
            "total_controls": 45,
            "created_at": datetime.now(timezone.utc).isoformat()
        }
    ]
    
    # ISO 27001 Controls (Annex A)
    iso27001_controls = [
        {"id": "iso27001-5.1", "framework_id": "fw-iso27001", "control_id": "5.1", "title": "Policies for information security", "description": "Information security policy and topic-specific policies shall be defined, approved by management, published, communicated to and acknowledged by relevant personnel and relevant interested parties, and reviewed at planned intervals and if significant changes occur.", "category": "Organizational", "testing_procedure": "Review policy documents, approval records, communication logs, and review cycles"},
        {"id": "iso27001-5.7", "framework_id": "fw-iso27001", "control_id": "5.7", "title": "Threat intelligence", "description": "Information relating to information security threats shall be collected and analyzed to produce threat intelligence.", "category": "Organizational", "testing_procedure": "Review threat intelligence sources, analysis reports, and integration with security operations"},
        {"id": "iso27001-5.10", "framework_id": "fw-iso27001", "control_id": "5.10", "title": "Acceptable use of information", "description": "Rules for the acceptable use and procedures for handling information shall be identified, documented and implemented.", "category": "Organizational", "testing_procedure": "Review acceptable use policies, training records, and compliance monitoring"},
        {"id": "iso27001-5.15", "framework_id": "fw-iso27001", "control_id": "5.15", "title": "Access control", "description": "Rules to control physical and logical access to information and other associated assets shall be established and implemented based on business and information security requirements.", "category": "Organizational", "testing_procedure": "Review access control policies, user access reviews, and segregation of duties"},
        {"id": "iso27001-5.18", "framework_id": "fw-iso27001", "control_id": "5.18", "title": "Access rights", "description": "Access rights to information and other associated assets shall be provisioned, reviewed, modified and removed in accordance with the organization's topic-specific policy on and rules for access control.", "category": "Organizational", "testing_procedure": "Test user provisioning process, access reviews, and deprovisioning procedures"},
        {"id": "iso27001-8.2", "framework_id": "fw-iso27001", "control_id": "8.2", "title": "Privileged access rights", "description": "The allocation and use of privileged access rights shall be restricted and managed.", "category": "Technological", "testing_procedure": "Review privileged user list, approval process, and monitoring of privileged activities"},
        {"id": "iso27001-8.3", "framework_id": "fw-iso27001", "control_id": "8.3", "title": "Information access restriction", "description": "Access to information and other associated assets shall be restricted in accordance with the established topic-specific policy on access control.", "category": "Technological", "testing_procedure": "Test access controls, least privilege implementation, and access logging"},
        {"id": "iso27001-8.5", "framework_id": "fw-iso27001", "control_id": "8.5", "title": "Secure authentication", "description": "Secure authentication technologies and procedures shall be implemented based on information access restrictions and the topic-specific policy on access control.", "category": "Technological", "testing_procedure": "Review authentication methods, MFA implementation, and password policies"},
        {"id": "iso27001-8.10", "framework_id": "fw-iso27001", "control_id": "8.10", "title": "Information deletion", "description": "Information stored in information systems, devices or in any other storage media shall be deleted when no longer required.", "category": "Technological", "testing_procedure": "Review data retention policies, deletion procedures, and verification of secure deletion"},
        {"id": "iso27001-8.24", "framework_id": "fw-iso27001", "control_id": "8.24", "title": "Use of cryptography", "description": "Rules for the effective use of cryptography, including cryptographic key management, shall be defined and implemented.", "category": "Technological", "testing_procedure": "Review cryptographic standards, key management procedures, and encryption implementation"},
    ]
    
    # PCI DSS Controls
    pci_dss_controls = [
        {"id": "pci-1.1.1", "framework_id": "fw-pci-dss", "control_id": "1.1.1", "title": "Processes and mechanisms for installing and maintaining network security controls", "description": "All security policies and operational procedures for network security controls are documented, kept up to date, and in use.", "category": "Network Security", "testing_procedure": "Review network security policies, change management records, and implementation evidence"},
        {"id": "pci-1.2.1", "framework_id": "fw-pci-dss", "control_id": "1.2.1", "title": "Configuration standards for NSCs", "description": "Configuration standards for network security control (NSC) rulesets are defined and implemented.", "category": "Network Security", "testing_procedure": "Review firewall rules, network segmentation, and configuration standards"},
        {"id": "pci-2.1.1", "framework_id": "fw-pci-dss", "control_id": "2.1.1", "title": "Configuration standards for system components", "description": "Configuration standards are defined and implemented for all system components.", "category": "Secure Configuration", "testing_procedure": "Review hardening guides, baseline configurations, and compliance scans"},
        {"id": "pci-3.3.1", "framework_id": "fw-pci-dss", "control_id": "3.3.1", "title": "SAD not retained after authorization", "description": "Sensitive authentication data (SAD) is not retained after authorization, even if encrypted.", "category": "Data Protection", "testing_procedure": "Review data flows, storage locations, and retention policies for SAD"},
        {"id": "pci-3.5.1", "framework_id": "fw-pci-dss", "control_id": "3.5.1", "title": "Account data storage restrictions", "description": "Account data storage is kept to a minimum through implementation of data retention and disposal policies.", "category": "Data Protection", "testing_procedure": "Review data retention policies, storage locations, and disposal procedures"},
        {"id": "pci-4.2.1", "framework_id": "fw-pci-dss", "control_id": "4.2.1", "title": "Strong cryptography for PAN transmission", "description": "Strong cryptography and security protocols are implemented to safeguard PAN during transmission over open, public networks.", "category": "Data Protection", "testing_procedure": "Test TLS configuration, encryption strength, and data in transit protection"},
        {"id": "pci-8.2.1", "framework_id": "fw-pci-dss", "control_id": "8.2.1", "title": "User identity verification before password reset", "description": "User identity is verified before modifying any authentication credential.", "category": "Access Control", "testing_procedure": "Test password reset process, identity verification methods, and audit logs"},
        {"id": "pci-8.3.1", "framework_id": "fw-pci-dss", "control_id": "8.3.1", "title": "Multi-factor authentication for personnel", "description": "Multi-factor authentication (MFA) is implemented for all access into the CDE.", "category": "Access Control", "testing_procedure": "Test MFA implementation, coverage, and bypass controls"},
        {"id": "pci-10.2.1", "framework_id": "fw-pci-dss", "control_id": "10.2.1", "title": "Audit logs capture required details", "description": "Audit logs are enabled and active for all system components and cardholder data.", "category": "Logging", "testing_procedure": "Review logging configuration, log content, and coverage of critical events"},
        {"id": "pci-11.3.1", "framework_id": "fw-pci-dss", "control_id": "11.3.1", "title": "External penetration testing", "description": "External penetration testing is performed at least annually and after significant changes.", "category": "Security Testing", "testing_procedure": "Review penetration testing reports, scope, and remediation tracking"},
    ]
    
    # SOC 2 Controls
    soc2_controls = [
        {"id": "soc2-cc6.1", "framework_id": "fw-soc2", "control_id": "CC6.1", "title": "Logical and Physical Access Controls", "description": "The entity implements logical access security software, infrastructure, and architectures over protected information assets to protect them from security events.", "category": "Access Control", "testing_procedure": "Review access control lists, authentication mechanisms, and authorization processes"},
        {"id": "soc2-cc6.2", "framework_id": "fw-soc2", "control_id": "CC6.2", "title": "Authentication and Access", "description": "Prior to issuing system credentials and granting system access, the entity registers and authorizes new internal and external users.", "category": "Access Control", "testing_procedure": "Test user provisioning process, approval workflows, and access reviews"},
        {"id": "soc2-cc6.3", "framework_id": "fw-soc2", "control_id": "CC6.3", "title": "User Authentication", "description": "The entity uses authentication tools and techniques to authenticate individuals and verify that they have access to only the information that is appropriate for their role.", "category": "Access Control", "testing_procedure": "Review MFA implementation, password policies, and role-based access"},
        {"id": "soc2-cc6.6", "framework_id": "fw-soc2", "control_id": "CC6.6", "title": "Logical Access Security Measures", "description": "The entity implements logical access security measures to protect against threats from sources outside its system boundaries.", "category": "Access Control", "testing_procedure": "Review perimeter security, VPN access, and external authentication"},
        {"id": "soc2-cc7.1", "framework_id": "fw-soc2", "control_id": "CC7.1", "title": "System Operations", "description": "The entity ensures that the entity's system continues to operate and that system incidents are detected in a timely manner.", "category": "Operations", "testing_procedure": "Review monitoring tools, alerting mechanisms, and incident detection processes"},
        {"id": "soc2-cc7.2", "framework_id": "fw-soc2", "control_id": "CC7.2", "title": "Change Management", "description": "The entity authorizes, designs, develops, configures, documents, tests, approves, and implements changes to infrastructure, data, software, and procedures.", "category": "Operations", "testing_procedure": "Review change management process, approvals, testing, and rollback procedures"},
        {"id": "soc2-cc8.1", "framework_id": "fw-soc2", "control_id": "CC8.1", "title": "Change Management Program", "description": "The entity authorizes, designs, develops or acquires, implements, operates, approves, maintains, and monitors environmental protections, software, data backup processes, and recovery infrastructure.", "category": "Operations", "testing_procedure": "Review backup procedures, recovery testing, and business continuity plans"},
    ]
    
    # NIST CSF Controls  
    nist_controls = [
        {"id": "nist-id.am-1", "framework_id": "fw-nist-csf", "control_id": "ID.AM-1", "title": "Physical devices and systems inventoried", "description": "Physical devices and systems within the organization are inventoried", "category": "Identify", "testing_procedure": "Review asset inventory, discovery processes, and inventory accuracy"},
        {"id": "nist-id.am-2", "framework_id": "fw-nist-csf", "control_id": "ID.AM-2", "title": "Software platforms and applications inventoried", "description": "Software platforms and applications within the organization are inventoried", "category": "Identify", "testing_procedure": "Review software inventory, license management, and unauthorized software controls"},
        {"id": "nist-pr.ac-1", "framework_id": "fw-nist-csf", "control_id": "PR.AC-1", "title": "Identities and credentials managed", "description": "Identities and credentials are issued, managed, verified, revoked, and audited for authorized devices, users and processes", "category": "Protect", "testing_procedure": "Test user lifecycle management, credential policies, and access reviews"},
        {"id": "nist-pr.ac-4", "framework_id": "fw-nist-csf", "control_id": "PR.AC-4", "title": "Access permissions and authorizations managed", "description": "Access permissions and authorizations are managed, incorporating the principles of least privilege and separation of duties", "category": "Protect", "testing_procedure": "Review access control policies, segregation of duties, and least privilege implementation"},
        {"id": "nist-pr.ds-1", "framework_id": "fw-nist-csf", "control_id": "PR.DS-1", "title": "Data-at-rest protected", "description": "Data-at-rest is protected", "category": "Protect", "testing_procedure": "Review encryption implementation, key management, and data classification"},
        {"id": "nist-de.cm-1", "framework_id": "fw-nist-csf", "control_id": "DE.CM-1", "title": "Network monitored", "description": "The network is monitored to detect potential cybersecurity events", "category": "Detect", "testing_procedure": "Review network monitoring tools, IDS/IPS, and security event detection"},
        {"id": "nist-rs.rp-1", "framework_id": "fw-nist-csf", "control_id": "RS.RP-1", "title": "Response plan executed", "description": "Response plan is executed during or after an incident", "category": "Respond", "testing_procedure": "Review incident response procedures, playbooks, and testing evidence"},
        {"id": "nist-rc.rp-1", "framework_id": "fw-nist-csf", "control_id": "RC.RP-1", "title": "Recovery plan executed", "description": "Recovery plan is executed during or after a cybersecurity incident", "category": "Recover", "testing_procedure": "Review recovery procedures, backup restoration testing, and RTO/RPO metrics"},
    ]
    
    # GDPR Controls
    gdpr_controls = [
        {"id": "gdpr-art5", "framework_id": "fw-gdpr", "control_id": "Article 5", "title": "Principles relating to processing of personal data", "description": "Personal data shall be processed lawfully, fairly and in a transparent manner", "category": "Data Processing", "testing_procedure": "Review data processing inventory, lawful basis, and transparency measures"},
        {"id": "gdpr-art6", "framework_id": "fw-gdpr", "control_id": "Article 6", "title": "Lawfulness of processing", "description": "Processing shall be lawful only if and to the extent that at least one legal basis applies", "category": "Data Processing", "testing_procedure": "Review lawful basis documentation for each processing activity"},
        {"id": "gdpr-art13", "framework_id": "fw-gdpr", "control_id": "Article 13", "title": "Information to be provided", "description": "Where personal data is collected, the controller shall provide data subject with required information", "category": "Transparency", "testing_procedure": "Review privacy notices, consent forms, and data subject information"},
        {"id": "gdpr-art25", "framework_id": "fw-gdpr", "control_id": "Article 25", "title": "Data protection by design and default", "description": "Implement appropriate technical and organizational measures for data protection", "category": "Data Protection", "testing_procedure": "Review privacy by design implementation, default privacy settings, and DPIAs"},
        {"id": "gdpr-art30", "framework_id": "fw-gdpr", "control_id": "Article 30", "title": "Records of processing activities", "description": "Each controller shall maintain a record of processing activities", "category": "Documentation", "testing_procedure": "Review ROPA (Record of Processing Activities), accuracy, and completeness"},
        {"id": "gdpr-art32", "framework_id": "fw-gdpr", "control_id": "Article 32", "title": "Security of processing", "description": "Implement appropriate technical and organizational measures to ensure security", "category": "Security", "testing_procedure": "Review security measures, encryption, access controls, and security testing"},
        {"id": "gdpr-art33", "framework_id": "fw-gdpr", "control_id": "Article 33", "title": "Notification of a personal data breach", "description": "In case of a breach, notify supervisory authority within 72 hours", "category": "Breach Management", "testing_procedure": "Review breach notification procedures, timelines, and testing evidence"},
        {"id": "gdpr-art35", "framework_id": "fw-gdpr", "control_id": "Article 35", "title": "Data protection impact assessment", "description": "Where processing is likely to result in high risk, carry out a DPIA", "category": "Risk Assessment", "testing_procedure": "Review DPIA process, completed assessments, and risk mitigation measures"},
    ]
    
    all_framework_controls = (
        iso27001_controls + 
        pci_dss_controls + 
        soc2_controls + 
        nist_controls + 
        gdpr_controls
    )
    
    # Add timestamps to all controls
    for ctrl in all_framework_controls:
        ctrl["created_at"] = datetime.now(timezone.utc).isoformat()
    
    return {
        "frameworks": frameworks,
        "framework_controls": all_framework_controls
    }


def get_sample_data():
    """Returns sample unified controls and policies for demo"""
    
    unified_controls = [
        {
            "id": "uc-001",
            "ccf_id": "CCF-AC-001",
            "name": "Multi-Factor Authentication",
            "description": "Enforce multi-factor authentication for all user accounts accessing sensitive systems",
            "control_type": "Preventive",
            "frequency": "Continuous",
            "owner": "IT Security",
            "mapped_framework_controls": ["iso27001-8.5", "pci-8.3.1", "soc2-cc6.3"],
            "mapped_policies": ["pol-sec-100"],
            "automation_possible": True,
            "automation_config": {"type": "api_check", "endpoint": "/api/mfa-status"},
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "uc-002",
            "ccf_id": "CCF-DS-002",
            "name": "Data Encryption at Rest",
            "description": "Encrypt all sensitive data stored in databases and file systems",
            "control_type": "Preventive",
            "frequency": "Continuous",
            "owner": "IT Security",
            "mapped_framework_controls": ["iso27001-8.24", "pci-3.5.1", "nist-pr.ds-1", "gdpr-art32"],
            "mapped_policies": ["pol-data-200"],
            "automation_possible": True,
            "automation_config": {"type": "scan", "tool": "encryption_scanner"},
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "uc-003",
            "ccf_id": "CCF-AC-003",
            "name": "User Access Review",
            "description": "Quarterly review of user access rights and permissions",
            "control_type": "Detective",
            "frequency": "Quarterly",
            "owner": "IT Security",
            "mapped_framework_controls": ["iso27001-5.18", "soc2-cc6.2", "nist-pr.ac-4"],
            "mapped_policies": ["pol-iam-150"],
            "automation_possible": False,
            "automation_config": None,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "uc-004",
            "ccf_id": "CCF-LOG-004",
            "name": "Security Event Logging",
            "description": "Enable and maintain audit logs for all security-relevant events",
            "control_type": "Detective",
            "frequency": "Continuous",
            "owner": "IT Operations",
            "mapped_framework_controls": ["pci-10.2.1", "soc2-cc7.1", "nist-de.cm-1"],
            "mapped_policies": ["pol-log-300"],
            "automation_possible": True,
            "automation_config": {"type": "log_check", "tool": "siem"},
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "uc-005",
            "ccf_id": "CCF-BC-005",
            "name": "Backup and Recovery",
            "description": "Regular backup of critical data with tested recovery procedures",
            "control_type": "Corrective",
            "frequency": "Daily",
            "owner": "IT Operations",
            "mapped_framework_controls": ["soc2-cc8.1", "nist-rc.rp-1"],
            "mapped_policies": ["pol-bc-400"],
            "automation_possible": True,
            "automation_config": {"type": "backup_verify", "tool": "backup_system"},
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "uc-006",
            "ccf_id": "CCF-NET-006",
            "name": "Network Segmentation",
            "description": "Implement network segmentation to isolate sensitive systems",
            "control_type": "Preventive",
            "frequency": "Continuous",
            "owner": "Network Team",
            "mapped_framework_controls": ["pci-1.2.1", "iso27001-8.3"],
            "mapped_policies": ["pol-net-500"],
            "automation_possible": True,
            "automation_config": {"type": "network_scan", "tool": "network_mapper"},
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "uc-007",
            "ccf_id": "CCF-PRIV-007",
            "name": "Privacy Impact Assessment",
            "description": "Conduct DPIA for high-risk data processing activities",
            "control_type": "Detective",
            "frequency": "As Needed",
            "owner": "Privacy Officer",
            "mapped_framework_controls": ["gdpr-art35", "gdpr-art25"],
            "mapped_policies": ["pol-priv-600"],
            "automation_possible": False,
            "automation_config": None,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "uc-008",
            "ccf_id": "CCF-CHG-008",
            "name": "Change Management",
            "description": "Formal change approval and testing before production deployment",
            "control_type": "Preventive",
            "frequency": "Per Change",
            "owner": "IT Operations",
            "mapped_framework_controls": ["soc2-cc7.2", "iso27001-5.15"],
            "mapped_policies": ["pol-chg-700"],
            "automation_possible": False,
            "automation_config": None,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "uc-009",
            "ccf_id": "CCF-VUL-009",
            "name": "Vulnerability Management",
            "description": "Regular vulnerability scanning and patching of systems",
            "control_type": "Detective",
            "frequency": "Weekly",
            "owner": "IT Security",
            "mapped_framework_controls": ["pci-11.3.1", "nist-de.cm-1"],
            "mapped_policies": ["pol-vul-800"],
            "automation_possible": True,
            "automation_config": {"type": "vuln_scan", "tool": "vulnerability_scanner"},
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "uc-010",
            "ccf_id": "CCF-INC-010",
            "name": "Incident Response",
            "description": "Documented incident response procedures with regular testing",
            "control_type": "Corrective",
            "frequency": "As Needed",
            "owner": "Security Team",
            "mapped_framework_controls": ["nist-rs.rp-1", "gdpr-art33"],
            "mapped_policies": ["pol-inc-900"],
            "automation_possible": False,
            "automation_config": None,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
    ]
    
    policies = [
        {
            "id": "pol-001",
            "policy_id": "POL-SEC-100",
            "name": "Information Security Policy",
            "description": "Master policy governing information security practices",
            "category": "Security",
            "owner": "CISO",
            "status": "Active",
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "pol-002",
            "policy_id": "POL-DATA-200",
            "name": "Data Protection Policy",
            "description": "Policy for protecting sensitive and personal data",
            "category": "Data Protection",
            "owner": "DPO",
            "status": "Active",
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "pol-003",
            "policy_id": "POL-IAM-150",
            "name": "Identity and Access Management Policy",
            "description": "Policy governing user access and identity management",
            "category": "Access Control",
            "owner": "IT Security",
            "status": "Active",
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "pol-004",
            "policy_id": "POL-LOG-300",
            "name": "Logging and Monitoring Policy",
            "description": "Policy for security event logging and monitoring",
            "category": "Monitoring",
            "owner": "IT Operations",
            "status": "Active",
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "pol-005",
            "policy_id": "POL-BC-400",
            "name": "Business Continuity Policy",
            "description": "Policy for backup, recovery, and business continuity",
            "category": "Business Continuity",
            "owner": "IT Operations",
            "status": "Active",
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "pol-006",
            "policy_id": "POL-NET-500",
            "name": "Network Security Policy",
            "description": "Policy governing network security controls",
            "category": "Network Security",
            "owner": "Network Team",
            "status": "Active",
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "pol-007",
            "policy_id": "POL-PRIV-600",
            "name": "Privacy Policy",
            "description": "Policy for handling personal data and privacy requirements",
            "category": "Privacy",
            "owner": "Privacy Officer",
            "status": "Active",
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "pol-008",
            "policy_id": "POL-CHG-700",
            "name": "Change Management Policy",
            "description": "Policy for managing changes to IT systems",
            "category": "Change Management",
            "owner": "IT Operations",
            "status": "Active",
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "pol-009",
            "policy_id": "POL-VUL-800",
            "name": "Vulnerability Management Policy",
            "description": "Policy for identifying and remediating vulnerabilities",
            "category": "Vulnerability Management",
            "owner": "IT Security",
            "status": "Active",
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "pol-010",
            "policy_id": "POL-INC-900",
            "name": "Incident Response Policy",
            "description": "Policy for responding to security incidents",
            "category": "Incident Management",
            "owner": "Security Team",
            "status": "Active",
            "created_at": datetime.now(timezone.utc).isoformat()
        },
    ]
    
    return {
        "unified_controls": unified_controls,
        "policies": policies
    }
