# Virtual Pet Overlay

A cute virtual pet that runs as a background overlay on your desktop! Your pet will roam around the screen, animate with different behaviors, and respond to your interactions.

## Features

- **Background Overlay**: Runs on top of all other applications
- **Sprite Animations**: Uses your existing sprite sheets for realistic animations
- **Autonomous Behavior**: Pet moves around, changes animations, and has mood/energy systems
- **Interactive**: Click to pet, drag to move, double-click to teleport
- **Persistent**: Continues running even when you close the main window

## Sprite Support

The virtual pet automatically loads and uses your existing sprite animations:
- **idle**: Default resting animation
- **walk**: Walking movement
- **run**: Fast running animation
- **jump**: Jumping/celebrating
- **up**: Upward movement
- **down**: Downward/tired movement

## Installation

1. Install Python 3.7+ if you haven't already
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Pet

**Option 1: Command Line**
```bash
python main.py
```

**Option 2: Windows Batch File**
Double-click `run_pet.bat`

### Controls

- **Left Click**: Pet your virtual pet (boosts happiness and energy)
- **Drag**: Move the pet around the screen
- **Double-Click**: Teleport the pet to a random location
- **Close Button**: The pet will continue running in the background

### Pet Behavior

Your virtual pet has:
- **Energy**: Decreases over time, affects activity level
- **Happiness**: Decreases over time, affects mood
- **Autonomous Movement**: Roams around the screen with realistic bouncing
- **Smart Animations**: Changes animations based on mood and energy
- **Random Actions**: Occasionally performs random behaviors

## Customization

You can modify the pet's behavior by editing these values in `main.py`:
- `animation_speed`: How fast sprites animate (milliseconds)
- `energy` and `happiness` decay rates
- Movement speed and direction change frequency
- Animation change probabilities

## Troubleshooting

- **No sprites visible**: Make sure your `sprites/` directory contains PNG files
- **Pet not moving**: Check that PyQt5 is properly installed
- **Performance issues**: Adjust timer intervals in the code

## Technical Details

- Built with PyQt5 for cross-platform compatibility
- Uses transparent overlay windows for seamless desktop integration
- Implements sprite sheet animation system
- Background timers for autonomous behavior
- Mouse event handling for user interaction

## License

This project is open source. Feel free to modify and distribute!
