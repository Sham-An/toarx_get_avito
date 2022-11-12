#!/usr/bin/python3wxpython
# -*- coding: utf-8 -*-

import os
import sys

from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QTextEdit,
                             QAction, QFileDialog)


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()


    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '')[0]

        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)

class Form(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.plainTextEdit = QPlainTextEdit()
        self.plainTextEdit.setFont(QFont('Arial', 11))

        openDirButton = QPushButton("Open Directory")
        openDirButton.clicked.connect(self.getDirectory)

        getFileNameButton = QPushButton("Open File")
        getFileNameButton.clicked.connect(self.getFileName)

        getFileNamesButton = QPushButton("Open Files")
        getFileNamesButton.clicked.connect(self.getFileNames)

        saveFileNameButton = QPushButton("Save File")
        saveFileNameButton.clicked.connect(self.saveFile)

        layoutV = QVBoxLayout()
        layoutV.addWidget(openDirButton)
        layoutV.addWidget(getFileNameButton)
        layoutV.addWidget(getFileNamesButton)
        layoutV.addWidget(saveFileNameButton)

        layoutH = QHBoxLayout()
        layoutH.addLayout(layoutV)
        layoutH.addWidget(self.plainTextEdit)

        centerWidget = QWidget()
        centerWidget.setLayout(layoutH)
        self.setCentralWidget(centerWidget)

        self.resize(740, 480)
        self.setWindowTitle("PyQt5-QFileDialog")

    def getDirectory(self):  # <-----
        dirlist = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        self.plainTextEdit.appendHtml("<br>Выбрали папку: <b>{}</b>".format(dirlist))

    def getFileName(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         ".",
                                                         "Text Files(*.txt);;JPEG Files(*.jpeg);;\
                                                         PNG Files(*.png);;GIF File(*.gif);;All Files(*)")
        self.plainTextEdit.appendHtml("<br>Выбрали файл: <b>{}</b> <br> <b>{:*^54}</b>"
                                      "".format(filename, filetype))

    def getFileNames(self):
        filenames, ok = QFileDialog.getOpenFileNames(self,
                                                     "Выберите несколько файлов",
                                                     ".",
                                                     "All Files(*.*)")
        self.plainTextEdit.appendHtml("""<br>Выбрали несколько файлов: 
                                       <b>{}</b> <br> <b>{:*^80}</b>"""
                                      "".format(filenames, ok))

        folder = os.path.dirname(filenames[0])
        print("folder =", folder)
        self.plainTextEdit.appendHtml("""<br>пути файлов, которые я выбираю: 
                                       <b>{}</b> """
                                      "".format(folder))

    def saveFile(self):
        filename, ok = QFileDialog.getSaveFileName(self,
                                                   "Сохранить файл",
                                                   ".",
                                                   "All Files(*.*)")
        self.plainTextEdit.appendHtml("<br>Сохранить файл: <b>{}</b> <br> <b>{:*^54}</b>"
                                      "".format(filename, ok))



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex2 = Form()
    ex2.show()

    sys.exit(app.exec_())