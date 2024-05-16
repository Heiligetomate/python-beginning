from PySide6.QtWidgets import QApplication, QWidget
from py6_helper import RocWidget
from py6_button_class import Text_Box_With_Enter
from py6_test import Make_laberrababer
import sys


app = QApplication(sys.argv)

ask_for_width = Text_Box_With_Enter("Please Type in Screen Width")
ask_for_width.show()
ask_for_width.exec()

ask_for_height = Text_Box_With_Enter("Please Type in Screen Height")
ask_for_height.show()
ask_for_height.exec()

window = Make_laberrababer(ask_for_width.text, ask_for_height.text)
window.show()

app.exec()
print(RocWidget.text)


