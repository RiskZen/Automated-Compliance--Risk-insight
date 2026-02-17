# GRC Platform - Pure Python Edition

A complete Governance, Risk, and Compliance (GRC) automation platform built with **Reflex** (Pure Python web framework).

## Features

- **5 Compliance Frameworks**: ISO 27001, PCI-DSS, SOC2, NIST, GDPR
- **Map Once, Comply Many**: Unified control framework (CCF)
- **Control Testing**: Record and track control test results
- **Issue Management**: Track issues with lifecycle management
- **Risk Management**: Define and monitor risks
- **KRIs & KCIs**: Key Risk and Control Indicators with thresholds
- **Risk Heatmap**: Visual risk matrix and relationship network
- **AI-Powered**: Risk suggestions via Google Gemini

## Screenshots

### Dashboard
Real-time compliance and risk management overview with key metrics.

### Risk Heatmap
Visual 5x5 risk matrix and Risk → KRI → KCI relationship network.

## Tech Stack

- **Framework**: [Reflex](https://reflex.dev/) (Pure Python)
- **Database**: MongoDB
- **AI**: Google Gemini API

## Quick Start

### Prerequisites

- Python 3.11+
- MongoDB (local or Atlas)
- Google Gemini API key (optional, for AI features)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/grc-platform.git
   cd grc-platform
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your MongoDB URL and API keys
   ```

5. **Seed the database (optional)**
   ```bash
   python seed_data.py
   ```

6. **Run the application**
   ```bash
   reflex run
   ```

7. **Open in browser**
   ```
   http://localhost:3000
   ```

## Configuration

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `MONGO_URL` | MongoDB connection string | `mongodb://localhost:27017` or `mongodb+srv://...` |
| `DB_NAME` | Database name | `grc_reflex_db` |
| `GOOGLE_API_KEY` | Google Gemini API key | `AIza...` |

### MongoDB Atlas Setup

1. Go to [MongoDB Atlas](https://www.mongodb.com/atlas)
2. Create a free cluster
3. Get your connection string
4. Replace `MONGO_URL` in `.env`

### Google Gemini API

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create an API key
3. Add to `GOOGLE_API_KEY` in `.env`

## Project Structure

```
grc-platform/
├── grc_platform/
│   ├── __init__.py
│   ├── grc_platform.py    # Main app with all pages
│   ├── state.py           # State management classes
│   ├── database.py        # MongoDB service
│   └── ai_service.py      # Gemini AI integration
├── assets/
│   └── favicon.ico
├── .env.example           # Environment template
├── .gitignore
├── requirements.txt
├── rxconfig.py            # Reflex configuration
├── seed_data.py           # Database seeding script
└── README.md
```

## Pages

| Page | Route | Description |
|------|-------|-------------|
| Dashboard | `/` | Overview with key metrics |
| Frameworks | `/frameworks` | Enable/disable compliance frameworks |
| Control Mapping | `/controls` | Unified controls with mapping details |
| Policies | `/policies` | Internal policy management |
| Control Testing | `/testing` | Record and track test results |
| Issues | `/issues` | Issue lifecycle management |
| Risks | `/risks` | Risk management with AI suggestions |
| KRIs | `/kris` | Key Risk Indicators |
| KCIs | `/kcis` | Key Control Indicators |
| Risk Heatmap | `/heatmap` | Visual risk matrix and network |

## Deployment

### Reflex Cloud (Recommended)
```bash
reflex deploy
```

### Docker
```bash
docker build -t grc-platform .
docker run -p 3000:3000 grc-platform
```

### Manual
```bash
reflex export
# Deploy the generated files to any static host
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - feel free to use for your own projects!

## Support

For questions or issues, please open a GitHub issue.

---

Built with Reflex - The pure Python web framework
