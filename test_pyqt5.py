#!/usr/bin/env python3
"""
Simple PyQt5 test to verify the installation is working correctly
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

def test_pyqt5():
    """Test basic PyQt5 functionality"""
    try:
        # Create application
        app = QApplication(sys.argv)
        
        # Create main window
        window = QWidget()
        window.setWindowTitle("PyQt5 Test - Virtual Pet")
        window.setGeometry(100, 100, 400, 200)
        
        # Create layout
        layout = QVBoxLayout()
        
        # Create labels
        title_label = QLabel("🐾 PyQt5 Test Successful!")
        title_label.setFont(QFont("Arial", 16))
        title_label.setAlignment(Qt.AlignCenter)
        
        info_label = QLabel("PyQt5 is working correctly!\nYour virtual pet should work fine.")
        info_label.setAlignment(Qt.AlignCenter)
        
        # Add labels to layout
        layout.addWidget(title_label)
        layout.addWidget(info_label)
        
        # Set layout
        window.setLayout(layout)
        
        # Show window
        window.show()
        
        print("✅ PyQt5 test successful! Starting application...")
        
        # Start event loop
        sys.exit(app.exec_())
        
    except Exception as e:
        print(f"❌ PyQt5 test failed: {e}")
        print("This indicates a PyQt5 installation problem.")
        return False

if __name__ == "__main__":
    test_pyqt5()
