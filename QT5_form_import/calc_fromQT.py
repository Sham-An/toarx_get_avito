# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=CnMfhhx0GBI&list=PL0lO_mIqDDFXeDkOLHmEsL_HAEhw4-xDX&index=3

################################################################################
## Form generated from reading UI file 'calcbthNXo.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2 import QtWidgets

import sys
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *
from calc_ui_PySide import *


class Calculator(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        # Создание формы и Ui (наш дизайн)
        self.setupUi(self)
        self.show()
        #        self.lineEdit.setText('0')

        self.first_value = None
        self.second_value = None
        self.result = None
        self.example = ""
        self.equal = ""

    ##############################################
    # # super().__init__()
    #  # Создание формы и Ui (наш дизайн)
    #  self.setupUi(self)
    #  self.show()
    #  #        self.lineEdit.setText('0')
    #
    #  self.first_value = None
    #  self.second_value = None
    #  self.result = None
    #  self.example = ""
    #  self.equal = ""

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


##################################################
if __name__ == "__main__":
    main()
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
