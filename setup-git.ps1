# Django Portfolio - Git Setup and Push Script for PowerShell

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Django Portfolio - GitHub Push" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Check if git is installed
$gitCheck = git --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Git is not installed!" -ForegroundColor Red
    Write-Host "Please install Git from: https://git-scm.com/download/win" -ForegroundColor Yellow
    Write-Host "After installation, restart your computer and run this script again." -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[1/6] Configuring Git user..." -ForegroundColor Green
git config --global user.name "Django Portfolio Developer"
git config --global user.email "developer@portfolio.local"

Write-Host "[2/6] Initializing repository..." -ForegroundColor Green
git init

Write-Host "[3/6] Adding all files..." -ForegroundColor Green
git add .

Write-Host "[4/6] Creating initial commit..." -ForegroundColor Green
git commit -m "Initial commit: Django Portfolio Project

- Models: Project, Skill, About
- Views and URL routing configured
- Templates for home, projects, skills, and project detail
- Admin interface configured
- Ready for deployment"

Write-Host ""
Write-Host "[5/6] Repository initialized successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Go to https://github.com/new" -ForegroundColor White
Write-Host "2. Create a new repository named 'django-portfolio'" -ForegroundColor White
Write-Host "3. Copy the repository URL" -ForegroundColor White
Write-Host "4. Run this command:" -ForegroundColor White
Write-Host "   git remote add origin YOUR_REPOSITORY_URL" -ForegroundColor Yellow
Write-Host "5. Then run:" -ForegroundColor White
Write-Host "   git branch -M main" -ForegroundColor Yellow
Write-Host "   git push -u origin main" -ForegroundColor Yellow
Write-Host ""
Write-Host "When prompted for authentication, use your GitHub credentials." -ForegroundColor Cyan
Write-Host ""
Read-Host "Press Enter to close this window"
