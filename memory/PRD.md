# GRC Platform - Product Requirements Document

## Overview
A complete Governance, Risk, and Compliance (GRC) automation platform built in **pure Python** using the **Reflex framework** and powered by **Google Gemini AI**.

## Original Requirements
1. **Framework Management**: Ingest standard frameworks (PCI DSS, ISO 27001, etc.) and allow users to select and map them.
2. **Unified Controls**: Map selected frameworks to a unified set of internal policies.
3. **Control Testing**: Support both automated evidence collection and manual evidence upload to pass/fail controls.
4. **Issue Management**: Track issues found during control testing, including lifecycle management.
5. **Risk Management**: Define top risks with AI recommendations, dynamically map Risks → KRIs → KCIs.
6. **Dynamic Dashboard**: Real-time dashboard reflecting control health and risk ratings.
7. **AI Integration**: Google Gemini for evaluation guidance and risk recommendations.
8. **Technology Stack**: Pure Python using Reflex framework.

## Technology Stack
- **Framework**: Reflex 0.8.26 (Python-only full-stack framework)
- **Database**: MongoDB (via PyMongo sync driver)
- **AI Service**: Google Gemini API (with fallback risks when no API key)
- **Deployment Mode**: Production single-port mode (both frontend and backend on port 3000)

## What's Been Implemented

### ✅ Completed Features (February 2025)
1. **Framework Management Page**
   - 5 compliance frameworks (ISO 27001:2022, PCI-DSS v4.0, SOC 2 Type II, NIST CSF 2.0, GDPR)
   - Enable/disable frameworks with toggle buttons
   - Shows control count per framework

2. **Control Mapping Page (NEW - Interactive Feature)**
   - 7 Unified Controls (CCF) with detailed information
   - **Interactive "View Mapping" button** on each control
   - Expandable mapping details panel showing:
     - Framework Controls → Unified Control → Internal Policies flow
     - Count of mapped framework controls
     - Count of mapped policies
     - Automation readiness indicator
   - Create new controls functionality

3. **Policies Page**
   - List of internal policies
   - Policy details (ID, name, description, category, owner, status)
   - Create new policies

4. **Risks Page**
   - Risk listing with inherent and residual scores
   - AI-powered risk suggestions (using Google Gemini with fallback)

5. **Dashboard**
   - Real-time metrics:
     - Enabled Frameworks count
     - Control Effectiveness percentage
     - Open Issues count
     - Average Risk Score
   - Feature overview

6. **Database Integration**
   - MongoDB connection with PyMongo (sync)
   - Seed data script for demo data
   - All CRUD operations working

### Known Limitations
- Websocket requires **single-port production mode** (`reflex run --env prod --single-port`)
- Google Gemini AI requires user-provided API key (fallback data available)
- Testing pages (Control Testing, Issues, KRIs, KCIs) have basic structure, need full implementation

## File Structure
```
/app/reflex-grc/
├── grc_platform/
│   ├── __init__.py
│   ├── grc_platform.py     # Main app with all pages
│   ├── state.py            # Reflex state management
│   ├── database.py         # MongoDB service (sync PyMongo)
│   └── ai_service.py       # Google Gemini AI service
├── .env                    # Environment variables
├── rxconfig.py             # Reflex configuration
├── requirements.txt        # Python dependencies
└── seed_data.py           # Database seed script
```

## Running the Application
```bash
cd /app/reflex-grc

# Seed the database (first time only)
python seed_data.py

# Run the app (MUST use single-port mode)
reflex run --env prod --single-port --frontend-port 3000
```

## Environment Variables Required
```
MONGO_URL=mongodb://localhost:27017
DB_NAME=grc_reflex_db
GOOGLE_API_KEY=your_gemini_api_key  # Optional, fallback available
```

## Upcoming Tasks (P0)
1. Implement Control Testing page with evidence upload
2. Complete Issues management with lifecycle workflow
3. Add KRI/KCI pages with threshold visualization
4. Risk-to-Control mapping visualization

## Future Enhancements (P1/P2)
1. User authentication and roles
2. Audit trail logging
3. Export/reporting functionality
4. Advanced AI-powered compliance analysis
5. Integration with external GRC tools

## Security Notes
- API keys should be stored in GitHub Codespaces secrets for secure deployment
- Never commit `.env` files with real keys to public repositories

---
Last Updated: February 15, 2025
