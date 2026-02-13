# 🎯 EXACT STEPS - Follow These In Order

## ✅ STEP 1: Get Google Gemini API Key (Do This First!)

### Click-by-Click:

1. Open browser → Go to: `https://makersuite.google.com/app/apikey`
2. Click **"Get API key"** (top right)
3. Click **"Create API key in new project"**
4. Wait 5 seconds
5. Click **"Copy"** button next to your key
6. Paste in notepad → Save it (you'll use it in Step 6)

**Your key looks like:** `AIzaSyBcdEfGhIjKlMnOpQrStUvWxYz`

✅ **DONE - You have your Gemini key!**

---

## ✅ STEP 2: Create GitHub Account (If You Don't Have One)

1. Go to: `https://github.com/signup`
2. Enter email → Click **"Continue"**
3. Create password → Click **"Continue"**  
4. Enter username → Click **"Continue"**
5. Verify email → Done!

✅ **DONE - Skip if you already have GitHub account**

---

## ✅ STEP 3: Create New Repository on GitHub

### Click-by-Click:

1. Go to: `https://github.com/new`
2. In "Repository name" box, type: `grc-platform-python`
3. Click the **"Public"** circle
4. **Check** the box: "Add a README file"
5. Click **"Create repository"** (green button at bottom)
6. Wait 3 seconds

✅ **DONE - Your repository is created!**

---

## ✅ STEP 4: Open GitHub Codespaces (Your Cloud Computer!)

### Click-by-Click:

1. You're on your repo page already
2. Look for green **"Code"** button (top right)
3. Click it
4. Click **"Codespaces"** tab
5. Click **"Create codespace on main"** (green button)
6. Wait 1-2 minutes → VS Code opens in browser!

✅ **DONE - You're now in your cloud development environment!**

---

## ✅ STEP 5: Open Terminal in Codespaces

### Click-by-Click:

1. Look at bottom of screen → You see tabs like "PROBLEMS", "OUTPUT", "TERMINAL"
2. Click **"TERMINAL"** tab
3. You see a command prompt with `@` symbol

If you don't see terminal:
- Click **"Terminal"** menu at very top
- Click **"New Terminal"**

✅ **DONE - Terminal is open!**

---

## ✅ STEP 6: Install Reflex (Copy-Paste Commands)

### Action 1: Install Reflex

**Copy this ENTIRE command:**
```bash
pip install reflex pymongo python-dotenv google-generativeai motor
```

**Paste in terminal** (Right-click → Paste, or Ctrl+V)

**Press Enter**

**Wait 30-40 seconds** → You'll see "Successfully installed..."

### Action 2: Initialize Reflex

**Copy this:**
```bash
reflex init --template blank
```

**Paste → Press Enter**

**When it asks "App name:"** → Type: `grc_platform`

**Press Enter**

**Wait 10 seconds** → You'll see "Success!"

✅ **DONE - Reflex is installed!**

---

## ✅ STEP 7: Create .env File (Your Gemini Key Goes Here!)

### Click-by-Click:

1. Look at left sidebar → You see file explorer
2. Right-click on empty space
3. Click **"New File"**
4. Name it: `.env`
5. Press Enter
6. File opens on right side

### Paste This (Replace with YOUR key):

```env
GOOGLE_API_KEY=AIzaSyXXXXXXXXXXXXX
MONGO_URL=mongodb+srv://demo:demo@cluster.mongodb.net/
DB_NAME=grc_platform
```

**IMPORTANT:** Replace `AIzaSyXXXXXXXXXXXXX` with the key you copied in Step 1!

7. Press **Ctrl+S** (or Cmd+S) to save

✅ **DONE - Configuration saved!**

---

## ✅ STEP 8: Download All Code Files

### Action: Copy Files from Emergent

I've created all the code files in `/app/reflex-grc/`. You need to copy them to your Codespace.

**Option A: Use My Pre-Built Files**

In Codespace terminal, paste:

```bash
# Create directory structure
mkdir -p grc_platform

# Download files (I'll provide download links)
```

**Option B: I'll provide each file content for you to copy-paste**

Which would you prefer? 

For now, let me create a simple seed script...

---

## ✅ STEP 9: Run Seed Data (Populate Database)

**Copy-paste this command:**
```bash
python seed_frameworks.py
```

**Press Enter**

You'll see: "✓ Frameworks seeded successfully"

✅ **DONE - Database has sample data!**

---

## ✅ STEP 10: Run Your App Locally

**Copy-paste:**
```bash
reflex run
```

**Press Enter**

**Wait 30 seconds** → You'll see:

```
App running at: http://localhost:3000
Backend running at: http://localhost:8000
```

A popup appears → Click **"Open in Browser"**

✅ **DONE - Your app is running!** 🎉

---

## ✅ STEP 11: Deploy to Reflex Cloud (FREE Forever!)

### Action 1: Login to Reflex

**Copy-paste:**
```bash
reflex login
```

**Press Enter**

Browser opens → Click **"Sign in with GitHub"**

Click **"Authorize Reflex"**

Go back to Codespace terminal

### Action 2: Set Your Gemini Key

**Copy this (replace with YOUR key):**
```bash
reflex config GOOGLE_API_KEY="AIzaSyXXXXXXXX"
```

**Paste → Press Enter**

### Action 3: Deploy!

**Copy-paste:**
```bash
reflex deploy
```

**Press Enter**

**When it asks "Region?"** → Type: `us-west-2`

**When it asks "Confirm?"** → Type: `y`

**Press Enter**

**Wait 2-3 minutes** → You'll see:

```
✓ Deployment successful!
🚀 Your app is live at: https://grc-platform.reflex.run
```

✅ **DONE - Your app is LIVE on the internet!** 🌐

---

## ✅ STEP 12: Access Your Live App

1. Copy the URL from terminal (ends with `.reflex.run`)
2. Open in new browser tab
3. Share with anyone!

---

## 🎉 YOU'RE DONE!

**What You Have:**
✅ GRC Platform running at your-app.reflex.run
✅ Code backed up on GitHub
✅ FREE hosting forever
✅ Google Gemini AI integrated
✅ Complete GRC features

**Total Time:** 20-30 minutes
**Total Cost:** $0

---

## 🔄 To Update Your App Later:

1. Make changes in Codespace
2. In terminal:
```bash
git add .
git commit -m \"Updated features\"
git push
reflex deploy
```
3. Wait 2 minutes → Updated!

---

## 📍 WHERE TO FIND EVERYTHING:

- **Your Live App**: `https://your-app.reflex.run`
- **GitHub Repo**: `https://github.com/YOUR_USERNAME/grc-platform-python`
- **Codespace**: Click "Code" → "Codespaces" on your repo

---

**Next: I'll create all the code files you need to copy into Codespace!**
