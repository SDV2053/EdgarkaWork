import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class HelpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.BACKGROUND_COLOR = "black"
        self.TEXT_COLOR = "white"
        self.FONT_SIZE = 30
        self.WINDOW_TITLE = "Help Window"
        self.WINDOW_WIDTH = 400
        self.WINDOW_HEIGHT = 200
        self.setWindowTitle(self.WINDOW_TITLE)
        self.setStyleSheet(f"background-color: {self.BACKGROUND_COLOR};")
        self.setFixedSize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.center_window()
        label = QLabel("SAME TEXT!")
        label.setStyleSheet(f"color: {self.TEXT_COLOR}; font-size: {self.FONT_SIZE}px;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setFont(QFont("Arial", self.FONT_SIZE))
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

    def center_window(self):
        screen_geometry = QApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelpWindow()
    window.show()
    sys.exit(app.exec())