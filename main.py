import sys
import random
from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QApplication, QWidget


class Pet(QWidget):
    def __init__(self, sprite_path = r"C:\Users\Hp\Desktop\sample projects\virtualPet\sprites\pet.png"):
        super().__init__()

        # Load pet sprite
        self.pet_pixmap = QPixmap(sprite_path)

        # Remove window borders, make it float on desktop
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint |
            Qt.FramelessWindowHint |
            Qt.Tool
        )

        # Make background transparent
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # Resize window to fit sprite
        self.resize(self.pet_pixmap.size())

        # Movement vars
        self.dx = random.choice([-3, -2, -1, 1, 2, 3])
        self.dy = random.choice([-3, -2, -1, 1, 2, 3])

        # Start a timer to animate movement
        self.timer = QTimer()
        self.timer.timeout.connect(self.move_pet)
        self.timer.start(30)  # ~33 FPS

        # Show pet
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pet_pixmap)

    def move_pet(self):
        screen = QApplication.desktop().screenGeometry()
        pos = self.pos()

        new_x = pos.x() + self.dx
        new_y = pos.y() + self.dy

        # Bounce off screen edges
        if new_x < 0 or new_x + self.width() > screen.width():
            self.dx *= -1
        if new_y < 0 or new_y + self.height() > screen.height():
            self.dy *= -1

        self.move(new_x, new_y)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Drag pet with mouse
            self.drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # Follow mouse while dragging
            self.move(event.globalPos() - self.drag_pos)
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pet = Pet("pet.png")  # put your sprite file here
    sys.exit(app.exec_())
