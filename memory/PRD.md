# GRC Platform - Product Requirements Document

## Original Problem Statement
Build a dynamic GRC (Governance, Risk, and Compliance) platform using the pure Python Reflex framework that can eventually be sold as a SaaS product.

## Core Requirements
1. **Framework Management**: Ingest standards like PCI DSS, ISO 27001, ISO 42001 (AI), MAS TRM (Singapore), RBI IT Framework (India)
2. **Unified Controls**: Map frameworks to unified internal policies with expandable mapping views
3. **Control Testing**: Manual and automated testing via connectors (AWS, GitHub)
4. **Issue Management**: Track issues found during control testing
5. **Risk Management**: Define risks with AI-powered recommendations (Gemini)
6. **Dynamic Dashboard**: Real-time dashboard with control health and risk ratings
7. **Visual Risk Heatmaps**: Risk heatmap visualization
8. **AI Governance Module**: Model registry, risk assessments, policy compliance
9. **Security**: JWT-based authentication (login/password)
10. **Audit Logs**: System audit log viewer
11. **AI Gap Analysis**: AI-powered compliance gap analysis against any framework
12. **Deployment Guide**: GitHub deployment and MongoDB Atlas setup guide

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
│   ├── database.py          # MongoDB CRUD operations
│   ├── grc_platform.py      # All pages and routing (2700+ lines)
│   └── state.py             # State management classes
├── nginx-reflex-proxy.conf  # Nginx proxy for API routing
├── rxconfig.py              # Reflex configuration
├── seed_data.py             # Database seeding
└── requirements.txt
```

## What's Been Implemented
- [x] JWT Authentication (login/logout flow)
- [x] 8 Compliance Frameworks (PCI DSS, ISO 27001, SOC 2, HIPAA, NIST CSF, ISO 42001, MAS TRM, RBI IT)
- [x] Unified Control Mapping with expandable detail views
- [x] Policy Management with expandable control/framework mappings
- [x] AI-Powered Risk Suggestions using Gemini 2.5 Flash
- [x] **AI-Powered Compliance Gap Analysis** (NEW - Mar 5, 2026)
  - Framework selector with all 8 frameworks
  - Compliance Score (0-100), Maturity Level assessment
  - Critical gaps with severity and AI recommendations
  - Strengths identification
  - Improvement areas with effort estimates
  - Quick wins for immediate action
  - Phased remediation roadmap
- [x] Risk Register with add/create functionality
- [x] Control Testing page
- [x] Issue Management page
- [x] KRI and KCI tracking pages
- [x] Risk Heatmap visualization
- [x] AI Governance Module (Model Registry, Assessments)
- [x] Connectors page
- [x] Audit Logs page (UI only)
- [x] Dashboard with real-time metrics
- [x] Nginx reverse proxy for Kubernetes deployment

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
- [ ] Implement Audit Log backend logic (populate with real events)
- [ ] Add user roles and permissions
- [ ] Multi-tenancy for SaaS

### P2 (Low)
- [ ] PDF/Excel reporting for gap analysis results
- [ ] Real connector integrations (AWS, Azure, GitHub)
- [ ] SSO (SAML/OAuth)
- [ ] Fix cosmetic `.to_string()` quote marks in Reflex display
