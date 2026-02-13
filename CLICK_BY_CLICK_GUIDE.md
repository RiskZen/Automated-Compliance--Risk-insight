# 🚀 GRC Reflex Platform - Cloud-Only Setup (No Local Installation)

## ⚠️ IMPORTANT: You Need ZERO Local Software
Everything is done in your browser. No Python, no Git, nothing on your computer!

---

## 📱 Step 1: Get Google Gemini API Key (5 minutes)

### 1.1 Get Your FREE Gemini Key:

**Action 1:** Open new browser tab → Go to:
```
https://makersuite.google.com/app/apikey
```

**Action 2:** Click **"Get API key"** button (top right)

**Action 3:** Click **"Create API key in new project"**

**Action 4:** Wait 5 seconds

**Action 5:** You'll see your key (starts with `AIza...`)

**Action 6:** Click **"Copy"** button

**Action 7:** Paste in a notepad - you'll need this later
```
Example: AIzaSyBXXXXXXXXXXXXXXXXXXXXXXX
```

✅ **Done! You have your Gemini key**

---

## 📁 Step 2: Create GitHub Repository (3 minutes)

### 2.1 Create Repo:

**Action 1:** Open new tab → Go to:
```
https://github.com/new
```

**Action 2:** Fill in:
- Repository name: `grc-reflex-platform`
- Description: `AI-Powered GRC Platform in Pure Python`
- **Click** the "Public" radio button
- **Check** "Add a README file"

**Action 3:** Click **"Create repository"** button (green button at bottom)

**Action 4:** Wait 3 seconds - Your repo is created!

✅ **Done! Repo created**

---

## 💻 Step 3: Open GitHub Codespaces (2 minutes)

### 3.1 Launch Cloud Development Environment:

**Action 1:** On your new repo page, click the **"Code"** button (green button, top right)

**Action 2:** Click **"Codespaces"** tab

**Action 3:** Click **"Create codespace on main"** button

**Action 4:** Wait 1-2 minutes while it loads

**Action 5:** You'll see VS Code in your browser!

✅ **Done! You're now coding in the cloud**

---

## 🛠️ Step 4: Setup Project (5 minutes)

### 4.1 Open Terminal in Codespace:

**Action 1:** Look at bottom of VS Code → You'll see "TERMINAL" tab

**Action 2:** If no terminal, click **Terminal** menu (top) → **New Terminal**

### 4.2 Install Reflex:

**Action 3:** Copy this command and paste in terminal:
```bash
pip install reflex pymongo python-dotenv google-generativeai motor
```

**Action 4:** Press **Enter**

**Action 5:** Wait 30 seconds while it installs

✅ **You'll see: Successfully installed reflex...**

### 4.3 Initialize Reflex:

**Action 6:** Copy and paste:
```bash
reflex init --template blank
```

**Action 7:** Press **Enter**

**Action 8:** When asked "App name:", type: `grc_platform`

**Action 9:** Press **Enter**

✅ **You'll see: Initializing the app directory... Success!**

---

## 📝 Step 5: Create Configuration Files (5 minutes)

### 5.1 Create .env File:

**Action 1:** Click **"File"** menu (top left) → **"New File"**

**Action 2:** Name it: `.env`

**Action 3:** Copy this and paste in the file:
```env
GOOGLE_API_KEY=PASTE_YOUR_KEY_HERE
MONGO_URL=mongodb+srv://demo:demo@cluster.mongodb.net/
DB_NAME=grc_platform
```

**Action 4:** Replace `PASTE_YOUR_KEY_HERE` with the Gemini key you copied earlier

**Action 5:** Press **Ctrl+S** (or Cmd+S on Mac) to save

### 5.2 Create requirements.txt:

**Action 6:** Create new file → Name it: `requirements.txt`

**Action 7:** Paste this:
```
reflex>=0.6.0
pymongo>=4.5.0
motor>=3.3.1
python-dotenv>=1.0.0
google-generativeai>=0.3.0
```

**Action 8:** Save (Ctrl+S)

---

## 🎯 Step 6: I'll Provide All Code Files

### What I'm Creating for You:

I'll create these files with complete code:

**Core Files:**
1. `grc_platform/grc_platform.py` - Main app
2. `grc_platform/state.py` - State management
3. `grc_platform/database.py` - MongoDB integration
4. `grc_platform/ai_service.py` - Gemini AI

**Pages (All in Pure Python):**
5. Dashboard
6. Framework Management
7. Control Mapping  
8. Policy Management
9. Control Testing
10. Issue Management
11. Risk Management (with AI)
12. KRI Management
13. KCI Management

**Helper:**
14. `seed_data.py` - Sample data

---

## 🚀 Step 7: Run Your App (After I Create Files)

### In Codespace Terminal:

**Action 1:** Copy and paste:
```bash
reflex run
```

**Action 2:** Press **Enter**

**Action 3:** Wait 30 seconds

**Action 4:** You'll see popup: "Your application is available on port 3000"

**Action 5:** Click **"Open in Browser"**

✅ **Your GRC app is running!**

---

## 🌐 Step 8: Deploy to Reflex Cloud (FREE Forever)

### 8.1 Login to Reflex:

**Action 1:** In Codespace terminal, paste:
```bash
reflex login
```

**Action 2:** Press **Enter**

**Action 3:** Browser will open → Login with GitHub

**Action 4:** Click **"Authorize"**

**Action 5:** Go back to Codespace terminal

### 8.2 Set Environment Variables:

**Action 6:** Paste this (replace with YOUR keys):
```bash
reflex env set GOOGLE_API_KEY="AIzaSy..." MONGO_URL="mongodb+srv://..." DB_NAME="grc_platform"
```

**Action 7:** Press **Enter**

### 8.3 Deploy:

**Action 8:** Paste:
```bash
reflex deploy
```

**Action 9:** Press **Enter**

**Action 10:** When asked "Choose region", type: `us-west` (or closest to you)

**Action 11:** When asked "Confirm?", type: `y`

**Action 12:** Wait 2-3 minutes

**Action 13:** You'll see: "Deployed successfully at https://your-app.reflex.run"

✅ **Your app is LIVE on the internet!**

---

## 🎉 Step 9: Access Your Live App

**Action 1:** Copy the URL from deploy output:
```
https://your-app-name.reflex.run
```

**Action 2:** Open in browser

**Action 3:** Share with anyone - it's public!

---

## 📊 Summary of What You Get:

**Your Cloud Setup:**
- ✅ Code on GitHub (backup + version control)
- ✅ Development in Codespaces (no local install needed)
- ✅ App live on Reflex Cloud (free .reflex.run domain)
- ✅ MongoDB Atlas (free 512MB database)
- ✅ Google Gemini AI (free 100k requests/day)

**Total Cost: $0/month** 🎉

---

## 🔄 Step 10: Update Your App Later

### From Codespaces:

**Action 1:** Make code changes

**Action 2:** In terminal:
```bash
git add .
git commit -m "Updated feature X"
git push
```

**Action 3:** Deploy new version:
```bash
reflex deploy
```

**Action 4:** Wait 2 minutes → Updated live!

---

## 📍 Where Are You Now:

✅ You have Gemini API key
✅ Instructions ready
⏳ Waiting for me to create all the Reflex code files

**Next: I'll create all 14 files with complete GRC platform code in pure Python!**

Say "create all files" and I'll generate the complete application! 🚀
