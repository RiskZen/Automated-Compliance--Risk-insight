# GRC Platform - Product Requirements Document

## Original Problem Statement
Build a comprehensive GRC (Governance, Risk, and Compliance) platform using pure Python Reflex framework for interview case study, evolved into a sellable, dynamic platform.

## What Was Implemented Today (Feb 16, 2026)

### 1. JWT Authentication
- Login page with email/password authentication
- Demo credentials: admin@grcplatform.com / admin123
- Session management and logout functionality

### 2. New Frameworks Added
- **ISO 42001:2023** - AI Management System (39 controls)
- **MAS TRM Guidelines** - Singapore banking regulations (85 controls)
- **RBI IT Framework** - Reserve Bank of India (78 controls)
- Fixed duplicate framework display issue

### 3. AI Governance Module (NEW)
- **AI Model Registry** - Track all AI/ML models with risk levels
- **AI Risk Assessments** - Bias, privacy, security, transparency risk evaluation
- Sample models: Customer Churn Prediction, Fraud Detection Engine, Resume Screening

### 4. Automated Control Testing Connectors (NEW)
- **AWS Security Hub** - Cloud security automated testing
- **GitHub Security** - Code vulnerability scanning
- **Okta Identity** - Identity management (can be connected)
- **Azure Security Center** - Azure cloud testing (can be connected)
- Both manual and automated test options available

### 5. Simplified Control & Policy Mapping
- Clean display of unified controls with framework and policy mappings
- Status indicators (Effective, Needs Improvement)
- Owner and frequency information visible

## Full Feature List

### Frameworks (8 total)
- ISO 27001:2022
- ISO 42001:2023 (AI Governance) - NEW
- PCI-DSS v4.0
- SOC 2 Type II
- NIST CSF 2.0
- GDPR
- MAS TRM Guidelines - NEW
- RBI IT Framework - NEW

### Pages
1. `/login` - Authentication
2. `/` - Dashboard with metrics
3. `/frameworks` - Framework management
4. `/controls` - Unified control mapping
5. `/policies` - Policy management
6. `/testing` - Manual & automated control testing
7. `/issues` - Issue lifecycle management
8. `/risks` - Risk management
9. `/kris` - Key Risk Indicators
10. `/kcis` - Key Control Indicators
11. `/heatmap` - Risk visualization
12. `/ai-models` - AI Model Registry (NEW)
13. `/ai-assessments` - AI Risk Assessments (NEW)
14. `/connectors` - Integration connectors (NEW)
15. `/audit-logs` - Activity tracking (NEW)

## Technology Stack
- **Framework**: Reflex (Pure Python)
- **Database**: MongoDB (pymongo)
- **Authentication**: JWT-based (SHA256 password hashing)

## Test Credentials
| Role | Email | Password |
|------|-------|----------|
| Admin | admin@grcplatform.com | admin123 |
| Auditor | auditor@grcplatform.com | auditor123 |
| Analyst | analyst@grcplatform.com | analyst123 |

## Database Collections
- users, frameworks, unified_controls, policies
- control_tests, issues, risks, kris, kcis
- ai_models, ai_assessments, connectors, audit_logs

## Key Files
- `/app/reflex-grc/grc_platform/grc_platform.py` - Main app
- `/app/reflex-grc/grc_platform/state.py` - State management
- `/app/reflex-grc/grc_platform/database.py` - MongoDB service
- `/app/reflex-grc/seed_data.py` - Database seeding

## Running the App
```bash
cd /app/reflex-grc
reflex run --env prod --single-port --frontend-port 3000
```

## Backlog / Future Tasks
1. **P1**: Add expandable mapping details in Controls/Policies pages
2. **P1**: Connect real cloud connectors (AWS, Azure, GitHub)
3. **P1**: Google Gemini AI integration for risk suggestions
4. **P2**: PDF/Excel report export
5. **P2**: User role-based access control
6. **P2**: Email notifications for issues/assessments
7. **P3**: Real-time dashboard refresh
8. **P3**: Multi-tenancy support

## Known Limitations
- Using MOCK data (seed_data.py)
- Connectors are simulated (not real API integrations)
- AI suggestions not implemented (Gemini API ready)
- Audit logs basic implementation
