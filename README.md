# 🐾 Virtual Pet Desktop Companion

A cute, animated virtual pet that lives on your desktop! Your pet will roam around, change animations, and respond to your interactions. Perfect for adding some life to your computer screen.

![Virtual Pet Demo](https://img.shields.io/badge/Status-Ready%20to%20Use-brightgreen)
![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

[![GitHub stars](https://img.shields.io/github/stars/Vanitha-SM/virtualPet.svg?style=social&label=Star)](https://github.com/Vanitha-SM/virtualPet)
[![GitHub forks](https://img.shields.io/github/forks/Vanitha-SM/virtualPet.svg?style=social&label=Fork)](https://github.com/Vanitha-SM/virtualPet)

## ✨ Features

- **🖥️ Desktop Overlay**: Runs on top of all applications
- **🎭 Animated Sprites**: Multiple animation states (idle, walk, run, jump, etc.)
- **🧠 Smart Behavior**: Autonomous movement and mood system
- **🖱️ Interactive**: Click to pet, drag to move, double-click to teleport
- **🔄 Persistent**: Continues running in the background
- **📱 Customizable Size**: Easy to adjust pet size

## 🚀 Quick Start

### Option 1: Run Executable (Recommended - No Python Required!)
1. **Download the VirtualPet.exe file** (if provided)
2. **Double-click to run** - that's it! No installation needed

### Option 2: Run from Source Code

#### Prerequisites
- **Windows 10/11** (tested and optimized)
- **Python 3.7 or higher**
- **Internet connection** (for first-time setup)

### Step 1: Download & Extract
1. Download this project folder to your computer
2. Extract it to a location like `C:\Users\YourName\Desktop\virtualPet\`

### Step 2: Install Python (if you don't have it)
1. Go to [python.org](https://python.org)
2. Download Python 3.7+ for Windows
3. **IMPORTANT**: Check "Add Python to PATH" during installation
4. Restart your computer after installation

### Step 3: Install Dependencies
1. Open **Command Prompt** or **PowerShell**
2. Navigate to your project folder:
   ```cmd
   cd "C:\Users\YourName\Desktop\virtualPet"
   ```
3. Install required packages:
   ```cmd
   pip install -r requirements.txt
   ```

### Step 4: Run Your Virtual Pet!
**Option A: Run the executable (if built)**
- Double-click `VirtualPet.exe` in the `dist` folder

**Option B: Double-click the batch file**
- Simply double-click `run_pet.bat` in your project folder

**Option C: Command line**
```cmd
python main.py
```

## 🎮 How to Use

### Basic Controls
- **🖱️ Left Click**: Pet your virtual pet (boosts happiness +10, energy +5)
- **🖱️ Drag**: Click and drag to move the pet around
- **🖱️ Double-Click**: Teleport pet to random location (boosts stats)

### Pet Behavior
Your virtual pet is autonomous and will:
- 🚶‍♂️ **Roam around** the screen with realistic bouncing
- 🎭 **Change animations** based on mood and energy
- 💤 **Get tired** when energy is low (shows "down" animation)
- 😢 **Get sad** when happiness is low (shows "idle" animation)
- 🎉 **Perform random actions** like jumping or running

### Pet Stats
- **Energy**: Decreases over time, affects activity level
- **Happiness**: Decreases over time, affects mood
- **Click interactions** boost both stats!

## 🎨 Customization

### Change Pet Size
Open `main.py` and find this line:
```python
scale_factor = 0.5  # 0.5 = half size, 0.3 = 30% size, etc.
```
- `0.3` = Very small (30% of original)
- `0.5` = Small (50% of original) ← **Default**
- `0.7` = Medium (70% of original)
- `1.0` = Full size (100%)

### Adjust Behavior
Modify these values in `main.py`:
- `animation_speed`: How fast sprites animate (milliseconds)
- Movement speed and direction change frequency
- Energy and happiness decay rates

## 🔨 Building an Executable

Want to create a standalone .exe file that others can run without Python? Here's how:

### Quick Build (Windows)
1. **Double-click `build_exe.bat`** in your project folder
2. Wait for the build to complete
3. Find `VirtualPet.exe` in the `dist` folder

### Advanced Build (Recommended)
1. **Run the Python build script:**
   ```cmd
   python build.py
   ```
2. This script handles everything automatically and provides better error handling

### Manual Build
```cmd
pip install pyinstaller
pyinstaller --onefile --windowed --name "VirtualPet" --add-data "sprites;sprites" main.py
```

### What Gets Created
- **`dist/VirtualPet.exe`** - Your standalone executable
- **All sprites included** - No need to distribute sprite folders separately
- **No Python required** - Users can run it on any Windows computer

## 🐛 Troubleshooting

### "No module named 'PyQt5'"
```cmd
pip install PyQt5
```

### "Sprite directory not found"
- Make sure you're running the script from the project folder
- Check that the `sprites/` folder exists with your PNG files

### Pet not visible
- The pet might be off-screen
- Double-click to teleport it back
- Check that your sprites folder contains PNG files

### Performance issues
- Reduce animation speed in the code
- Close other resource-heavy applications

### Pet too big/small
- Adjust the `scale_factor` value in the code
- Restart the application after changes

## 📁 File Structure
```
virtualPet/
├── main.py              # Main virtual pet application
├── requirements.txt     # Python dependencies
├── run_pet.bat         # Windows batch file to run easily
├── build_exe.bat       # Quick executable builder
├── build.py             # Advanced executable builder (recommended)
├── README.md           # This file
├── dist/               # Executable output folder (created after building)
│   └── VirtualPet.exe  # Standalone executable (after building)
└── sprites/            # Your pet animation sprites
    ├── idle/           # Resting animations
    ├── walk/           # Walking animations
    ├── run/            # Running animations
    ├── jump/           # Jumping animations
    ├── up/             # Upward movement
    └── down/           # Downward movement
```

## 🔧 Advanced Usage

### Run Multiple Pets
```cmd
python main.py
# In another terminal:
python main.py
```

### Custom Sprite Folders
Modify the `animations` dictionary in `load_sprites()` to add new animation types.

### Background Operation
The pet continues running even when you close the main window. To completely stop it, use Task Manager and end the Python process.

## 🆘 Support

### Common Issues
1. **Python not found**: Make sure Python is installed and added to PATH
2. **PyQt5 errors**: Try `pip install --upgrade PyQt5`
3. **Sprites not loading**: Check file permissions and PNG format
4. **Pet stuck**: Double-click to teleport or restart the application

### Getting Help
- Check that all files are in the correct folders
- Ensure Python 3.7+ is installed
- Verify PyQt5 is properly installed
- Try running from Command Prompt to see error messages

## 🎯 Tips for Best Experience

- **Keep the pet visible**: Don't let it get stuck behind other windows
- **Regular interaction**: Click your pet to keep it happy and energetic
- **Monitor performance**: If your computer slows down, close other applications
- **Customize size**: Adjust the scale factor to match your screen size
- **Multiple monitors**: The pet works across all connected displays

## 🚀 Ready to Go!

### For Users (No Python Required)
If you have the `VirtualPet.exe` file, simply double-click it to run your virtual pet!

### For Developers
Your virtual pet is ready to bring life to your desktop! Run `run_pet.bat` or `python main.py` and enjoy your new companion.

### Want to Share with Others?
Build an executable using the build scripts above, then share the `VirtualPet.exe` file. Others can run it without installing Python!

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Ideas for Contributions
- 🎨 New pet animations and behaviors
- 🔧 Performance optimizations
- 🐛 Bug fixes and improvements
- 📚 Documentation updates
- 🌍 Localization support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [PyQt5](https://www.riverbankcomputing.com/software/pyqt/)
- Sprite animations and graphics
- Community feedback and suggestions

**Happy petting! 🐾✨**

---

*Made with ❤️ using Python and PyQt5*
