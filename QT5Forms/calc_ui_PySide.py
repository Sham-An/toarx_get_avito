# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calcypHOWf.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(362, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_result = QLabel(self.centralwidget)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setGeometry(QRect(0, -1, 361, 61))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet(u"background-color: rgb(170, 170, 170);\n"
"color: rgb(255, 255, 255);")
        self.label_result.setMargin(10)
        self.btn_zero = QPushButton(self.centralwidget)
        self.btn_zero.setObjectName(u"btn_zero")
        self.btn_zero.setGeometry(QRect(0, 330, 151, 71))
        self.btn_equal = QPushButton(self.centralwidget)
        self.btn_equal.setObjectName(u"btn_equal")
        self.btn_equal.setGeometry(QRect(150, 330, 151, 71))
        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setGeometry(QRect(0, 240, 100, 90))
        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setGeometry(QRect(100, 240, 100, 90))
        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setGeometry(QRect(200, 240, 100, 90))
        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setGeometry(QRect(200, 150, 100, 90))
        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setGeometry(QRect(100, 150, 100, 90))
        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setGeometry(QRect(0, 150, 100, 90))
        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setGeometry(QRect(200, 60, 100, 90))
        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setGeometry(QRect(100, 60, 100, 90))
        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setGeometry(QRect(0, 60, 100, 90))
        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setObjectName(u"btn_plus")
        self.btn_plus.setGeometry(QRect(300, 60, 61, 90))
        self.btn_minus = QPushButton(self.centralwidget)
        self.btn_minus.setObjectName(u"btn_minus")
        self.btn_minus.setGeometry(QRect(300, 150, 61, 90))
        self.btn_mult = QPushButton(self.centralwidget)
        self.btn_mult.setObjectName(u"btn_mult")
        self.btn_mult.setGeometry(QRect(300, 240, 61, 90))
        self.btn_divide = QPushButton(self.centralwidget)
        self.btn_divide.setObjectName(u"btn_divide")
        self.btn_divide.setGeometry(QRect(300, 330, 61, 71))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        #self.btn_zero.clicked.connect(self.label_result.update)

        QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()
        self.is_equal = False
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u043a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.label_result.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_zero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_mult.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.btn_divide.setText(QCoreApplication.translate("MainWindow", u"/", None))
    # retranslateUi


    def add_functions(self):
        #self.btn_zero.clicked.connect()
        self.btn_zero.clicked.connect(lambda: self.write_number(self.btn_zero.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
        self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))
        self.btn_mult.clicked.connect(lambda: self.write_number(self.btn_mult.text()))
        self.btn_divide.clicked.connect(lambda: self.write_number(self.btn_divide.text()))


        self.btn_equal.clicked.connect(self.results)

    def write_number(self, number):
        #print(number)
        if self.label_result.text() == "0" or self.is_equal:
            self.label_result.setText(number)
            self.is_equal = False
        else:
            self.label_result.setText(self.label_result.text() + number)

    def results(self):
        res = eval(self.label_result.text())
        self.label_result.setText("Результат: " + str(res))
        self.is_equal = True