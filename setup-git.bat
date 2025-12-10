@echo off
REM Django Portfolio - Git Setup and Push Script

echo.
echo ================================
echo Django Portfolio - GitHub Push
echo ================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Git is not installed!
    echo Please install Git from: https://git-scm.com/download/win
    echo After installation, restart your computer and run this script again.
    pause
    exit /b 1
)

echo [1/6] Configuring Git user...
git config --global user.name "Django Portfolio Developer"
git config --global user.email "developer@portfolio.local"

echo [2/6] Initializing repository...
git init

echo [3/6] Adding all files...
git add .

echo [4/6] Creating initial commit...
git commit -m "Initial commit: Django Portfolio Project

- Models: Project, Skill, About
- Views and URL routing configured
- Templates for home, projects, skills, and project detail
- Admin interface configured
- Ready for deployment"

echo [5/6] Repository initialized successfully!
echo.
echo Next steps:
echo 1. Go to https://github.com/new
echo 2. Create a new repository named 'django-portfolio'
echo 3. Copy the repository URL
echo 4. Run this command:
echo    git remote add origin YOUR_REPOSITORY_URL
echo 5. Then run:
echo    git branch -M main
echo    git push -u origin main
echo.
echo When prompted for authentication, use your GitHub credentials.
echo.
pause
