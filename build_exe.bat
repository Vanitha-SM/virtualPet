@echo off
echo Building Virtual Pet Executable...
echo.

REM Install PyInstaller if not already installed
echo Installing PyInstaller...
pip install pyinstaller

echo.
echo Building executable...
pyinstaller --onefile --windowed --name "VirtualPet" --icon=sprites/idle/final-10.png main.py

echo.
echo Build complete! Check the 'dist' folder for VirtualPet.exe
echo.
pause
