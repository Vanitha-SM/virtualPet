# 🐾 Virtual Pet Desktop Companion

A cute, animated virtual pet that lives on your desktop! Your pet will roam around, change animations, and respond to your interactions. Perfect for adding some life to your computer screen.

## Pet animation Source -
All the sprites files and artworks has been sourced from the artist crug63r. Below are the profike links for the artists art work

https://crug63r.itch.io/

https://crug63r.itch.io/aoko-asp1

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

### For Users (No Python Required)
If you have the `VirtualPet.exe` file, simply double-click it to run your virtual pet!

### For Developers
Your virtual pet is ready to bring life to your desktop! Run `run_pet.bat` or `python main.py` and enjoy your new companion.


**Happy petting! 🐾✨**


