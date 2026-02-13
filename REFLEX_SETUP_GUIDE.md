# 🚀 GRC Reflex Platform - Complete Setup Guide with Google Gemini

## 📋 Step-by-Step Instructions

### ✅ What You Have Now:
1. Database service (MongoDB integration)
2. AI service (Google Gemini integration)
3. Requirements file
4. Environment template

---

## Step 1: Get Your Google Gemini API Key (FREE)

### 1.1 Go to Google AI Studio:
```
https://makersuite.google.com/app/apikey
```

### 1.2 Sign in with Google Account

### 1.3 Click "Create API Key"
- Choose "Create API key in new project" or select existing project
- Copy the API key (starts with `AIza...`)

### 1.4 Update .env file:
```bash
cd /app/reflex-grc
nano .env  # or use any text editor
```

Replace `your_gemini_api_key_here` with your actual key:
```env
GOOGLE_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXX
```

**💰 Google Gemini Free Tier:**
- ✅ 60 requests per minute
- ✅ 100,000 requests per day
- ✅ FREE forever
- ✅ No credit card required

---

## Step 2: Setup MongoDB

### Option A: MongoDB Atlas (FREE - Recommended)

1. Go to https://mongodb.com/cloud/atlas/register
2. Create free account
3. Create FREE M0 cluster (512MB free forever)
4. Click "Connect" → "Connect your application"
5. Copy connection string
6. Update `.env`:
```env
MONGO_URL=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
DB_NAME=grc_production
```

### Option B: Local MongoDB

```bash
# Install MongoDB
# macOS:
brew install mongodb-community

# Ubuntu:
sudo apt install mongodb

# Start MongoDB
mongod

# Keep .env as:
MONGO_URL=mongodb://localhost:27017
DB_NAME=grc_reflex_db
```

---

## Step 3: Install Dependencies

```bash
cd /app/reflex-grc

# Activate virtual environment
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt
```

---

## Step 4: Seed Sample Data

I'll create a seed script next. Run:
```bash
python seed_data.py
```

This will populate:
- ✅ 5 compliance frameworks
- ✅ 50+ framework controls
- ✅ 10 unified controls
- ✅ 10 internal policies
- ✅ Sample data for testing

---

## Step 5: Run the Application

```bash
# From /app/reflex-grc directory
reflex run
```

This will:
1. Start backend API (port 8000)
2. Start frontend (port 3000)
3. Auto-open browser

**Access at:** `http://localhost:3000`

---

## Step 6: Test Features

### Test AI Features:
1. Go to "Risks" page
2. Click "Get AI Suggestions"
3. Gemini will suggest top 10 risks
4. Click "Use This" to add a risk

### Test Complete Workflow:
1. **Frameworks** → Enable ISO 27001
2. **Control Mapping** → Create unified control
3. **Policies** → Create policy
4. **Control Testing** → Test a control (Pass/Fail)
5. **Issues** → View auto-created issues from failed tests
6. **Risks** → Add risks (manual or AI-suggested)

---

## Step 7: Deploy to Reflex Cloud (FREE)

### 7.1 Login to Reflex:
```bash
reflex login
```

### 7.2 Set Environment Variables:
```bash
reflex env set GOOGLE_API_KEY="your_key_here"
reflex env set MONGO_URL="your_mongodb_atlas_url"
reflex env set DB_NAME="grc_production"
```

### 7.3 Deploy:
```bash
reflex deploy
```

Follow prompts:
- Choose region
- Confirm deployment
- Get your free `.reflex.run` URL

### 7.4 Access Your Live App:
```
https://your-app-name.reflex.run
```

---

## Step 8: Deploy to GitHub Codespaces

### 8.1 Push to GitHub:
```bash
# Initialize git
git init
git add .
git commit -m "GRC Reflex Platform with Gemini AI"

# Create repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/grc-reflex.git
git push -u origin main
```

### 8.2 Create Codespace:
1. Go to your GitHub repo
2. Click **Code** → **Codespaces** → **Create codespace**
3. Wait 2-3 minutes for setup

### 8.3 Run in Codespace:
```bash
pip install -r requirements.txt
reflex run
```

Codespace will auto-forward port 3000.

---

## 🔧 Configuration

### Update rxconfig.py:
```python
import reflex as rx

config = rx.Config(
    app_name="reflex_grc",
    port=3000,
    api_url="http://localhost:8000",
)
```

---

## 🎯 Google Gemini Integration Details

### Features Using Gemini AI:

1. **Risk Suggestions**
   - Get top 10 risks for any industry
   - AI-generated descriptions
   - Intelligent risk scoring

2. **Risk-KRI Analysis**
   - Analyze effectiveness of risk indicators
   - Recommendations for improvements

3. **Control Health Impact**
   - Analyze how control health affects risk
   - Prioritize control improvements

### Gemini API Usage:
```python
# In your code (already integrated):
from reflex_grc.ai_service import ai_service

# Get risk suggestions
risks = await ai_service.get_risk_suggestions("Healthcare")

# Analyze risk-KRI
analysis = await ai_service.analyze_risk_kri(context)

# Analyze control health
analysis = await ai_service.analyze_control_health(context)
```

---

## 🐛 Troubleshooting

### Issue: "No module named 'google.generativeai'"
```bash
pip install google-generativeai
```

### Issue: "Invalid API key"
- Check your API key in .env
- Ensure no spaces or quotes
- Get new key from https://makersuite.google.com/app/apikey

### Issue: "MongoDB connection failed"
```bash
# For Atlas: Check connection string
# For local: Ensure mongod is running
mongod --version
```

### Issue: "Port 3000 already in use"
```bash
lsof -ti:3000 | xargs kill -9
reflex run
```

---

## 📊 Next Files I'm Creating:

1. ✅ Database service (DONE)
2. ✅ AI service with Gemini (DONE)
3. ⏳ Main app file
4. ⏳ Dashboard page
5. ⏳ Framework management page
6. ⏳ Control mapping page
7. ⏳ Policy management page
8. ⏳ Control testing page
9. ⏳ Issue management page
10. ⏳ Risk management page (with AI suggestions)
11. ⏳ KRI/KCI pages
12. ⏳ Seed data script

---

## 💰 Total Cost

**FREE Everything:**
- ✅ Google Gemini API: FREE (60 req/min)
- ✅ MongoDB Atlas: FREE (512MB)
- ✅ Reflex Cloud: FREE (.reflex.run domain)
- ✅ GitHub Codespaces: FREE (60 hours/month)

**Total: $0/month** 🎉

---

**Next: I'll continue creating all the Reflex pages! Let me know when you're ready.**
