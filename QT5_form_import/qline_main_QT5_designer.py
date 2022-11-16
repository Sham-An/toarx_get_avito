#from PyQt5 import QtWidgets, QtCore, QtGui
from PySide2 import QtWidgets
from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


# Импортируем наш файл
from qline_form_QT5_designer import Ui_MainWindow
import sys

# if 'PyQt5' in sys.modules: #if 'PyQt6' in sys.modules:
#     # PyQt6
#     from PyQt5 import QtGui, QtWidgets, QtCore
#     from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
#
# else:
#     # PySide5
#     from PySide5 import QtGui, QtWidgets, QtCore
#     from PySide5.QtCore import Signal, Slot
#https://python-scripts.com/pyqt5?ysclid=lagg1me49i992191830#load-ui-convert-to-py
#pyside6-uic mainwindow.ui -o MainWindow.py
#     pyuic6 mainwindow.ui -o MainWindow.py
# my_custom_signal = pyqtSignal()  # PyQt6
# my_custom_signal = Signal()  # PySide6
#
# my_other_signal = pyqtSignal(int)  # PyQt6
# my_other_signal = Signal(int)  # PySide6
#
# @pyqtslot
# def my_custom_slot():
#     pass
#
# @Slot
# def my_custom_slot():
#     pass


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Меняем текст Для 1-го QLineEdit
        self.ui.lineEdit.setText("Добро пожаловать на PythonScripts")

        # указать максимальную длину Для 2-го QLineEdit
        self.ui.lineEdit_2.setMaxLength(10)

        # ввод пароля Для 3-го QLineEdit
        self.ui.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        # только чтение без изменения содержимого.
        self.ui.lineEdit_4.setReadOnly(True)

        # меняем цвет вводимого текста
        self.ui.lineEdit_5.setStyleSheet("color: rgb(28, 43, 255);")

        # изменение цвета фона QLineEdit
        self.ui.lineEdit_6.setStyleSheet("background-color: rgb(28, 43, 255);")

        font = QFont()
        font.setFamily("SansSerif")
        font.setPointSize(15)
        self.ui.label.setFont(font)
        self.ui.label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.ui.label.setTextFormat(Qt.PlainText)
        #self.ui.label.setFont(QtGui.QFont('SansSerif', 13))  # Изменение шрифта и размера

        #self.ui.label.setFont(QFont('SansSerif', 10))  # Изменение шрифта и размера
        #self.ui.label.setText("PyScripts")  # Меняем текст

        ######################## BUTTON
        self.ui.pushButton.setText(u"Button1")
        #Слоты и сигналы Перетяните QPushButton и QLineEdit в вашу форму.
        #Нажмите F4 и перетяните курсор из QPushButton и отпустите его в верхней
        # части QLineEdit. Чтобы вернуться в обычный режим, нажмите на F3.
        #Визуальный редактор слота/сигнала
        #https://python-scripts.com/pyqt5?ysclid=lagg1me49i992191830#signal-slot-editor
        self.ui.pushButton.clicked.connect(self.btnClicked)
        ########################## BUTTON2
        self.ui.btn_2.setText(u"Button2")
        self.ui.btn_2.clicked.connect(lambda: self.write_number(self.ui.btn_2.text()))
        #self.btn_2.clicked.connect(self.label.clear)
        self.retranslateUi(self) #MainWindow)


    def retranslateUi(self, MainWindow):
        #pass
        #MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u043a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow",
                                                             u"Настройка запроса",
                                                             None))
        #self.ui.setWindowTitle(QCoreApplication.translate("MainWindow", u"Main_Window", None))
        #self.label_result.setText(QCoreApplication.translate("MainWindow", u"0", None))
        #self.btn_zero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        #self.btn_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        #self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.ui.btn_2.setText(QCoreApplication.translate("Main_Window", u"2", None))

    def btnClicked(self):
        self.ui.label.setText("Вы нажали на кнопку 1!")
        # Если не использовать, то часть текста исчезнет.
        self.ui.label.adjustSize()


    def add_functions(self):
        #self.btn_zero.clicked.connect()
        #self.btn_zero.clicked.connect(lambda: self.write_number(self.btn_zero.text()))
        #self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))

    def write_number(self, number):
        #print(self.ui.label.text())
        print(number)
        # if self.label_result.text() == "0" or self.is_equal:
        #     self.label_result.setText(number)
        #     self.is_equal = False
        # else:
        self.ui.label.setText(self.ui.label.text()+number)
        #self.ui.label.setText(number)



# if __name__ == "__main__":
    # if 'PyQt5' in sys.modules:  # if 'PyQt6' in sys.modules:
    #     # PyQt6
    #     from PyQt5 import QtGui, QtWidgets, QtCore
    #     from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
    #
    # else:
    #     # PySide5
    #     from PySide2 import QtGui, QtWidgets, QtCore
    #     from PySide2.QtCore import Signal, Slot

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec_())
