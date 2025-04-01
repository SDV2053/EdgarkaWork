import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt

class HelpWindow(QWidget):
    def __init__(self):
        super().__init__()
        # ВИЗУАЛ
        self.setWindowTitle("⠀")
        self.setStyleSheet("background-color: black;")
        label = QLabel("SAME TEXT!", self)
        label.setStyleSheet("color: white; font-size: 30px; qproperty-alignment: AlignCenter;")
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.setAlignment(label, Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)
        self.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelpWindow()
    window.show()
    sys.exit(app.exec())