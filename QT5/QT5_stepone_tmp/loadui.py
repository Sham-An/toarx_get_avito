import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class ui(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("simple.ui",self)


app=QApplication(sys.argv)
window=ui()
window.show()
app.exec()