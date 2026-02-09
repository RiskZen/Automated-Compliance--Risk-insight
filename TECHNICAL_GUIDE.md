# GRC Intelligence Platform - Technical Implementation Guide

## Architecture Overview

### System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Frontend (React)                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  Dashboard   │  │     Risk     │  │   Control    │          │
│  │              │  │ Intelligence │  │   Mapping    │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│                                                                   │
│  ┌──────────────────────────────────────────────────┐          │
│  │         Recharts (Visualization)                  │          │
│  │         Framer Motion (Animations)                │          │
│  └──────────────────────────────────────────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                              ↕ HTTPS/REST
┌─────────────────────────────────────────────────────────────────┐
│                      Backend (FastAPI)                           │
│  ┌──────────────────────────────────────────────────┐          │
│  │              API Router (/api)                    │          │
│  │  • /risks      • /controls    • /kris            │          │
│  │  • /kcis       • /evidence    • /ai/analyze      │          │
│  └──────────────────────────────────────────────────┘          │
│                                                                   │
│  ┌──────────────────────────────────────────────────┐          │
│  │        AI Service (emergentintegrations)          │          │
│  │               GPT-4o Integration                  │          │
│  └──────────────────────────────────────────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                              ↕
┌─────────────────────────────────────────────────────────────────┐
│                      MongoDB Database                            │
│  • risks        • controls      • kris                          │
│  • kcis         • evidence                                      │
└─────────────────────────────────────────────────────────────────┘
```

## Backend Implementation

### Database Schema

#### Risks Collection
```python
{
    "id": "r1",                          # UUID
    "name": "Data Breach",
    "description": "Unauthorized access...",
    "category": "Cybersecurity",
    "inherent_risk_score": 8.5,         # Before controls
    "residual_risk_score": 4.2,         # After controls
    "status": "Active",
    "owner": "CISO",
    "kris": ["kri1", "kri2"],           # Linked KRIs
    "linked_controls": ["c1", "c2"],    # Linked Controls
    "ai_insights": "High priority...",
    "created_at": "2026-01-15T10:00:00Z"
}
```

#### Controls Collection
```python
{
    "id": "c1",
    "name": "Multi-Factor Authentication",
    "description": "Enforce MFA...",
    "ccf_id": "CCF-AC-001",             # Common Control Framework ID
    "internal_policy": "POL-SEC-100",   # Internal policy reference
    "control_type": "Preventive",       # Preventive/Detective/Corrective
    "frequency": "Continuous",
    "owner": "IT Security",
    "health_score": 92.0,               # 0-100 effectiveness score
    "status": "Effective",
    "linked_risks": ["r1"],
    "kcis": ["kci1"],                   # Linked KCIs
    "last_tested": "2026-01-10",
    "created_at": "2026-01-15T10:00:00Z"
}
```

#### KRIs Collection (Key Risk Indicators)
```python
{
    "id": "kri1",
    "name": "Failed Login Attempts",
    "description": "Number of failed logins per hour",
    "risk_id": "r1",                    # Links to risk
    "current_value": 45.0,
    "threshold": 100.0,                 # Alert threshold
    "status": "Normal",                 # Normal/Warning/Critical
    "trend": "Stable",                  # Increasing/Decreasing/Stable
    "created_at": "2026-01-15T10:00:00Z"
}
```

#### KCIs Collection (Key Control Indicators)
```python
{
    "id": "kci1",
    "name": "MFA Adoption Rate",
    "description": "Percentage of users with MFA enabled",
    "kri_id": "kri1",                   # Links to KRI
    "control_id": "c1",                 # Links to control
    "current_value": 98.0,
    "target": 100.0,
    "status": "On Track",
    "created_at": "2026-01-15T10:00:00Z"
}
```

#### Evidence Collection
```python
{
    "id": "e1",
    "control_id": "c1",
    "evidence_type": "Log Report",
    "description": "MFA enrollment logs",
    "collected_at": "2026-01-15T10:00:00Z",
    "automated": True,                  # Automated vs manual
    "status": "Collected"
}
```

### API Endpoints

#### Data CRUD Operations
```
GET  /api/risks          - List all risks
POST /api/risks          - Create new risk
GET  /api/controls       - List all controls
POST /api/controls       - Create new control
GET  /api/kris           - List all KRIs
POST /api/kris           - Create new KRI
GET  /api/kcis           - List all KCIs
POST /api/kcis           - Create new KCI
GET  /api/evidence       - List all evidence
POST /api/evidence       - Create new evidence
POST /api/seed-data      - Seed sample data
```

#### AI Analysis Endpoint
```
POST /api/ai/analyze

Request Body:
{
    "analysis_type": "control_health_impact",  // or "risk_kri_mapping" or "ccf_mapping"
    "context": {
        "risk": {...},
        "controls": [...],
        "kris": [...],
        "kcis": [...]
    }
}

Response:
{
    "analysis": "AI-generated analysis text",
    "recommendations": [
        "Recommendation 1",
        "Recommendation 2",
        ...
    ]
}
```

### AI Integration

#### emergentintegrations Library Usage
```python
from emergentintegrations.llm.chat import LlmChat, UserMessage

async def get_ai_analysis(prompt: str) -> str:
    chat = LlmChat(
        api_key=os.environ.get('EMERGENT_LLM_KEY'),
        session_id=str(uuid.uuid4()),
        system_message="You are a GRC expert..."
    ).with_model("openai", "gpt-4o")
    
    user_message = UserMessage(text=prompt)
    response = await chat.send_message(user_message)
    return response
```

#### AI Analysis Types

1. **Control Health Impact Analysis**
   - Input: Risk data + Control health scores
   - Output: Quantified impact analysis + recommendations
   - Use case: Understanding how control effectiveness reduces risk

2. **Risk-KRI-KCI Mapping Analysis**
   - Input: Risk + linked KRIs + linked KCIs
   - Output: Effectiveness analysis of indicators + recommendations
   - Use case: Optimizing risk monitoring and control measurement

3. **CCF Framework Mapping Analysis**
   - Input: Control + CCF ID + Internal Policy
   - Output: Framework coverage analysis + gap identification
   - Use case: "Map Once, Comply Many" optimization

## Frontend Implementation

### Component Structure

```
src/
├── App.js                          # Main app with routing & context
├── App.css                         # Global styles
├── index.css                       # Tailwind + custom fonts
├── components/
│   ├── Sidebar.js                  # Navigation sidebar
│   └── ui/                         # Shadcn UI components
└── pages/
    ├── Dashboard.js                # Main dashboard
    ├── RiskIntelligence.js         # Risk-KRI-KCI analysis
    ├── ControlMapping.js           # CCF mapping
    └── EvidenceCollection.js       # Evidence tracking
```

### State Management

Using React Context API:
```javascript
export const AppContext = React.createContext();

// Context provides:
{
    risks: [],          // All risks
    controls: [],       // All controls
    kris: [],          // All KRIs
    kcis: [],          // All KCIs
    evidence: [],      // All evidence
    loading: false,    // Loading state
    refreshData: fn,   // Refresh function
    API: string        // API base URL
}
```

### Data Visualization

#### Recharts Components Used
1. **LineChart**: Risk score trend over time
2. **BarChart**: 
   - Risk-KRI-KCI mapping visualization
   - Control health impact on risk
3. **PieChart**: Risk distribution by category

#### Framer Motion Animations
- Page transitions: `initial`, `animate`, `transition`
- Staggered card animations: Delay-based entrance
- Hover effects: Scale and shadow transitions

### Design System

#### Typography
- **Headings**: Outfit (Google Fonts)
- **Body**: Plus Jakarta Sans (Google Fonts)
- **Code/Data**: JetBrains Mono (Google Fonts)

#### Color Palette
```css
Primary: #0f172a (Slate 900)
Secondary: #f1f5f9 (Slate 100)
Accent: #3b82f6 (Blue 500)
Success: #10b981 (Green 500)
Warning: #f59e0b (Amber 500)
Danger: #ef4444 (Red 500)
Background: #f8fafc (Slate 50)
```

## Key Features Implementation

### 1. Dynamic Risk Scoring

**Concept**: Control health automatically affects risk scores

```python
# Backend calculates:
risk_reduction = (inherent_score - residual_score) / inherent_score * 100

# AI analyzes:
- Average control health for risk
- Correlation between control health and risk score
- Recommendations to improve control effectiveness
```

**Frontend displays**:
- Visualization showing higher control health = lower risk scores
- Real-time updates when control health changes

### 2. Map Once, Comply Many

**Implementation**:
1. Each control has unique CCF ID (e.g., CCF-AC-001)
2. Control maps to internal policy (e.g., POL-SEC-100)
3. AI analyzes control coverage across frameworks:
   - ISO 27001
   - SOC 2
   - GDPR
   - NIST CSF
   - PCI-DSS

**Value**: Define control once, automatically satisfy requirements across 5+ frameworks

### 3. Automated Evidence Collection

**Tracking**:
- `automated: true/false` flag on each evidence item
- Calculate automation rate: `automated_count / total_count * 100`

**AI Recommendations**:
- Identifies manual evidence that could be automated
- Suggests API integrations for automatic collection
- Prioritizes automation opportunities by impact

### 4. Risk-KRI-KCI Relationships

**Data Structure**:
```
Risk (Data Breach)
  ├── KRI (Failed Login Attempts)
  │     └── KCI (MFA Adoption Rate)
  │           └── Control (Multi-Factor Authentication)
  └── KRI (Data Access Violations)
        └── KCI (Encryption Coverage)
              └── Control (Encryption at Rest)
```

**Dynamic Updates**:
- KCI measures control effectiveness
- KRI monitors risk indicators
- AI analyzes relationships and effectiveness
- Recommendations to optimize monitoring

## Testing Strategy

### Backend Testing
```bash
# Test API endpoints
curl -X GET "https://your-app.com/api/risks"
curl -X POST "https://your-app.com/api/ai/analyze" \
  -H "Content-Type: application/json" \
  -d '{"analysis_type": "control_health_impact", "context": {...}}'
```

### Frontend Testing
- Component rendering tests
- User interaction tests (AI button clicks)
- Navigation tests
- Data visualization tests

### Integration Testing
- End-to-end user flows
- AI analysis response handling
- Real-time data updates

## Deployment

### Environment Variables

**Backend (.env)**:
```
MONGO_URL=mongodb://localhost:27017
DB_NAME=grc_database
CORS_ORIGINS=*
EMERGENT_LLM_KEY=sk-emergent-xxxxx
```

**Frontend (.env)**:
```
REACT_APP_BACKEND_URL=https://your-backend-url.com
```

### Production Considerations

1. **Database**: MongoDB Atlas for production
2. **API Keys**: Secure storage for EMERGENT_LLM_KEY
3. **CORS**: Restrict to specific origins
4. **Rate Limiting**: On AI analysis endpoints
5. **Caching**: Cache AI responses for identical queries
6. **Monitoring**: Track AI usage and costs

## Performance Optimization

### Backend
- Database indexing on frequently queried fields
- Async operations for AI calls
- Batch operations for bulk data

### Frontend
- Lazy loading for charts
- Memoization for expensive calculations
- Debouncing for search/filter operations

## Security

### Data Protection
- No sensitive data in URLs
- API authentication (implement JWT tokens)
- Input validation on all endpoints
- MongoDB injection prevention (using Pydantic models)

### AI Security
- Prompt injection prevention
- Rate limiting on AI endpoints
- Response validation before displaying

## Future Enhancements

### Phase 1 (Next Steps)
1. User authentication (JWT-based)
2. Role-based access control (Admin, Analyst, Viewer)
3. Export functionality (PDF reports)
4. Email notifications for KRI threshold breaches

### Phase 2 (Advanced Features)
1. Predictive risk modeling
2. Integration with SIEM tools
3. Automated remediation workflows
4. Board-level executive dashboards
5. Mobile app for executives

### Phase 3 (Enterprise)
1. Multi-tenant architecture
2. Advanced analytics and reporting
3. Integration marketplace
4. Custom framework definitions
5. Compliance certification tracking

---

## Quick Start Guide

### 1. Start the Application
```bash
# Backend automatically starts via supervisor
# Frontend automatically starts via supervisor
# MongoDB automatically starts via supervisor

# Check status
sudo supervisorctl status
```

### 2. Access the Platform
```
Dashboard: http://localhost:3000
API Docs: http://localhost:8001/docs (FastAPI auto-generated)
```

### 3. Seed Sample Data
```bash
# Data automatically seeds on first load
# Or manually trigger:
curl -X POST "http://localhost:8001/api/seed-data"
```

### 4. Test AI Features
- Navigate to Risk Intelligence
- Click "Analyze KRI-KCI Mapping" on any risk
- View AI-generated analysis and recommendations

---

## Troubleshooting

### Backend Issues
```bash
# Check backend logs
tail -f /var/log/supervisor/backend.err.log

# Restart backend
sudo supervisorctl restart backend
```

### Frontend Issues
```bash
# Check frontend logs
tail -f /var/log/supervisor/frontend.err.log

# Restart frontend
sudo supervisorctl restart frontend
```

### MongoDB Issues
```bash
# Check MongoDB status
sudo supervisorctl status mongodb

# Connect to MongoDB
mongosh mongodb://localhost:27017
```

---

*Technical Implementation Guide - GRC Intelligence Platform*
