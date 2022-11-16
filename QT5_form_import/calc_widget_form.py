# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calc_widgetSFuHLC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_w_app(object):
    def setupUi(self, w_app):
        if not w_app.objectName():
            w_app.setObjectName(u"w_app")
        w_app.resize(350, 400)
        w_app.setMinimumSize(QSize(350, 400))
        w_app.setMaximumSize(QSize(350, 400))
        w_app.setStyleSheet(u"background-color: rgb(252, 216, 255);")
        self.l_display = QLabel(w_app)
        self.l_display.setObjectName(u"l_display")
        self.l_display.setGeometry(QRect(20, 50, 291, 51))
        font = QFont()
        font.setPointSize(26)
        self.l_display.setFont(font)
        self.l_display.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(85, 255, 127);")
        self.l_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.widget = QWidget(w_app)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 110, 331, 264))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_9 = QPushButton(self.widget)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setMinimumSize(QSize(61, 61))
        self.btn_9.setMaximumSize(QSize(61, 61))
        self.btn_9.setStyleSheet(u"background-color: rgb(169, 143, 255);")

        self.gridLayout.addWidget(self.btn_9, 0, 2, 1, 1)

        self.btn_1 = QPushButton(self.widget)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setMinimumSize(QSize(61, 61))
        self.btn_1.setMaximumSize(QSize(61, 61))
        self.btn_1.setStyleSheet(u"background-color: rgb(169, 143, 255);")

        self.gridLayout.addWidget(self.btn_1, 2, 0, 1, 1)

        self.btn_8 = QPushButton(self.widget)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setMinimumSize(QSize(61, 61))
        self.btn_8.setMaximumSize(QSize(61, 61))
        self.btn_8.setStyleSheet(u"background-color: rgb(169, 143, 255);")

        self.gridLayout.addWidget(self.btn_8, 0, 1, 1, 1)

        self.btn_4 = QPushButton(self.widget)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setMinimumSize(QSize(61, 61))
        self.btn_4.setMaximumSize(QSize(61, 61))
        self.btn_4.setStyleSheet(u"background-color: rgb(169, 143, 255);")

        self.gridLayout.addWidget(self.btn_4, 1, 0, 1, 1)

        self.btn_2 = QPushButton(self.widget)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setMinimumSize(QSize(61, 61))
        self.btn_2.setMaximumSize(QSize(61, 61))
        self.btn_2.setStyleSheet(u"background-color: rgb(169, 143, 255);")

        self.gridLayout.addWidget(self.btn_2, 2, 1, 1, 1)

        self.btn_3 = QPushButton(self.widget)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setMinimumSize(QSize(61, 61))
        self.btn_3.setMaximumSize(QSize(61, 61))
        self.btn_3.setStyleSheet(u"background-color: rgb(169, 143, 255);")

        self.gridLayout.addWidget(self.btn_3, 2, 2, 1, 1)

        self.btn_7 = QPushButton(self.widget)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setMinimumSize(QSize(61, 61))
        self.btn_7.setMaximumSize(QSize(61, 61))
        self.btn_7.setStyleSheet(u"background-color: rgb(169, 143, 255);")

        self.gridLayout.addWidget(self.btn_7, 0, 0, 1, 1)

        self.btn_x = QPushButton(self.widget)
        self.btn_x.setObjectName(u"btn_x")
        self.btn_x.setMinimumSize(QSize(61, 61))
        self.btn_x.setMaximumSize(QSize(61, 61))
        self.btn_x.setStyleSheet(u"background-color: rgb(169, 143, 255);")

        self.gridLayout.addWidget(self.btn_x, 2, 3, 1, 1)

        self.btn_eq = QPushButton(self.widget)
        self.btn_eq.setObjectName(u"btn_eq")
        self.btn_eq.setMinimumSize(QSize(61, 61))
        self.btn_eq.setMaximumSize(QSize(61, 61))
        self.btn_eq.setStyleSheet(u"background-color: rgb(169, 143, 255);")

        self.gridLayout.addWidget(self.btn_eq, 3, 1, 1, 1)

        self.btn_d = QPushButton(self.widget)
        self.btn_d.setObjectName(u"btn_d")
        self.btn_d.setMinimumSize(QSize(61, 61))
        self.btn_d.setMaximumSize(QSize(61, 61))
        self.btn_d.setStyleSheet(u"background-color: rgb(169, 143, 255);")

        self.gridLayout.addWidget(self.btn_d, 1, 3, 1, 1)

        self.btn_5 = QPushButton(self.widget)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setMinimumSize(QSize(61, 61))
        self.btn_5.setMaximumSize(QSize(61, 61))
        self.btn_5.setStyleSheet(u"background-color: rgb(169, 143, 255);")

        self.gridLayout.addWidget(self.btn_5, 1, 1, 1, 1)

        self.btn_6 = QPushButton(self.widget)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setMinimumSize(QSize(61, 61))
        self.btn_6.setMaximumSize(QSize(61, 61))
        self.btn_6.setStyleSheet(u"background-color: rgb(169, 143, 255);")

        self.gridLayout.addWidget(self.btn_6, 1, 2, 1, 1)

        self.btn_0 = QPushButton(self.widget)
        self.btn_0.setObjectName(u"btn_0")
        self.btn_0.setMinimumSize(QSize(61, 61))
        self.btn_0.setMaximumSize(QSize(61, 61))
        self.btn_0.setStyleSheet(u"background-color: rgb(169, 143, 255);")

        self.gridLayout.addWidget(self.btn_0, 3, 0, 1, 1)

        self.btn_min = QPushButton(self.widget)
        self.btn_min.setObjectName(u"btn_min")
        self.btn_min.setMinimumSize(QSize(61, 61))
        self.btn_min.setMaximumSize(QSize(61, 61))
        self.btn_min.setStyleSheet(u"background-color: rgb(169, 143, 255);")

        self.gridLayout.addWidget(self.btn_min, 3, 3, 1, 1)

        self.btn_plus = QPushButton(self.widget)
        self.btn_plus.setObjectName(u"btn_plus")
        self.btn_plus.setMinimumSize(QSize(61, 61))
        self.btn_plus.setMaximumSize(QSize(61, 61))
        self.btn_plus.setStyleSheet(u"background-color: rgb(169, 143, 255);")

        self.gridLayout.addWidget(self.btn_plus, 3, 2, 1, 1)

        self.btn_clear = QPushButton(self.widget)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMinimumSize(QSize(61, 61))
        self.btn_clear.setMaximumSize(QSize(61, 61))
        self.btn_clear.setStyleSheet(u"background-color: rgb(169, 143, 255);")

        self.gridLayout.addWidget(self.btn_clear, 0, 3, 1, 1)


        self.retranslateUi(w_app)

        QMetaObject.connectSlotsByName(w_app)
    # setupUi

    def retranslateUi(self, w_app):
        w_app.setWindowTitle(QCoreApplication.translate("w_app", u"Form", None))
        self.l_display.setText(QCoreApplication.translate("w_app", u"0", None))
        self.btn_9.setText(QCoreApplication.translate("w_app", u"9", None))
        self.btn_1.setText(QCoreApplication.translate("w_app", u"1", None))
        self.btn_8.setText(QCoreApplication.translate("w_app", u"8", None))
        self.btn_4.setText(QCoreApplication.translate("w_app", u"4", None))
        self.btn_2.setText(QCoreApplication.translate("w_app", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("w_app", u"3", None))
        self.btn_7.setText(QCoreApplication.translate("w_app", u"7", None))
        self.btn_x.setText(QCoreApplication.translate("w_app", u"X", None))
        self.btn_eq.setText(QCoreApplication.translate("w_app", u"=", None))
        self.btn_d.setText(QCoreApplication.translate("w_app", u"/", None))
        self.btn_5.setText(QCoreApplication.translate("w_app", u"5", None))
        self.btn_6.setText(QCoreApplication.translate("w_app", u"6", None))
        self.btn_0.setText(QCoreApplication.translate("w_app", u"0", None))
        self.btn_min.setText(QCoreApplication.translate("w_app", u"-", None))
        self.btn_plus.setText(QCoreApplication.translate("w_app", u"+", None))
        self.btn_clear.setText(QCoreApplication.translate("w_app", u"C", None))
    # retranslateUi

