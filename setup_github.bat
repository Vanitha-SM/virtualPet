@echo off
echo 🚀 Setting up GitHub Repository for Virtual Pet
echo ================================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git is not installed! Please install Git first.
    echo Download from: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo ✅ Git is installed
echo.

REM Check if we're in the right directory
if not exist "main.py" (
    echo ❌ main.py not found! Make sure you're in the project directory.
    pause
    exit /b 1
)

echo ✅ Project files found
echo.

REM Initialize git repository
echo 🔧 Initializing Git repository...
git init

REM Add all files
echo 📁 Adding files to Git...
git add .

REM Make initial commit
echo 💾 Making initial commit...
git commit -m "Initial commit: Virtual Pet Desktop Companion with power management"

echo.
echo 🎉 Git repository initialized successfully!
echo.
echo 📋 Next steps:
echo 1. Create a new repository on GitHub
echo 2. Copy the repository URL
echo 3. Run these commands:
echo    git remote add origin YOUR_REPOSITORY_URL
echo    git push -u origin main
echo.
echo 💡 Replace YOUR_REPOSITORY_URL with your actual GitHub repo URL
echo.
pause
