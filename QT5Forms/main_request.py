# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=CnMfhhx0GBI&list=PL0lO_mIqDDFXeDkOLHmEsL_HAEhw4-xDX&index=3

#Creeate LineEdit with Qt Designer - PyQt5 tutorial #7
#https://www.youtube.com/watch?v=7TMPaRnX6RQ
################################################################################

## Form generated from reading UI file 'calcbthNXo.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2 import QtWidgets
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *
from main_request_ui import *


class Request_board(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Создание формы и Ui (наш дизайн)
        self.setupUi(self)
        #self.checkBox.setObjectName("check_Box")
        #self.checkBox.setObjectName(u"CcheckBox")
        self.retranslateUi2(Ui_MainWindow)
        self.show()
        self.checkBox.setText('111')
        self.retranslateUi2(Ui_MainWindow)
        self.first_value = None
        self.second_value = None
        self.result = None
        self.example = ""
        self.equal = ""


    def retranslateUi2(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Main_Window", None))
        self.groupBox.setTitle(QCoreApplication.translate("Main_Window", u"GGroupBox", None))
        print("retranslateUi2")
        self.label.setText(QCoreApplication.translate("MainWindow", u"categoryId", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"locationId", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"searchRadius", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"priceMin", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"priceMax", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"sort", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"withImagesOnly", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"limit_page", None))
        self.label_result.setText(QCoreApplication.translate("MainWindow", u"result", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CCheckBox", None))


##################################################
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
