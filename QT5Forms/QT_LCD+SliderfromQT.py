from PySide2 import QtWidgets
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerSIrVKi.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(339, 321)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.verticalLayout_2.addWidget(self.lcdNumber)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalSlider)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_2.addWidget(self.progressBar)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 339, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.horizontalSlider.valueChanged.connect(lambda: self.on_change_func(self.horizontalSlider))
        self.horizontalSlider.valueChanged.connect(lambda: self.on_change_value(self.horizontalSlider))
        #self.horizontalSlider.valueChanged.connect(self.lcdNumber.display)
        #self.horizontalSlider.valueChanged.connect(self.progressBar.setValue)
        #self.horizontalSlider.valueChanged.connect(self.label.setNum)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
    # retranslateUi

    def on_change_func(self, slider):  # 7
        #pass
#        #if slider == self.slider_1:
#            #self.slider_2.setValue(self.slider_1.value())
            new_value = str(self.horizontalSlider.value())

            print('on_change_func' +new_value)
            #self.label.setText(str(self.horizontalSlider.value()+10))
#       #else:
#        #    self.slider_1.setValue(self.slider_2.value())
#        #    self.label.setText(str(self.slider_2.value()))
    def on_change_value(self, slider):
        new_value = str(self.horizontalSlider.value())
        print('on_change_value ' +new_value)
        self.label.setText(str(new_value))
        self.lcdNumber.display(new_value)
        self.progressBar.setValue(self.horizontalSlider.value())




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
