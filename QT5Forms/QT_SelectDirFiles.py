import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        MainWindow.setMinimumSize(QtCore.QSize(500, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowse.setGeometry(QtCore.QRect(0, 0, 131, 23))
        self.btnBrowse.setObjectName("btnBrowse")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 20, 331, 151))
        self.listWidget.setObjectName("listWidget")
        self.btnArch = QtWidgets.QPushButton(self.centralwidget)
        self.btnArch.setGeometry(QtCore.QRect(110, 180, 81, 23))
        self.btnArch.setObjectName("btnArch")
        self.extractButton = QtWidgets.QPushButton(self.centralwidget)
        self.extractButton.setGeometry(QtCore.QRect(380, 0, 81, 23))
        self.extractButton.setObjectName("extractButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnBrowse.setText(_translate("MainWindow", "Выбрать ..."))
        self.btnArch.setText(_translate("MainWindow", "Архивировать"))
        self.extractButton.setText(_translate("MainWindow", "Извлечь"))


def getOpenFilesAndDirs(parent=None, caption='', directory='',
                        filter='', initialFilter='', options=None):
    def updateText():
        # обновить содержимое виджета редактирования строки выбранными файлами
        selected = []
        for index in view.selectionModel().selectedRows():
            selected.append('"{}"'.format(index.data()))
        lineEdit.setText(' '.join(selected))

    dialog = QtWidgets.QFileDialog(parent, windowTitle=caption)
    dialog.setFileMode(dialog.ExistingFiles)
    if options:
        dialog.setOptions(options)
    dialog.setOption(dialog.DontUseNativeDialog, True)  # !!!
    if directory:
        dialog.setDirectory(directory)
    if filter:
        dialog.setNameFilter(filter)
        if initialFilter:
            dialog.selectNameFilter(initialFilter)

    # по умолчанию, если каталог открыт в режиме списка файлов,
    # QFileDialog.accept() показывает содержимое этого каталога,
    # но нам нужно иметь возможность "открывать" и каталоги, как мы можем делать с файлами,
    # поэтому мы просто переопределяем `accept()` с реализацией QDialog по умолчанию,
    # которая просто вернет `dialog.selectedFiles()`

    dialog.accept = lambda: QtWidgets.QDialog.accept(dialog)

    # в неродном диалоге есть много представлений элементов,
    # но те, которые отображают фактическое содержимое, создаются внутри QStackedWidget;
    # это QTreeView и QListView, и дерево используется только тогда,
    # когда viewMode установлен на QFileDialog.Details, что не в этом случае.

    stackedWidget = dialog.findChild(QtWidgets.QStackedWidget)
    view = stackedWidget.findChild(QtWidgets.QListView)
    view.selectionModel().selectionChanged.connect(updateText)

    lineEdit = dialog.findChild(QtWidgets.QLineEdit)
    # очищаем содержимое строки редактирования всякий раз, когда изменяется текущий каталог
    dialog.directoryEntered.connect(lambda: lineEdit.setText(''))

    dialog.exec_()
    return dialog.selectedFiles()


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnBrowse.clicked.connect(self.browse_folder)
        self.btnArch.clicked.connect(self.arch_folder)
        self.extractButton.clicked.connect(self.extract)

    def browse_folder(self):
        selected_files = getOpenFilesAndDirs()
        print(selected_files)
        if selected_files:
            self.listWidget.addItems(selected_files)
        else:
            msg = QtWidgets.QMessageBox.information(self, 'Message', 'Вы ничего не выбрали.')

    def arch_folder(self):
        print(f'Выполнить Архивирование: ...')

    def extract(self):
        print(f'Что-то Извлечь:  ...')


import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        MainWindow.setMinimumSize(QtCore.QSize(500, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowse.setGeometry(QtCore.QRect(0, 0, 131, 23))
        self.btnBrowse.setObjectName("btnBrowse")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 20, 331, 151))
        self.listWidget.setObjectName("listWidget")
        self.btnArch = QtWidgets.QPushButton(self.centralwidget)
        self.btnArch.setGeometry(QtCore.QRect(110, 180, 81, 23))
        self.btnArch.setObjectName("btnArch")
        self.extractButton = QtWidgets.QPushButton(self.centralwidget)
        self.extractButton.setGeometry(QtCore.QRect(380, 0, 81, 23))
        self.extractButton.setObjectName("extractButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnBrowse.setText(_translate("MainWindow", "Выбрать ..."))
        self.btnArch.setText(_translate("MainWindow", "Архивировать"))
        self.extractButton.setText(_translate("MainWindow", "Извлечь"))


def getOpenFilesAndDirs(parent=None, caption='', directory='',
                        filter='', initialFilter='', options=None):
    def updateText():
        # обновить содержимое виджета редактирования строки выбранными файлами
        selected = []
        for index in view.selectionModel().selectedRows():
            selected.append('"{}"'.format(index.data()))
        lineEdit.setText(' '.join(selected))

    dialog = QtWidgets.QFileDialog(parent, windowTitle=caption)
    dialog.setFileMode(dialog.ExistingFiles)
    if options:
        dialog.setOptions(options)
    dialog.setOption(dialog.DontUseNativeDialog, True)  # !!!
    if directory:
        dialog.setDirectory(directory)
    if filter:
        dialog.setNameFilter(filter)
        if initialFilter:
            dialog.selectNameFilter(initialFilter)

    # по умолчанию, если каталог открыт в режиме списка файлов,
    # QFileDialog.accept() показывает содержимое этого каталога,
    # но нам нужно иметь возможность "открывать" и каталоги, как мы можем делать с файлами,
    # поэтому мы просто переопределяем `accept()` с реализацией QDialog по умолчанию,
    # которая просто вернет `dialog.selectedFiles()`

    dialog.accept = lambda: QtWidgets.QDialog.accept(dialog)

    # в неродном диалоге есть много представлений элементов,
    # но те, которые отображают фактическое содержимое, создаются внутри QStackedWidget;
    # это QTreeView и QListView, и дерево используется только тогда,
    # когда viewMode установлен на QFileDialog.Details, что не в этом случае.

    stackedWidget = dialog.findChild(QtWidgets.QStackedWidget)
    view = stackedWidget.findChild(QtWidgets.QListView)
    view.selectionModel().selectionChanged.connect(updateText)

    lineEdit = dialog.findChild(QtWidgets.QLineEdit)
    # очищаем содержимое строки редактирования всякий раз, когда изменяется текущий каталог
    dialog.directoryEntered.connect(lambda: lineEdit.setText(''))

    dialog.exec_()
    return dialog.selectedFiles()


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnBrowse.clicked.connect(self.browse_folder)
        self.btnArch.clicked.connect(self.arch_folder)
        self.extractButton.clicked.connect(self.extract)

    def browse_folder(self):
        selected_files = getOpenFilesAndDirs()
        print(selected_files)
        if selected_files:
            self.listWidget.addItems(selected_files)
        else:
            msg = QtWidgets.QMessageBox.information(self, 'Message', 'Вы ничего не выбрали.')

    def arch_folder(self):
        print(f'Выполнить Архивирование: ...')

    def extract(self):
        print(f'Что-то Извлечь:  ...')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    sys.exit(app.exec_())