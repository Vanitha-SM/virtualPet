#!/usr/bin/env python3
"""
Build script for Virtual Pet executable
Run this script to create a standalone .exe file
"""

import os
import sys
import subprocess
import shutil

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    try:
        import PyInstaller
        print("✓ PyInstaller already installed")
        return True
    except ImportError:
        print("Installing PyInstaller...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("✓ PyInstaller installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("✗ Failed to install PyInstaller")
            return False

def build_executable():
    """Build the executable using PyInstaller"""
    print("Building Virtual Pet executable...")
    
    # PyInstaller command with more robust PyQt5 handling
    cmd = [
        "pyinstaller",
        "--onedir",                     # Use directory instead of single file (more reliable)
        "--windowed",                   # No console window
        "--name", "VirtualPet",         # Executable name
        # "--icon=sprites/idle/final-10.png",  # Icon from your sprites (commented out due to format issues)
        "--add-data", "sprites;sprites",     # Include sprite folder
        "--add-data", "sprites/idle;sprites/idle",  # Ensure idle sprites are included
        "--add-data", "sprites/walk;sprites/walk",  # Ensure walk sprites are included
        "--add-data", "sprites/run;sprites/run",    # Ensure run sprites are included
        "--add-data", "sprites/jump;sprites/jump",  # Ensure jump sprites are included
        "--hidden-import", "PyQt5.QtCore",   # Ensure PyQt5 modules are included
        "--hidden-import", "PyQt5.QtGui",
        "--hidden-import", "PyQt5.QtWidgets",
        "--hidden-import", "PyQt5.sip",      # Additional PyQt5 dependency
        "--hidden-import", "PyQt5.QtPrintSupport",  # Additional Qt modules
        "--hidden-import", "PyQt5.QtSvg",
        "--collect-all", "PyQt5",            # Collect ALL PyQt5 modules
        "--collect-all", "PyQt5.QtCore",
        "--collect-all", "PyQt5.QtGui", 
        "--collect-all", "PyQt5.QtWidgets",
        "--exclude-module", "matplotlib",     # Exclude unnecessary modules
        "--exclude-module", "numpy",
        "--exclude-module", "PIL",
        "--clean",                      # Clean build cache
        "main.py"
    ]
    
    try:
        subprocess.check_call(cmd)
        print("✓ Executable built successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Build failed with error: {e}")
        return False

def cleanup():
    """Clean up build artifacts"""
    print("Cleaning up build files...")
    
    # Remove build and spec files
    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists("VirtualPet.spec"):
        os.remove("VirtualPet.spec")
    
    print("✓ Cleanup complete")

def main():
    """Main build process"""
    print("🐾 Virtual Pet Executable Builder")
    print("=" * 40)
    
    # Check if main.py exists
    if not os.path.exists("main.py"):
        print("✗ Error: main.py not found!")
        print("Make sure you're running this script from the project directory.")
        return
    
    # Check if sprites folder exists
    if not os.path.exists("sprites"):
        print("✗ Error: sprites folder not found!")
        print("Make sure the sprites folder is in the same directory.")
        return
    
    # Install PyInstaller
    if not install_pyinstaller():
        return
    
    # Build executable
    if not build_executable():
        return
    
    # Cleanup
    cleanup()
    
    print("\n🎉 Build completed successfully!")
    print("📁 Your executable is in the 'dist' folder: VirtualPet.exe")
    print("🚀 Users can now run it without Python installed!")
    print("\nTo distribute:")
    print("1. Copy VirtualPet.exe from the dist folder")
    print("2. Share it with others - no installation required!")

if __name__ == "__main__":
    main()
