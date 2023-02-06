# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\group_radiobutton.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        # chicken
        self.radioButton.setObjectName("radioButton")

        self.radioButton.toggled.connect(self.item_selected)


        self.verticalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)

        # egg
        self.radioButton_2.setObjectName("radioButton_2")

        self.radioButton_2.toggled.connect(self.item_selected)

        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)

        # fish
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.toggled.connect(self.item_selected)

        self.verticalLayout_2.addWidget(self.radioButton_3)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)

        # water
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_4.toggled.connect(self.item_selected)
        self.verticalLayout.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_5.setFont(font)

        # lemon
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_5.toggled.connect(self.item_selected)
        self.verticalLayout.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_6.setFont(font)

        # tea
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_6.toggled.connect(self.item_selected)
        self.verticalLayout.addWidget(self.radioButton_6)
        self.verticalLayout_3.addWidget(self.splitter)
        self.label_result = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout_3.addWidget(self.label_result)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def item_selected(self):
        item1=""
        item2=""

        # item1
        if self.radioButton.isChecked()==True:
            item1="chicken"

        if self.radioButton_2.isChecked()==True:
            item1="egg"

        if self.radioButton_3.isChecked()==True:
            item1="fish"

        # item2
        if self.radioButton_4.isChecked()==True:
            item2="water"

        if self.radioButton_5.isChecked()==True:
            item2="lemon"

        if self.radioButton_6.isChecked()==True:
            item2="tea"

        self.label_result.setText("you order "+item1+" and "+ item2)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "food"))
        self.radioButton.setText(_translate("Dialog", "CHICKEN"))
        self.radioButton_2.setText(_translate("Dialog", "EGG"))
        self.radioButton_3.setText(_translate("Dialog", "FISH"))
        self.label_2.setText(_translate("Dialog", "drink"))
        self.radioButton_4.setText(_translate("Dialog", "WATER"))
        self.radioButton_5.setText(_translate("Dialog", "LEMON"))
        self.radioButton_6.setText(_translate("Dialog", "TEA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
