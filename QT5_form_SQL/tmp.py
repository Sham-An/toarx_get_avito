from PyQt5 import QtCore, QtGui, QtWidgets, QtSql


class Ui_Form_2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(833, 519)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 631, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(650, 10, 171, 441))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.sql()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def sql(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("")
        self.db.setDatabaseName("")
        self.db.setUserName("")
        self.db.setPassword("")
        self.db.open()

        self.sql_table()

    #  self.db.close()

    def sql_table(self):
        self.mod = QtSql.QSqlRelationalTableModel(parent=None)
        self.mod.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.mod.setTable('Прогули')
        self.mod.setSort(1, QtCore.Qt.AscendingOrder)
        self.mod.setRelation(0, QtSql.QSqlRelation('Студенти', 'КодСтудента', 'ПІБ'))
        self.mod.setRelation(1, QtSql.QSqlRelation('Групи', 'КодГрупи', 'НомерГрупи'))
        self.mod.select()
        self.mod.setHeaderData(0, QtCore.Qt.Horizontal, "ПІБ")
        self.mod.setHeaderData(1, QtCore.Qt.Horizontal, "Номер групи")
        self.mod.setHeaderData(2, QtCore.Qt.Horizontal, "Прогули")

        self.mod.dataChanged.connect(self.mod.submitAll)

        self.findTextPushButton()

        self.tv = self.tableView
        self.tv.setModel(self.find)

        self.tv.setSortingEnabled(True)
        self.tv.setItemDelegateForColumn(0, QtSql.QSqlRelationalDelegate(self.tv))
        self.tv.setItemDelegateForColumn(1, QtSql.QSqlRelationalDelegate(self.tv))
        self.tv.setColumnWidth(0, 300)
        self.tv.setColumnWidth(1, 150)
        self.tv.setColumnWidth(2, 100)
        self.pushButton.clicked.connect(self.addStr)
        self.pushButton_2.clicked.connect(self.deletStr)

    def findTextPushButton(self):
        self.find = QtCore.QSortFilterProxyModel(parent=None)
        self.find.setSourceModel(self.mod)
        self.find.sort(1, order=QtCore.Qt.AscendingOrder)
        self.find.setFilterKeyColumn(-1)
        self.lineEdit.textChanged.connect(self.find.setFilterRegExp)

    def addStr(self):
        self.mod.insertRow(self.mod.rowCount())

    def deletStr(self):
        self.mod.removeRow(self.tv.currentIndex().row())
        self.mod.select()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Пошук"))
        self.pushButton.setText(_translate("Form", "Добавити запис"))
        self.pushButton_2.setText(_translate("Form", "Видалити запис"))