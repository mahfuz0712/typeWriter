import sys
import time
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, 
    QWidget, QLabel, QFileDialog
)
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QFont
import pyautogui

class CPPTypeWriter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Type Writer")
        self.resize(700, 400)
        
        self.file_path = None
        self.content = ""

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        title = QLabel("CPP Code Human Typer (Types in Active Window)")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Arial", 15, QFont.Weight.Bold))
        layout.addWidget(title)

        self.select_btn = QPushButton("1. Select CPP File")
        self.select_btn.clicked.connect(self.select_file)
        layout.addWidget(self.select_btn)

        self.write_btn = QPushButton("2. Start Typing (10s delay)")
        self.write_btn.clicked.connect(self.start_typing)
        self.write_btn.setEnabled(False)
        layout.addWidget(self.write_btn)

        self.status = QLabel("Status: No file selected")
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status)

        # Warning
        warning = QLabel("⚠️ Make sure your code editor is active and ready before clicking Start")
        warning.setStyleSheet("color: red;")
        warning.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(warning)

    def select_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Select C++ File", "", "C++ Files (*.cpp *.h);;All Files (*)"
        )
        if file_name:
            self.file_path = file_name
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    self.content = f.read()
                self.status.setText(f"Loaded: {file_name.split('/')[-1]} ({len(self.content)} chars)")
                self.write_btn.setEnabled(True)
            except Exception as e:
                self.status.setText(f"Error: {str(e)}")

    def start_typing(self):
        if not self.content:
            return

        self.write_btn.setEnabled(False)
        self.status.setText("Waiting 10 seconds... Switch to your code editor now!")
        
        # 10 second delay
        QTimer.singleShot(10000, self.type_in_active_window)

    def type_in_active_window(self):
        self.status.setText("Typing started... Do NOT move mouse or switch window!")
        
        pyautogui.PAUSE = 0.01  # Small delay between actions

        for char in self.content:
            try:
                pyautogui.typewrite(char)
                # Random small delay to look more human
                if char in '\n':
                    time.sleep(0.15)
                elif char in ' ':
                    time.sleep(0.03)
                else:
                    time.sleep(0.02)
            except Exception:
                break  # Stop if something goes wrong

        self.status.setText("Typing completed!")
        self.write_btn.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CPPTypeWriter()
    window.show()
    sys.exit(app.exec())