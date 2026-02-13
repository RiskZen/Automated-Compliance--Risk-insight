# 🐍 GRC Platform - Pure Python (Reflex) Deployment Guide

## 📋 Complete Step-by-Step Guide

### What We're Building:
A **complete GRC platform in pure Python** using Reflex framework - No JavaScript needed!

### Deployment Options (Both FREE):
1. ✅ **Reflex Cloud** - Free tier (Recommended - Easiest)
2. ✅ **GitHub Codespaces** - Free 60 hours/month

---

## 🚀 Step 1: Local Development Setup

### Prerequisites:
- Python 3.9+
- Git
- GitHub account (free)

### Install Reflex & Create Project:

```bash
# Create new directory
mkdir grc-reflex-app
cd grc-reflex-app

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install Reflex
pip install reflex pymongo python-dotenv motor

# Initialize Reflex project
reflex init
```

---

## 📁 Step 2: Project Structure

```
grc-reflex-app/
├── grc_reflex_app/
│   ├── __init__.py
│   ├── grc_reflex_app.py (Main app file)
│   ├── pages/
│   │   ├── dashboard.py
│   │   ├── frameworks.py
│   │   ├── controls.py
│   │   ├── testing.py
│   │   └── risks.py
│   ├── components/
│   │   └── sidebar.py
│   └── state.py (State management)
├── assets/ (CSS, images)
├── rxconfig.py (Reflex configuration)
├── requirements.txt
└── .env
```

---

## 🛠️ Step 3: Build the Application

I'll create all the files for you in the next step. The complete Reflex GRC platform includes:

✅ Dashboard with real-time metrics
✅ Framework management
✅ Control mapping
✅ Control testing
✅ Issue management
✅ Risk management with AI
✅ All features in pure Python!

---

## 🌐 Step 4: Deploy to Reflex Cloud (FREE - Easiest)

### 4.1 Create Reflex Account:
```bash
# Install Reflex CLI
pip install reflex

# Login to Reflex
reflex login
```

### 4.2 Deploy:
```bash
# From your project directory
reflex deploy

# Follow the prompts:
# - Choose region (closest to you)
# - Confirm deployment
# - Get your free .reflex.run URL
```

### 4.3 Your App Will Be Live At:
```
https://your-app-name.reflex.run
```

**Free Tier Includes:**
- Custom subdomain
- HTTPS automatically
- Unlimited visitors
- Auto-scaling

---

## 💻 Step 5: Deploy to GitHub Codespaces (Alternative)

### 5.1 Push to GitHub:

```bash
# Initialize git
git init

# Create .gitignore
cat > .gitignore << EOF
venv/
__pycache__/
*.pyc
.env
.web/
EOF

# Commit code
git add .
git commit -m "Initial commit - Reflex GRC Platform"

# Create GitHub repo and push
# (Do this on GitHub.com first, then:)
git remote add origin https://github.com/YOUR_USERNAME/grc-reflex.git
git branch -M main
git push -u origin main
```

### 5.2 Create Codespace:

1. Go to your GitHub repo
2. Click **"Code"** → **"Codespaces"** → **"Create codespace on main"**
3. Wait for environment to load (2-3 minutes)

### 5.3 Run in Codespace:

```bash
# Codespace opens automatically in VS Code in browser
# In terminal:
pip install -r requirements.txt
reflex run

# Forward port 3000 (Codespaces does this automatically)
# Access your app at the forwarded URL
```

**Free Codespaces:**
- 60 hours/month free
- 2 concurrent codespaces
- Perfect for development

---

## 🔧 Step 6: Configuration

### Environment Variables:

Create `.env` file:
```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=grc_database
REFLEX_APP_NAME=grc-platform
```

### For Production (Reflex Cloud):

```bash
# Set environment variables
reflex env set MONGO_URL="your_mongodb_atlas_url"
reflex env set DB_NAME="grc_production"
```

---

## 📊 Step 7: Connect MongoDB

### Option 1: MongoDB Atlas (FREE - Recommended for Production)

1. Go to https://mongodb.com/cloud/atlas
2. Create free account
3. Create free cluster (M0 - Free Forever)
4. Get connection string
5. Add to your .env file

```env
MONGO_URL=mongodb+srv://username:password@cluster.mongodb.net/
```

### Option 2: Local MongoDB (Development)

```bash
# Install MongoDB locally
# macOS
brew install mongodb-community

# Ubuntu
sudo apt install mongodb

# Start MongoDB
mongod
```

---

## 🎨 Step 8: Customize Your App

### Update rxconfig.py:

```python
import reflex as rx

config = rx.Config(
    app_name="grc_reflex_app",
    port=3000,
    api_url="http://localhost:8000",
    deploy_url="https://your-app.reflex.run",
)
```

---

## ✅ Step 9: Test Everything

### Local Testing:
```bash
reflex run
```

### Production Testing:
```bash
# After deploying to Reflex Cloud
# Visit your .reflex.run URL
```

---

## 🚀 Quick Commands Cheat Sheet

### Development:
```bash
reflex run          # Run development server
reflex run --loglevel debug  # Debug mode
reflex db migrate   # Run database migrations
```

### Deployment:
```bash
reflex login        # Login to Reflex Cloud
reflex deploy       # Deploy to production
reflex deployments list  # View deployments
reflex logs         # View production logs
```

### Git:
```bash
git add .
git commit -m "Update message"
git push
```

---

## 💰 Cost Breakdown

### FREE Options:

**Reflex Cloud Free Tier:**
- ✅ FREE forever
- ✅ 1 app
- ✅ .reflex.run subdomain
- ✅ Auto HTTPS
- ✅ Unlimited traffic

**GitHub Codespaces:**
- ✅ 60 hours/month FREE
- ✅ Perfect for development

**MongoDB Atlas:**
- ✅ 512MB FREE forever
- ✅ Shared cluster

**Total Monthly Cost: $0** 🎉

---

## 🎯 What's Next After Deployment?

1. ✅ Custom domain (upgrade Reflex plan)
2. ✅ Add authentication
3. ✅ Connect real AI key
4. ✅ Scale with Reflex Pro ($19/month for unlimited apps)

---

## 📚 Resources

- Reflex Docs: https://reflex.dev/docs
- Reflex Gallery: https://reflex.dev/gallery
- MongoDB Atlas: https://mongodb.com/cloud/atlas
- GitHub Codespaces: https://github.com/features/codespaces

---

## 🆘 Troubleshooting

### Issue: "reflex: command not found"
```bash
pip install --upgrade reflex
```

### Issue: "Port 3000 already in use"
```bash
# Kill existing process
lsof -ti:3000 | xargs kill -9
```

### Issue: MongoDB connection failed
```bash
# Check MongoDB is running
mongod --version
```

---

## 🎉 Success!

Once deployed, your GRC platform will be live at:
- **Reflex Cloud**: `https://your-app-name.reflex.run`
- **Codespaces**: `https://random-name.app.github.dev`

**Now let me create all the Reflex code files for you!** 🚀
