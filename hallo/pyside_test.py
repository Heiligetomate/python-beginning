import sys
from PySide6.QtWidgets import (QApplication,
                               QMainWindow, QPushButton, QVBoxLayout,
                               QWidget)
from PySide6.QtGui import QPalette
import random as r
colors = ['red', 'green', 'blue', 'magenta', 'cyan']


class MainWindow(QMainWindow):
    def __init__(self, window_title):
        super().__init__()

        # setup
        self.container = QWidget()
        self.setCentralWidget(self.container)

        self.frameLayout = QVBoxLayout()
        self.container.setLayout(self.frameLayout)

        self.show_sample_btn = QPushButton(text='Sample Window')
        self.frameLayout.addWidget(self.show_sample_btn)

        self.init_style()
        self.show()

    def init_style(self):
        newPalette = QPalette()
        newPalette.setColor(QPalette.Active, QPalette.Window, r.choice(colors))
        self.setPalette(newPalette)
        self.setStyleSheet(f"background-color:{r.choice(colors)};")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    win = MainWindow("testing")
    sys.exit(app.exec())