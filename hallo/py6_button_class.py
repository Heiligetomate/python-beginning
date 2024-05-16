import sys
from PySide6.QtWidgets import QApplication, QDialog, QFormLayout, QMessageBox
from PySide6.QtWidgets import (QPushButton, QLineEdit)


class Text_Box_With_Enter(QDialog):
    def __init__(self, hello_text):
        super().__init__()

        self.hello_text = hello_text

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
        self.text = ""

        self.setWindowTitle(self.hello_text)

    def button_click(self):
        self.text = self.line_edit.text()
        try:
            self.text = int(self.text)
            can_end = True
        except ValueError:
            QMessageBox.warning(self, "!!!", "Keine Zahl Eingegeben")

