#from PyQt5 import QtCore, QtWidgets, QtSql
from PySide2 import QtCore, QtWidgets, QtSql
import sys
def addRecord():
    # Вставляем пустую запись, в которую пользователь сможет
    # ввести нужные данные
    stm.insertRow(stm.rowCount())
def delRecord():
    # Удаляем запись из модели
    stm.removeRow(tv.currentIndex().row())
    # Выполняем повторное считывание данных в модель,
    # чтобы убрать пустую "мусорную" запись
    stm.select()
    
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QSqlRelationalTableModel")
# Устанавливаем соединение с базой данных
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
#con.setDatabaseName('c:\\temp\\data.sqlite')
con.setDatabaseName('data.sqlite')
con.open()
# Создаем модель
stm = QtSql.QSqlRelationalTableModel(parent = window)
# 1-я вставка
stm.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
# Конец 1-й вставки
stm.setTable('good')
stm.setSort(1, QtCore.Qt.AscendingOrder)
# Задаем для поля категории связь с таблицей списка категорий
stm.setRelation(3, QtSql.QSqlRelation('category', 'id', 'catname'))
stm.select()
stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Название')
stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Кол-во')
stm.setHeaderData(3, QtCore.Qt.Horizontal, 'Категория')
# 2-я вставка
stm.dataChanged.connect(stm.submitAll)
# Конец 2-й вставки
vbox = QtWidgets.QVBoxLayout()
tv = QtWidgets.QTableView()
tv.setModel(stm)
# 3-я вставка
tv.setItemDelegateForColumn(3, QtSql.QSqlRelationalDelegate(tv))
# Конец 3-й вставки
tv.hideColumn(0)
tv.setColumnWidth(1, 150)
tv.setColumnWidth(2, 60)
tv.setColumnWidth(3, 150)
vbox.addWidget(tv)
btnAdd = QtWidgets.QPushButton("&Добавить запись")
btnAdd.clicked.connect(addRecord)
vbox.addWidget(btnAdd)
btnDel = QtWidgets.QPushButton("&Удалить запись")
btnDel.clicked.connect(delRecord)
vbox.addWidget(btnDel)
window.setLayout(vbox)
window.resize(400, 250)
window.show()
sys.exit(app.exec_())
