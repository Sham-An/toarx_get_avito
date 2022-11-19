from PyQt5 import QtCore, QtWidgets, QtSql
# from PySide2 import QtCore, QtWidgets, QtSql
import sys
import json_to_sqlite_region


def addRecord():
    # Вставляем пустую запись, в которую пользователь сможет
    # ввести нужные данные
    stm.insertRow(stm.rowCount())


def delRecord():
    # Удаляем запись из модели

    currow = tv.currentIndex().row()
    # print(currow)
    # stm.removeRow(tv.currentIndex().row())
    # stm.setRowHidden()
    stm.removeRow(currow)
    # Регистрируем в базе изменения
    stm.submitAll()  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
    # Выполняем повторное считывание данных в модель,
    # чтобы убрать пустую "мусорную" запись
    stm.select()


# Пример удаления пяти записей:
# 1. model.removeRows(row, 5);2. model.submitAll();
# Первый аргумент QSqlTableModel::removeRows() является номером первой строки, второй количеством удаляемых записей.
# Обратите внимание: После окончания изменения записей необходимо вызвать QSqlTableModel::submitAll(), которая гарантирует, что изменения записались в БД. Необходимость и время, когда необходимо вызвать submitAll(), зависят от текущей стратегии редактирования табличной модели: ·

# 1. OnFieldChange, // изм. применяются (сразу) при вводе значения
# 2. OnRowChange,   // изм. применяются при обр. к другой строке (по умолч.)
# 3. OnManualSubmit // изм. применяются только после вызова submitAll()6. };


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QSqlRelationalTableModel")
# Устанавливаем соединение с базой данных
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
# con.setDatabaseName('c:\\temp\\data.sqlite')
con.setDatabaseName('region.db')
# con.setDatabaseName('data.sqlite')
con.open()
# Создаем модель
stm = QtSql.QSqlRelationalTableModel(parent=window)
# 1-я вставка
stm.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)  # OnRowChange
# stm.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
# stm.setEditStrategy(QtSql.QSqlTableModel.OnRowChange)

# model->setEditStrategy(QSqlRelationalTableModel::OnFieldChange);
# Конец 1-й вставки
stm.setTable('city')
stm.setSort(1, QtCore.Qt.AscendingOrder)
# Задаем для поля категории связь с таблицей списка категорий
# stm.setRelation(3, QtSql.QSqlRelation('category', 'id', 'catname'))
stm.setRelation(2, QtSql.QSqlRelation('region', 'id', 'name'))
# quer = ('SELECT * FROM category ORDER BY id LIMIT 3')
stm.select()  # quer)
stm.setHeaderData(0, QtCore.Qt.Horizontal, 'City_id')
stm.setHeaderData(1, QtCore.Qt.Horizontal, 'City_name')
#stm.setHeaderData(2, QtCore.Qt.Horizontal, 'City_id')
stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Region')

#stm.setHeaderData(3, QtCore.Qt.Horizontal, 'Категория')
# 2-я вставка
stm.dataChanged.connect(stm.submitAll)
# Конец 2-й вставки
vbox = QtWidgets.QVBoxLayout()
tv = QtWidgets.QTableView()
tv.setModel(stm)
# 3-я вставка
#tv.setItemDelegateForColumn(3, QtSql.QSqlRelationalDelegate(tv))
tv.setItemDelegateForColumn(2, QtSql.QSqlRelationalDelegate(tv))
# Конец 3-й вставки
#tv.hideColumn(0)
tv.setColumnWidth(0, 50)
tv.setColumnWidth(1, 150)
tv.setColumnWidth(2, 150)
#tv.setColumnWidth(3, 150)
vbox.addWidget(tv)
btnAdd = QtWidgets.QPushButton("&Добавить запись")
btnAdd.clicked.connect(addRecord)
vbox.addWidget(btnAdd)
btnDel = QtWidgets.QPushButton("&Удалить запись")
btnDel.clicked.connect(delRecord)
vbox.addWidget(btnDel)
window.setLayout(vbox)
window.resize(400, 350)
window.show()
sys.exit(app.exec_())
