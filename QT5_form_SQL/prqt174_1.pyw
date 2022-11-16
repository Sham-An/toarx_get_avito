from PyQt5 import QtWidgets, QtSql
import sys
# Создаем объект приложения, иначе поддержка баз данных не будет работать
арр = QtWidgets.QApplication(sys.argv)
con = QtSql.QSqlDatabase.addDatabase('QSQLITE') 
#con.setDatabaseName('c:\\temp\\data.sqlite')
con.setDatabaseName('data.sqlite')
if con.open():
    # Работаем с базой данных
     if 'category' not in con.tables():
         query = QtSql.QSqlQuery()
         query.exec("create table category (id integer primary key autoincrement, catname text)")
         query.prepare("insert into category values(null, :name)")
         lst = ['Носители', 'Расходники']
         query.bindValue(':name', lst)
         query.execBatch()
         query.exec("alter table good add column category integer default 2")
         query.exec("update good set category=1 where id=1")
else:
    # Выводим текст описания ошибки
    print(con.lastError().text())
     
