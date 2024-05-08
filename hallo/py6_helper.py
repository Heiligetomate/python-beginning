from PySide6.QtWidgets import QWidget,QPushButton,QHBoxLayout,QVBoxLayout


class RocWidget (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")
        self.a = 0
        self.b = 0
        button1 = QPushButton("Button1")
        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton("Button2")
        button2.clicked.connect(self.button2_clicked)
        button3 = QPushButton("show")
        button3.clicked.connect(self.button3_clicked)
        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        button_layout.addWidget(button3)

        self.setLayout(button_layout)

    def button1_clicked(self):
        #print("Button1 clicked")
        self.a += 1

    def button2_clicked(self):
        #print("Button2 clicked")
        self.b += 1

    def button3_clicked(self):
        print(self.a)
        print(self.b)