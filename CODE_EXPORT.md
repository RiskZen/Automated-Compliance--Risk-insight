# GRC Platform - Complete Code Export

## Project Structure

```
grc-platform/
├── backend/
│   ├── server.py
│   ├── seed_data.py
│   ├── requirements.txt
│   ├── .env
│   └── uploads/
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Sidebar.js
│   │   │   └── ui/ (shadcn components)
│   │   ├── pages/
│   │   │   ├── Dashboard.js
│   │   │   ├── FrameworkManagement.js
│   │   │   ├── ControlMapping.js
│   │   │   ├── PolicyManagement.js
│   │   │   ├── ControlTesting.js
│   │   │   ├── IssueManagement.js
│   │   │   ├── RiskManagement.js
│   │   │   ├── KRIManagement.js
│   │   │   └── KCIManagement.js
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.css
│   ├── package.json
│   ├── tailwind.config.js
│   ├── .env
│   └── craco.config.js
└── README.md
```

## Installation Instructions

### Backend Setup

1. Install Python 3.9+
2. Create virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Setup MongoDB:
   - Install MongoDB locally or use MongoDB Atlas
   - Update MONGO_URL in .env

5. Run backend:
```bash
uvicorn server:app --reload --host 0.0.0.0 --port 8001
```

### Frontend Setup

1. Install Node.js 16+
2. Install dependencies:
```bash
cd frontend
npm install
# or
yarn install
```

3. Update .env with your backend URL

4. Run frontend:
```bash
npm start
# or
yarn start
```

### Environment Variables

**Backend (.env):**
```
MONGO_URL=mongodb://localhost:27017
DB_NAME=grc_database
CORS_ORIGINS=http://localhost:3000
EMERGENT_LLM_KEY=your_key_here
```

**Frontend (.env):**
```
REACT_APP_BACKEND_URL=http://localhost:8001
```

## Features

- ✅ 5 Compliance Frameworks (ISO 27001, PCI-DSS, SOC2, NIST CSF, GDPR)
- ✅ 50+ Real Framework Controls
- ✅ Unified Control Framework (Map Once, Comply Many)
- ✅ Control Testing with Pass/Fail
- ✅ Manual Evidence Upload + Automated Collection
- ✅ Issue Management with Lifecycle
- ✅ Exception Management
- ✅ Risk Management with AI Suggestions
- ✅ KRI/KCI Management
- ✅ Dynamic Risk→KRI→KCI→Control Mapping
- ✅ Real-time Dashboard

## Tech Stack

### Backend
- FastAPI
- MongoDB
- emergentintegrations (GPT-4o AI)
- Motor (async MongoDB)
- Pydantic

### Frontend
- React
- Tailwind CSS
- Recharts
- Framer Motion
- Axios
- Shadcn UI

## API Endpoints

### Frameworks
- GET /api/frameworks
- POST /api/frameworks
- PATCH /api/frameworks/{id}/toggle

### Controls
- GET /api/unified-controls
- POST /api/unified-controls
- GET /api/framework-controls/{framework_id}

### Policies
- GET /api/policies
- POST /api/policies

### Control Testing
- GET /api/control-tests
- POST /api/control-tests

### Evidence
- GET /api/evidence
- POST /api/evidence/upload
- POST /api/evidence/automated

### Issues
- GET /api/issues
- POST /api/issues
- PATCH /api/issues/{id}/status
- PATCH /api/issues/{id}/exception

### Risk Management
- GET /api/risks
- POST /api/risks
- POST /api/risks/ai-suggest

### KRI/KCI
- GET /api/kris
- POST /api/kris
- GET /api/kcis
- POST /api/kcis

### Dashboard
- GET /api/dashboard/stats

### Data Seeding
- POST /api/seed-production-data

## Deployment

### Using Vercel (Frontend)
1. Connect GitHub repo to Vercel
2. Set environment variables
3. Deploy

### Using Railway/Render (Backend)
1. Connect GitHub repo
2. Set environment variables
3. Deploy

### Using Emergent Native
- Use "Deploy" feature in Emergent
- 50 credits/month
- Custom domain support

## License

MIT License - Free to use and modify

## Support

For questions or issues, contact your development team.

---

**Built with Emergent AI** - Production-Ready GRC Platform
