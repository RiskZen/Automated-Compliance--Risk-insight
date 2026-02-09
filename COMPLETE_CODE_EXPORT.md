# GRC Platform - Complete Source Code Export

## Quick Start Commands

```bash
# Extract the archive
tar -xzf grc-platform-export.tar.gz

# Or download individual files from the sections below
```

---

## File Tree

```
grc-platform/
├── backend/
│   ├── server.py (Main FastAPI application - 600+ lines)
│   ├── seed_data.py (Framework & sample data - 400+ lines)
│   ├── requirements.txt (Python dependencies)
│   └── .env (Environment variables)
├── frontend/
│   ├── src/
│   │   ├── App.js (Main React app with routing)
│   │   ├── App.css (Global styles)
│   │   ├── index.css (Tailwind + fonts)
│   │   ├── index.js (React entry point)
│   │   ├── components/
│   │   │   └── Sidebar.js (Navigation)
│   │   └── pages/
│   │       ├── Dashboard.js (Main dashboard)
│   │       ├── FrameworkManagement.js (Enable/disable frameworks)
│   │       ├── ControlMapping.js (CCF mapping)
│   │       ├── PolicyManagement.js (Policy CRUD)
│   │       ├── ControlTesting.js (Test controls)
│   │       ├── IssueManagement.js (Issue lifecycle)
│   │       ├── RiskManagement.js (Risk + AI suggestions)
│   │       ├── KRIManagement.js (Key Risk Indicators)
│   │       └── KCIManagement.js (Key Control Indicators)
│   ├── package.json (Frontend dependencies)
│   ├── tailwind.config.js (Tailwind configuration)
│   ├── postcss.config.js (PostCSS config)
│   └── .env (Frontend environment variables)
└── README.md
```

---

## Download Links

The complete code archive is available at:
**Location**: `/app/grc-platform-export.tar.gz`

You can download this file using the Emergent file browser or export feature.

---

## All Files Included

### Backend Files (4 files)
1. ✅ server.py - Complete FastAPI application with all endpoints
2. ✅ seed_data.py - 50+ framework controls from ISO 27001, PCI-DSS, SOC2, NIST, GDPR
3. ✅ requirements.txt - All Python dependencies
4. ✅ .env - Environment configuration

### Frontend Files (15+ files)
1. ✅ App.js - Main application with routing
2. ✅ App.css - Global styles
3. ✅ index.css - Tailwind + custom fonts
4. ✅ index.js - React entry point
5. ✅ Sidebar.js - Navigation component
6. ✅ Dashboard.js - Real-time metrics dashboard
7. ✅ FrameworkManagement.js - Framework selection
8. ✅ ControlMapping.js - Control mapping interface
9. ✅ PolicyManagement.js - Policy management
10. ✅ ControlTesting.js - Control testing workflow
11. ✅ IssueManagement.js - Issue lifecycle tracking
12. ✅ RiskManagement.js - Risk management with AI
13. ✅ KRIManagement.js - KRI management
14. ✅ KCIManagement.js - KCI management
15. ✅ package.json - Dependencies
16. ✅ tailwind.config.js - Tailwind setup
17. ✅ .env - Frontend config

---

## Installation Steps

### 1. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup .env file
# Add your MONGO_URL and EMERGENT_LLM_KEY

# Run server
uvicorn server:app --reload --host 0.0.0.0 --port 8001
```

### 2. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install
# or
yarn install

# Setup .env file
# Add your REACT_APP_BACKEND_URL

# Run frontend
npm start
# or
yarn start
```

### 3. Database Setup

- Install MongoDB locally or use MongoDB Atlas
- No schema needed - MongoDB is schemaless
- Data seeds automatically on first load

---

## Key Features Included

✅ **Framework Management** - ISO 27001, PCI-DSS, SOC2, NIST CSF, GDPR
✅ **Control Mapping** - Map Once, Comply Many
✅ **50+ Real Framework Controls** - Actual requirements from standards
✅ **Control Testing** - Pass/Fail with evidence upload
✅ **Issue Management** - Full lifecycle + exceptions
✅ **Risk Management** - AI-powered suggestions (GPT-4o)
✅ **KRI/KCI Tracking** - Dynamic indicator management
✅ **Real-time Dashboard** - Live metrics from actual data
✅ **Evidence Management** - Manual upload + automated collection
✅ **AI Integration** - emergentintegrations library

---

## Technology Stack

**Backend:**
- FastAPI (Python)
- MongoDB
- emergentintegrations (AI)
- Motor (async MongoDB)
- Pydantic (data validation)

**Frontend:**
- React 18
- Tailwind CSS
- Recharts (charts)
- Framer Motion (animations)
- Axios (API calls)
- Shadcn UI (components)
- React Router (navigation)

---

## Environment Variables

### Backend (.env)
```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=grc_database
CORS_ORIGINS=http://localhost:3000
EMERGENT_LLM_KEY=your_emergent_llm_key_here
```

### Frontend (.env)
```env
REACT_APP_BACKEND_URL=http://localhost:8001
```

---

## API Documentation

Once backend is running, visit:
**http://localhost:8001/docs** - FastAPI auto-generated API documentation

---

## Deployment Options

### Option 1: Emergent Native (Easiest)
- Use "Deploy" in Emergent
- 50 credits/month
- Fully managed

### Option 2: Vercel + Railway
- Frontend: Vercel (free tier)
- Backend: Railway/Render (free tier)
- Connect GitHub repo

### Option 3: AWS/DigitalOcean
- Full control
- More setup required
- Best for enterprise

---

## Support & Documentation

- API Docs: http://localhost:8001/docs (auto-generated)
- Frontend: http://localhost:3000
- All code is well-commented and self-explanatory

---

## File Sizes

- Backend: ~50KB total
- Frontend: ~200KB (source code only, excluding node_modules)
- Total: ~250KB of source code
- Archive: ~100KB compressed

---

## License

MIT License - Free to use, modify, and sell

---

**Built with Emergent AI**
Production-ready GRC Platform
