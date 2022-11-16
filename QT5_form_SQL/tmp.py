#from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QApplication, QMessageBox, QLabel
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import sys

def query():
    # Create the connection
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("contacts.sqlite")
    # Open the connection
    if not con.open():
        print("Database Error: %s" % con.lastError().databaseText())
        sys.exit(1)
    # Create a query and execute it right away using .exec()
    createTableQuery = QSqlQuery()
    createTableQuery.exec(
        """
        CREATE TABLE contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL
        )
        """
    )
    print(con.tables())

def message():
    # Create the connection
    con = QSqlDatabase.addDatabase("QSQLITE")
    #con.setDatabaseName("/home/contacts.sqlite")
    con.setDatabaseName("contacts.sqlite")
    # Create the application
    app = QApplication(sys.argv)
    # Try to open the connection and handle possible errors
    if not con.open():
        QMessageBox.critical(
            None,
            "App Name - Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        sys.exit(1)
    # Create the application's window
    win = QLabel("Connection Successfully Opened!")
    win.setWindowTitle("App Name")
    win.resize(200, 100)
    win.show()
    sys.exit(app.exec_())

def main():

# 1. Создание соединения с базой данных
  # 1.1 Обработка нескольких соединений
    # First connection
    con1 = QSqlDatabase.addDatabase("QSQLITE", "con1") #name_db contacts.sqlite
    con1.setDatabaseName("contacts.sqlite") #name_connect "con1" or "qt_sql_default_connection"
    # Second connection
    con2 = QSqlDatabase.addDatabase("QSQLITE", "con2")
    con2.setDatabaseName("contacts.sqlite")

    name_db = con1.databaseName()
    name_connect = con1.connectionName()
    print(name_db, " ", name_connect)

    db = QSqlDatabase.database("con1", open=False) #Если open True (по умолчанию)
    # и соединение не открыто, открывается автоматически.

    name_db = db.databaseName()
    name_connect = db.connectionName()
    open_connect = db.open() # db.isOpen()
    # .open() в соединении, использующем драйвер SQLite, а файл базы данных не существует, то новый и пустой файл базы данных будет создан автоматически.
    print(name_db, " ", name_connect, open_connect)

# 2. Открытие соединения с базой данных

# Как только у вас есть подключение к базе данных, вам нужно открыть это соединение, чтобы иметь возможность взаимодействовать с вашей базой данных. Для этого вы вызываете функцию .open() для объекта .open() имеет следующие два варианта:
#
# 1. .open() открывает соединение с базой данных с использованием текущих значений соединения.
# 2. .open(username, password) открывает соединение с базой данных с использованием предоставленных имени пользователя и пароля.

#Обертывание вызова функции .open() в условный оператор позволяет обрабатывать любую ошибку, возникающую при открытии соединения.
    if not db.open():
        print("Unable to connect to the database")
        sys.exit(1)
#в графических приложениях вместо print () обычно используется объект QMessageBox.
# С помощью QMessageBox вы можно небольшие диалоги для представления информации



if __name__ == "__main__":
    #main()
    #message()
    query()
#con = QSqlDatabase.addDatabase("QSQLITE")
#con.setDatabaseName("contacts.sqlite")