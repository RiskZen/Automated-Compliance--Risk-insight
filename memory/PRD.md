# GRC Platform - Product Requirements Document

## Original Problem Statement
Build a dynamic GRC (Governance, Risk, and Compliance) platform using the pure Python Reflex framework that can eventually be sold as a SaaS product.

## Core Requirements
1. **Framework Management**: Ingest standards (PCI DSS, ISO 27001, ISO 42001, MAS TRM, RBI IT)
2. **Unified Controls**: Map frameworks to unified internal policies with expandable mapping views
3. **Control Testing**: Manual and automated testing via connectors
4. **Issue Management**: Track issues found during control testing
5. **Risk Management**: Define risks with AI-powered recommendations (Gemini)
6. **Dynamic Dashboard**: Real-time dashboard with control health and risk ratings
7. **Visual Risk Heatmaps**: Risk heatmap visualization
8. **AI Governance Module**: Model registry, risk assessments, policy compliance
9. **Security**: JWT-based authentication
10. **Audit Logs**: System audit log viewer
11. **AI Gap Analysis**: AI-powered compliance gap analysis
12. **Internal Audit Management**: Plan audits, track findings, manage remediation
13. **Audit Readiness**: Framework-level readiness with CCF testing integration
14. **Workspace/Department Isolation**: Siloed data per department with cross-dept admin view

## Tech Stack
- **Framework**: Reflex (Pure Python)
- **Database**: MongoDB (pymongo)
- **AI**: Google Gemini 2.5 Flash
- **Authentication**: JWT (passlib + python-jose)
- **Deployment**: Reflex production mode with nginx reverse proxy

## Architecture
```
/app/reflex-grc/
├── grc_platform/
│   ├── __init__.py
│   ├── ai_service.py       # Gemini AI (risk suggestions, gap analysis)
│   ├── database.py          # MongoDB CRUD + department-scoped queries
│   ├── grc_platform.py      # All pages and routing
│   └── state.py             # State management with department filtering
├── nginx-reflex-proxy.conf
├── rxconfig.py
├── seed_data.py
└── requirements.txt
```

## What's Been Implemented
- [x] JWT Authentication
- [x] 8 Compliance Frameworks
- [x] Expandable Control/Policy Mappings
- [x] AI-Powered Risk Suggestions (Gemini 2.5 Flash)
- [x] AI-Powered Compliance Gap Analysis
- [x] Internal Audit Management
- [x] Audit Readiness with CCF integration
- [x] **Workspace/Department Isolation** (NEW - Mar 5, 2026)
  - 6 departments: IT & Security, Finance, HR, Operations, Legal & Compliance, Engineering
  - Top bar department selector on every page
  - Department-scoped data: risks, issues, tests, audits filtered per workspace
  - "All Departments" admin view for cross-department overview
  - Blue badge indicator showing active workspace
  - New data (risks, audits) auto-tagged with current department
- [x] Risk Register, Control Testing, Issue Management
- [x] KRI/KCI tracking, Risk Heatmap
- [x] AI Governance Module, Connectors, Audit Logs, Dashboard

## Departments/Workspaces
| Department | Head | Scope |
|---|---|---|
| IT & Security | CISO | Cybersecurity, infrastructure |
| Finance | CFO | Financial ops, compliance |
| Human Resources | CHRO | HR ops, data privacy |
| Operations | COO | Business ops, continuity |
| Legal & Compliance | CLO | Legal, regulatory |
| Engineering | CTO | DevSecOps, product dev |

## Credentials
- Admin: admin@grcplatform.com / admin123
- Analyst: analyst@grcplatform.com / analyst123

## Running the App
```bash
sudo supervisorctl stop frontend backend
cd /app/reflex-grc
nginx -c /app/reflex-grc/nginx-reflex-proxy.conf
REACT_APP_BACKEND_URL=<url> reflex run --env prod --frontend-port 3000 --backend-port 8002
```

## Backlog
### P0 (High)
- [ ] Refactor grc_platform.py into modular page files

### P1 (Medium)
- [ ] Implement Audit Log backend logic
- [ ] User roles/permissions per department
- [ ] Full multi-tenancy (separate clients/orgs)
- [ ] PDF/Excel export for gap analysis and audit reports

### P2 (Low)
- [ ] Real connector integrations (AWS, Azure, GitHub)
- [ ] SSO (SAML/OAuth)
- [ ] Evidence attachments in audit findings
