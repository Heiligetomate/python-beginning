from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class RocWidget(QWidget):
    text = ""
    next_window = True

    def __init__(self, width, height):
        super().__init__()
        self.setWindowTitle("RockWidget")
        self.resize(width, height)
        button_layout = QVBoxLayout()

        button1 = QPushButton("a")
        button1.clicked.connect(self.button1_clicked)
        button_layout.addWidget(button1)

        button2 = QPushButton("Dont Press Me")
        button2.clicked.connect(self.button2_clicked)
        button_layout.addWidget(button2)

        self.setLayout(button_layout)

    def button1_clicked(self):
        RocWidget.text += "a"

    def button2_clicked(self):
        RocWidget.next_window = False
