# -*- coding: utf-8 -*-
#https://www.youtube.com/watch?v=90xZtB3bbcg

from PySide2 import QtWidgets

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
import sys
from PySide2.QtWidgets import *
#from calc_ui_PySide import *
#from PySide2 import uic
from PyQt5 import uic
from calc_widget_form import Ui_w_app #as clc

import os

class App(QWidget):
    #def __init__(self):
        def __init__(self):
            self.start()

        def start(self):
            self.ui = uic.loadUi('calc_widget_form.ui')
            self.ui = Ui_w_app(self)
            #self.ui = QMainWindow()
            self.ui.setupUi(self)
            self.ui.show()
            #self.show()


def main():
    #app = QtWidgets.QApplication(sys.argv)
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()

    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    sys.exit(app.exec_())


##################################################
if __name__ == "__main__":
    main()