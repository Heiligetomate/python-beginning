from PySide6.QtWidgets import QApplication, QWidget
from py6_helper import RocWidget

import sys
app = QApplication(sys.argv)

window = RocWidget()
window.show()

app.exec()
print(window.a)
print(window.b)

