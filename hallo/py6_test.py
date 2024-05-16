import sys
from PySide6.QtWidgets import QApplication, QDialog, QFormLayout, QMessageBox
from PySide6.QtWidgets import (QPushButton, QLineEdit)


class Make_laberrababer(QDialog):
    def __init__(self, width, height):
        super().__init__()

        self.resize(width, height)
        self.line_edit = QLineEdit()
        self.line_edit.setObjectName("host")
        self.line_edit.setText("")

        self.push_button = QPushButton()
        self.push_button.setObjectName("connect")
        self.push_button.setText("Connect")
        self.push_button.clicked.connect(self.button_click)

        layout = QFormLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.push_button)
        self.setLayout(layout)

    def button_click(self):
        QMessageBox.warning(self, "!!!", "WARUM????")

