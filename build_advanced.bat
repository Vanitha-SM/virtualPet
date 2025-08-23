@echo off
echo Building Advanced Virtual Pet Executable...
echo.

REM Install PyInstaller if not already installed
echo Installing PyInstaller...
pip install pyinstaller

echo.
echo Building executable with advanced options...
pyinstaller --onefile ^
            --windowed ^
            --name "VirtualPet" ^
            --icon=sprites/idle/final-10.png ^
            --add-data "sprites;sprites" ^
            --hidden-import PyQt5.QtCore ^
            --hidden-import PyQt5.QtGui ^
            --hidden-import PyQt5.QtWidgets ^
            --clean ^
            main.py

echo.
echo Build complete! Check the 'dist' folder for VirtualPet.exe
echo.
echo The executable includes all sprite files and dependencies.
echo Users can now run it without Python installed!
echo.
pause
