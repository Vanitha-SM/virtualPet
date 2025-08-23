@echo off
echo 🔧 Fixing GitHub Repository Setup for Virtual Pet
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
    echo ❌ main.py not found! Make sure you're in the right directory.
    pause
    exit /b 1
)

echo ✅ Project files found
echo.

REM Check current remote status
echo 📡 Checking current remote configuration...
git remote -v
echo.

REM Ask user what to do
echo Choose an option:
echo 1. Remove old remote and add new one
echo 2. Update existing remote URL
echo 3. Just show current status
echo.
set /p choice="Enter your choice (1-3): "

if "%choice%"=="1" (
    echo.
    echo 🔄 Removing old remote...
    git remote remove origin
    echo ✅ Old remote removed
    echo.
    set /p new_url="Enter your new GitHub repository URL: "
    git remote add origin "%new_url%"
    echo ✅ New remote added: %new_url%
) else if "%choice%"=="2" (
    echo.
    set /p new_url="Enter your new GitHub repository URL: "
    git remote set-url origin "%new_url%"
    echo ✅ Remote URL updated to: %new_url%
) else if "%choice%"=="3" (
    echo.
    echo 📊 Current remote configuration:
    git remote -v
    echo.
    echo No changes made.
    pause
    exit /b 0
) else (
    echo ❌ Invalid choice. Exiting.
    pause
    exit /b 1
)

echo.
echo 📡 New remote configuration:
git remote -v
echo.

REM Check if we need to commit changes
git status --porcelain | findstr /r "^[AM]" >nul
if not errorlevel 1 (
    echo 📁 Uncommitted changes detected. Committing...
    git add .
    git commit -m "Update project files and documentation"
    echo ✅ Changes committed
) else (
    echo ✅ No uncommitted changes
)

echo.
echo 🚀 Ready to push to your new repository!
echo.
echo Run this command to push:
echo git push -u origin main
echo.
echo Or if you're using 'master' branch:
echo git push -u origin master
echo.
pause
