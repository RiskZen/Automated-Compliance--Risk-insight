# 📦 ALL CODE FILES - COPY THESE TO YOUR CODESPACE

## 🎯 IMPORTANT: Follow EXACT_DEPLOYMENT_STEPS.md First!

Once you're in Codespace (Step 4 complete), come back here and copy these files.

---

## FILE 1: requirements.txt

**Create file:** `requirements.txt`
**Copy this:**

```
reflex>=0.6.0
pymongo>=4.5.0
motor>=3.3.1
python-dotenv>=1.0.0
google-generativeai>=0.3.0
```

**Save:** Ctrl+S

---

## FILE 2: .env

**Create file:** `.env`
**Copy this (REPLACE with your Gemini key!):**

```env
GOOGLE_API_KEY=AIzaSyXXXXXXXXXXXX
MONGO_URL=mongodb+srv://demo:demo@cluster.mongodb.net/
DB_NAME=grc_platform
```

**Save:** Ctrl+S

---

## FILE 3: rxconfig.py

**Create file:** `rxconfig.py`
**Copy this:**

```python
import reflex as rx

config = rx.Config(
    app_name=\"grc_platform\",
    db_url=\"sqlite:///reflex.db\",
)
```

**Save:** Ctrl+S

---

##📁 FILES ALREADY CREATED:

All code files are in `/app/reflex-grc/` directory:

✅ `grc_platform/grc_platform.py` - Main app (Dashboard, Frameworks, Policies, Risks pages)
✅ `grc_platform/state.py` - State management
✅ `grc_platform/database.py` - MongoDB integration  
✅ `grc_platform/ai_service.py` - Google Gemini AI
✅ `requirements.txt` - Dependencies

---

## 🚀 QUICK COMMANDS FOR CODESPACE:

### After creating files above, run:

```bash
# Install dependencies
pip install -r requirements.txt

# Initialize database (auto-creates sample data)
reflex db init

# Run app
reflex run
```

**Then click "Open in Browser" when popup appears!**

---

## 🌐 TO DEPLOY:

```bash
# Login
reflex login

# Deploy
reflex deploy
```

**Your app will be live at:** `https://your-app.reflex.run`

---

## 📊 What Works:

✅ Dashboard with real-time metrics
✅ Framework Management (Enable/Disable)
✅ Control Mapping (Create unified controls)
✅ Policy Management (Create policies)
✅ Risk Management with AI suggestions from Gemini
✅ Beautiful UI in pure Python!

---

## 🎯 Files Location:

All complete code files are ready at:
`/app/reflex-grc/`

You can:
1. Download from Emergent file browser
2. Or copy-paste each file manually into Codespace

---

**Next Steps:**
1. Follow `/app/EXACT_DEPLOYMENT_STEPS.md` 
2. Copy files to Codespace
3. Run `reflex run`
4. Deploy with `reflex deploy`

**That's it! Your GRC platform will be live! 🚀**
