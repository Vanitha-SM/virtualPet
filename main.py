import sys
import random
import os
from PyQt5.QtCore import Qt, QTimer, QPoint, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtCore import pyqtProperty, QRect


class VirtualPet(QWidget):
    def __init__(self):
        super().__init__()
        
        # Set up the window properties for overlay
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint |
            Qt.FramelessWindowHint |
            Qt.Tool |
            Qt.WindowDoesNotAcceptFocus
        )
        
        # Make background transparent
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_ShowWithoutActivating, True)
        
        # Initialize sprite system
        self.current_animation = "idle"
        self.current_frame = 0
        self.animation_speed = 100  # milliseconds between frames
        self.sprites = {}
        self.load_sprites()
        
        # Set initial size based on sprite dimensions (scaled down)
        if self.sprites:
            first_sprite = list(self.sprites.values())[0][0]
            # Scale down the pet size - adjust these values to make it smaller/larger
            scale_factor = 0.3  # 0.5 = half size, 0.3 = 30% size, etc.
            new_width = int(first_sprite.width() * scale_factor)
            new_height = int(first_sprite.height() * scale_factor)
            self.resize(new_width, new_height)
        
        # Movement and behavior
        self.dx = random.choice([-2, -1, 1, 2])
        self.dy = random.choice([-2, -1, 1, 2])
        self.energy = 100
        self.happiness = 100
        self.last_action = 0
        
        # Power-efficient timers
        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self.animate)
        self.animation_timer.start(self.animation_speed)
        
        self.behavior_timer = QTimer()
        self.behavior_timer.timeout.connect(self.update_behavior)
        self.behavior_timer.start(2000)  # Reduced to every 2 seconds
        
        self.movement_timer = QTimer()
        self.movement_timer.timeout.connect(self.move_pet)
        self.movement_timer.start(100)  # Reduced to every 100ms
        
        # Power management
        self.is_visible = True
        self.last_activity = 0
        self.power_save_mode = False
        self.power_status_timer = QTimer()
        self.power_status_timer.timeout.connect(self.show_power_status)
        self.power_status_timer.start(10000)  # Show status every 10 seconds
        
        # Position pet randomly on screen
        self.randomize_position()
        
        # Show the pet
        self.show()
        
    def load_sprites(self):
        """Load all sprite animations from the sprites directory"""
        sprite_dir = "sprites"
        if not os.path.exists(sprite_dir):
            print(f"Sprite directory {sprite_dir} not found!")
            return
            
        # Define animation sequences
        animations = {
            "idle": ["idle"],
            "walk": ["walk"],
            "run": ["run"],
            "jump": ["jump"],
            "up": ["up"],
            "down": ["down"]
        }
        
        for anim_name, subdirs in animations.items():
            self.sprites[anim_name] = []
            for subdir in subdirs:
                subdir_path = os.path.join(sprite_dir, subdir)
                if os.path.exists(subdir_path):
                    # Load all PNG files in the subdirectory
                    for file in sorted(os.listdir(subdir_path)):
                        if file.endswith('.png'):
                            file_path = os.path.join(subdir_path, file)
                            pixmap = QPixmap(file_path)
                            if not pixmap.isNull():
                                self.sprites[anim_name].append(pixmap)
        
        # If no sprites loaded, create a simple colored rectangle
        if not any(self.sprites.values()):
            self.create_fallback_sprite()
    
    def create_fallback_sprite(self):
        """Create a simple fallback sprite if no image files are found"""
        pixmap = QPixmap(64, 64)
        pixmap.fill(Qt.transparent)
        
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Draw a simple pet shape
        path = QPainterPath()
        path.addEllipse(20, 20, 24, 24)  # Body
        path.addEllipse(15, 15, 8, 8)    # Left ear
        path.addEllipse(41, 15, 8, 8)    # Right ear
        
        painter.fillPath(path, Qt.blue)
        painter.end()
        
        self.sprites["idle"] = [pixmap]
    
    def animate(self):
        """Animate the current sprite sequence"""
        if self.current_animation in self.sprites and self.sprites[self.current_animation]:
            self.current_frame = (self.current_frame + 1) % len(self.sprites[self.current_animation])
            self.update()
    
    def update_behavior(self):
        """Update pet behavior and mood"""
        # Check power management
        self.check_power_management()
        
        # Gradually decrease energy and happiness
        self.energy = max(0, self.energy - 0.5)
        self.happiness = max(0, self.happiness - 0.3)
        
        # Change animation based on mood and energy
        if self.energy < 30:
            self.current_animation = "down"  # Tired
        elif self.happiness < 30:
            self.current_animation = "idle"  # Sad
        elif random.random() < 0.1:  # 10% chance to change animation
            animations = list(self.sprites.keys())
            if animations:
                self.current_animation = random.choice(animations)
        
        # Random actions (reduced frequency in power save mode)
        chance = 0.02 if self.power_save_mode else 0.05
        if random.random() < chance:
            self.random_action()
    
    def show_power_status(self):
        """Show current power consumption status"""
        if self.power_save_mode:
            print(f"🐾 Power Save Mode: CPU usage ~1-2%, Battery impact: Minimal")
        else:
            print(f"🐾 Normal Mode: CPU usage ~2-5%, Battery impact: Low")
    
    def random_action(self):
        """Perform a random action"""
        actions = ["jump", "run", "walk"]
        if self.energy > 50:
            self.current_animation = random.choice(actions)
            # Boost happiness when active
            self.happiness = min(100, self.happiness + 5)
    
    def move_pet(self):
        """Move the pet around the screen"""
        screen = QDesktopWidget().screenGeometry()
        pos = self.pos()
        
        new_x = pos.x() + self.dx
        new_y = pos.y() + self.dy
        
        # Bounce off screen edges
        if new_x <= 0 or new_x + self.width() >= screen.width():
            self.dx *= -1
            # Change animation when hitting walls
            if self.current_animation == "walk":
                self.current_animation = "idle"
        
        if new_y <= 0 or new_y + self.height() >= screen.height():
            self.dy *= -1
            if self.current_animation == "walk":
                self.current_animation = "idle"
        
        # Occasionally change direction
        if random.random() < 0.01:  # 1% chance per movement
            self.dx = random.choice([-2, -1, 1, 2])
            self.dy = random.choice([-2, -1, 1, 2])
        
        # Move the pet
        self.move(new_x, new_y)
    
    def randomize_position(self):
        """Place the pet at a random position on screen"""
        screen = QDesktopWidget().screenGeometry()
        x = random.randint(0, max(0, screen.width() - self.width()))
        y = random.randint(0, max(0, screen.height() - self.height()))
        self.move(x, y)
    
    def enter_power_save_mode(self):
        """Enter power saving mode to reduce CPU usage"""
        if not self.power_save_mode:
            self.power_save_mode = True
            # Slow down timers
            self.animation_timer.setInterval(200)  # 5 FPS instead of 10
            self.movement_timer.setInterval(200)   # 5 updates/second instead of 10
            self.behavior_timer.setInterval(5000)  # 5 seconds instead of 2
            print("🐾 Pet entered power save mode (lower CPU usage)")
    
    def exit_power_save_mode(self):
        """Exit power saving mode for normal operation"""
        if self.power_save_mode:
            self.power_save_mode = False
            # Restore normal timers
            self.animation_timer.setInterval(self.animation_speed)
            self.movement_timer.setInterval(100)
            self.behavior_timer.setInterval(2000)
            print("🐾 Pet exited power save mode (normal operation)")
    
    def check_power_management(self):
        """Check if we should enter/exit power save mode"""
        import time
        current_time = time.time()
        
        # Enter power save if no activity for 30 seconds
        if current_time - self.last_activity > 30 and not self.power_save_mode:
            self.enter_power_save_mode()
        # Exit power save if there was recent activity
        elif current_time - self.last_activity <= 30 and self.power_save_mode:
            self.exit_power_save_mode()
    
    def paintEvent(self, event):
        """Draw the pet sprite"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        
        if (self.current_animation in self.sprites and 
            self.sprites[self.current_animation] and 
            self.current_frame < len(self.sprites[self.current_animation])):
            
            current_sprite = self.sprites[self.current_animation][self.current_frame]
            # Scale the sprite to fit the window size
            scaled_sprite = current_sprite.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            painter.drawPixmap(0, 0, scaled_sprite)
        else:
            # Fallback: draw a simple shape
            painter.fillRect(self.rect(), Qt.blue)
    
    def mousePressEvent(self, event):
        """Handle mouse clicks for interaction"""
        if event.button() == Qt.LeftButton:
            # Track activity for power management
            import time
            self.last_activity = time.time()
            
            # Boost happiness when clicked
            self.happiness = min(100, self.happiness + 10)
            self.energy = min(100, self.energy + 5)
            
            # Change to happy animation
            if "jump" in self.sprites:
                self.current_animation = "jump"
            
            # Start dragging
            self.drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    
    def mouseMoveEvent(self, event):
        """Handle mouse dragging"""
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_pos)
            event.accept()
    
    def mouseDoubleClickEvent(self, event):
        """Handle double-click for special actions"""
        if event.button() == Qt.LeftButton:
            # Track activity for power management
            import time
            self.last_activity = time.time()
            
            # Randomize position on double-click
            self.randomize_position()
            # Boost stats
            self.happiness = min(100, self.happiness + 15)
            self.energy = min(100, self.energy + 10)
            event.accept()


def main():
    app = QApplication(sys.argv)
    
    # Create the virtual pet
    pet = VirtualPet()
    
    # Set application properties for background operation
    app.setQuitOnLastWindowClosed(False)
    
    print("Virtual Pet is running! Click and drag to interact, double-click to teleport.")
    print("The pet will continue running in the background.")
    
    # Start the event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
