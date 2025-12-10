# GitHub Push Instructions

Follow these steps to push your Django Portfolio to GitHub:

## Prerequisites

1. **Install Git**
   - Download from https://git-scm.com/download/win (for Windows)
   - Install with default settings

2. **Create a GitHub Account**
   - Go to https://github.com
   - Sign up if you don't have an account

## Step-by-Step Instructions

### 1. Create a New Repository on GitHub

1. Go to https://github.com/new
2. Repository name: `django-portfolio` (or your preferred name)
3. Add description: "A modern Django portfolio website"
4. Choose **Public** or **Private**
5. **DO NOT** check "Initialize this repository with: README"
6. Click **Create repository**

### 2. Open PowerShell in Your Project Directory

1. Open the folder `C:\Censon\Ralph` in File Explorer
2. Right-click inside the folder → **Open PowerShell window here**
   - Or press `Shift + Right-click` → **Open PowerShell window here**

### 3. Configure Git (First Time Only)

```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 4. Initialize and Commit Your Code

Run these commands in PowerShell:

```powershell
# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Django portfolio project"
```

### 5. Add Remote Repository

Replace `yourusername` and `repository-name` with your GitHub username and repo name:

```powershell
git remote add origin https://github.com/yourusername/django-portfolio.git
```

### 6. Push to GitHub

For Windows PowerShell, use:

```powershell
git branch -M main
git push -u origin main
```

A browser window will open asking for authentication. Sign in with your GitHub credentials.

### 7. Verify on GitHub

1. Go to `https://github.com/yourusername/django-portfolio`
2. You should see all your files uploaded!

## What Gets Uploaded?

✅ **Included (in repository):**
- All Python files (.py)
- HTML templates
- Django configuration
- requirements.txt
- README.md
- LICENSE
- .gitignore

❌ **Excluded (due to .gitignore):**
- `db.sqlite3` (database)
- `__pycache__/` (Python cache)
- `.venv/` (virtual environment)
- `*.pyc` files
- `.env` (environment variables)
- `staticfiles/` (compiled static files)

## Updating Your Repository

To update your GitHub repository with new changes:

```powershell
# Stage changes
git add .

# Commit changes
git commit -m "Describe your changes here"

# Push to GitHub
git push origin main
```

## Important Security Notes

1. **Never commit sensitive data:**
   - Never push `.env` files with real secrets
   - Never push database files with real data
   - Never commit API keys or passwords

2. **Keep your repository clean:**
   - Add more rules to `.gitignore` if needed
   - Only commit necessary files

3. **Update settings for production:**
   - Change `SECRET_KEY` in `settings.py`
   - Set `DEBUG = False` for production
   - Use environment variables for sensitive settings

## Troubleshooting

### Error: "git: The term 'git' is not recognized"
- Git is not installed or not in PATH
- Restart your computer after installing Git
- Try opening a new PowerShell window

### Error: "remote origin already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/yourusername/django-portfolio.git
```

### Error: "Please tell me who you are"
You haven't configured your Git username and email. Run:
```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Authentication Issues
1. If prompted for password, use a **Personal Access Token** instead:
   - Go to GitHub Settings → Developer settings → Personal access tokens
   - Generate new token with `repo` scope
   - Use token as password when prompted

## Next Steps After Pushing

1. **Add a .env.example file** (already created)
2. **Write deployment documentation**
3. **Add contribution guidelines** (CONTRIBUTING.md)
4. **Add badges** to README.md
5. **Set up GitHub Actions** for CI/CD (optional)

## Useful Git Commands

```powershell
# Check status
git status

# View commit history
git log --oneline

# Create a new branch
git checkout -b feature-name

# Switch branches
git checkout main

# Delete a branch
git branch -d branch-name

# View remote repositories
git remote -v

# Pull latest changes
git pull origin main
```

---

**Need help?** Check the official Git documentation: https://git-scm.com/docs
