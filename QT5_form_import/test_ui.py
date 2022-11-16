import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5 import uic

class Widget(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi("test.ui", self)
        self.label.setText("New__Text")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())