# How to Push Your Django Portfolio to GitHub

## ⚠️ Important: Install Git First!

**Your system currently does NOT have Git installed.**

### Step 1: Install Git

1. **Download Git for Windows**
   - Go to: https://git-scm.com/download/win
   - The download should start automatically
   - If not, click the blue "Click here to download manually" link

2. **Install Git**
   - Run the installer (Git-X.XX.X-64-bit.exe)
   - Click **Next** on each screen
   - Use the default settings
   - When you see "Configure the line ending conversions", select:
     - **"Checkout Windows-style, commit Unix-style line endings"**
   - Complete the installation

3. **Restart Your Computer**
   - This is important! Restart after installation.

---

## Step 2: Create a GitHub Repository

1. Go to: https://github.com/new
2. **Repository name:** `django-portfolio`
3. **Description:** "A modern Django portfolio website to showcase projects and skills"
4. **Public or Private:** Choose based on your preference
   - **Public:** Anyone can see it (good for portfolios)
   - **Private:** Only you can see it
5. **DO NOT check:** "Initialize this repository with README"
6. Click **Create repository**
7. **Copy the repository URL** (it will look like: `https://github.com/yourusername/django-portfolio.git`)

---

## Step 3: Push Your Code

### Option A: Using the Setup Script (Recommended)

1. Open File Explorer
2. Navigate to `C:\Censon\Ralph`
3. Right-click the `setup-git.ps1` file
4. Select **Run with PowerShell**
5. If you get a security warning, type `Y` and press Enter
6. Follow the instructions in the script

### Option B: Manual Commands

1. **Open PowerShell in C:\Censon\Ralph**
   - Shift + Right-click in the folder
   - Select **Open PowerShell window here**

2. **Run these commands one by one:**

```powershell
# Configure Git (first time only)
git config --global user.name "Your Name"
git config --global user.email "your.email@gmail.com"

# Initialize git repository
git init

# Add all files to git
git add .

# Create initial commit
git commit -m "Initial commit: Django Portfolio Project"

# Add your GitHub repository as remote
git remote add origin https://github.com/yourusername/django-portfolio.git

# Rename branch to main (GitHub standard)
git branch -M main

# Push to GitHub
git push -u origin main
```

3. **When you run `git push -u origin main`:**
   - A browser window will open
   - Click **Authorize GitCredentialManager**
   - This allows your computer to push code to GitHub

---

## Step 4: Verify Your Code is on GitHub

1. Go to `https://github.com/yourusername/django-portfolio`
2. You should see all your files:
   - ✅ Ivan/ folder
   - ✅ Ralph/ folder
   - ✅ templates/ folder
   - ✅ manage.py
   - ✅ requirements.txt
   - ✅ README.md
   - And more...

3. Files **NOT visible** (correctly excluded by .gitignore):
   - ❌ db.sqlite3
   - ❌ .venv/
   - ❌ __pycache__/
   - ❌ .env

---

## Troubleshooting

### Error: "git: The term 'git' is not recognized"

**Solution:** Git is not installed or not in your PATH
1. Install Git: https://git-scm.com/download/win
2. **Restart your computer**
3. Try again in a new PowerShell window

---

### Error: "fatal: not a git repository"

**Solution:** You're not in the right directory
1. Open PowerShell
2. Run: `cd C:\Censon\Ralph`
3. Then run the git commands

---

### Error: "remote origin already exists"

**Solution:** You already have a remote set up
```powershell
git remote remove origin
git remote add origin https://github.com/yourusername/django-portfolio.git
git push -u origin main
```

---

### Error: "Everything up-to-date" but files not on GitHub

**Solution:** Check that you added your correct repository URL
```powershell
git remote -v
# Should show your GitHub URL
```

---

## What to Do After Pushing

✅ **Your GitHub repository is now live!**

1. **Share your portfolio**
   - Share the link: `https://github.com/yourusername/django-portfolio`
   - Include in your resume/CV
   - Share on LinkedIn

2. **Make it a deployed website**
   - Use Heroku (free tier): https://www.heroku.com
   - Use PythonAnywhere: https://www.pythonanywhere.com
   - Use Railway: https://railway.app

3. **Add more features**
   - Contact form
   - Blog section
   - Dark mode
   - More styling

4. **Keep updating**
   - Add new projects
   - Update skills
   - Push changes to GitHub with:
     ```powershell
     git add .
     git commit -m "Your message here"
     git push origin main
     ```

---

## Quick Reference

| Command | What it does |
|---------|-------------|
| `git init` | Start a new git repository |
| `git add .` | Add all files for commit |
| `git commit -m "message"` | Save changes with a message |
| `git remote add origin URL` | Connect to GitHub |
| `git push origin main` | Upload to GitHub |
| `git status` | See what files changed |
| `git log --oneline` | See commit history |

---

## Need Help?

- **Git Documentation:** https://git-scm.com/docs
- **GitHub Help:** https://docs.github.com
- **Django Documentation:** https://docs.djangoproject.com

---

**You're all set! 🚀 Good luck with your portfolio!**
