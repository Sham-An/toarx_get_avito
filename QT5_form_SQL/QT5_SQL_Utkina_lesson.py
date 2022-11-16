# from PyQt5.QtSql import QSqlDatabase

#from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PySide2.QtSql import QSqlDatabase, QSqlQuery

#from PyQt5.QtCore import Qt
from PySide2.QtCore import Qt

#from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PySide2.QtSql import QSqlDatabase, QSqlTableModel

#from PyQt5.QtWidgets import (
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableView,
    QTableWidget,
    QTableWidgetItem,
    QLabel,
)
import sys

class Contacts_edit(QMainWindow):
    # Использование классов представления и модели
    #

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTableView Example")
        self.resize(415, 200)
        # Set up the model
        """
        некоторые из классов моделей, которые PyQt предоставляет для работы с базами данных SQL:

        Модель Класс	                Описание
        QSqlQueryModel	            Модель данных только для чтения для запросов SQL
        QSqlTableModel	            Редактируемая модель данных для чтения и записи записей в одной таблице
        QSqlRelationalTableModel	Редактируемая модель данных для чтения и записи записей в реляционной таблице
        """
        self.model = QSqlTableModel(self)   #создает редактируемый QSqlTableModel объект.
        self.model.setTable("contacts") #связывает вашу модель с contacts таблицей в вашей базе данных с помощью .setTable().
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange) #устанавливает стратегию редактирования модели OnFieldChange, позволяет модели автоматически обновлять данные
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Job")
        self.model.setHeaderData(3, Qt.Horizontal, "Email")
        self.model.select() #загружает данные из вашей базы данных и заполняет модель путем вызова .select().
        # Set up the view
        self.view = QTableView() #создает объект табличного представления для отображения данных, содержащихся в модели.
        self.view.setModel(self.model) #связывает представление с моделью, вызывая .setModel() представление с вашей моделью данных в качестве аргумента.
        self.view.resizeColumnsToContents() #вызывает .resizeColumnsToContents() объект просмотра, чтобы настроить таблицу в соответствии с ее содержимым.
        self.setCentralWidget(self.view)



class Contacts_view(QMainWindow):
    #Использование стандартных классов виджетов
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTableView Example")
        self.resize(450, 250)
        # Set up the view and load the data
        self.view = QTableWidget()
        self.view.setColumnCount(4)
        self.view.setHorizontalHeaderLabels(["ID", "Name", "Job", "Email"])
        query = QSqlQuery("SELECT id, name, job, email FROM contacts")
        while query.next():
            rows = self.view.rowCount()
            self.view.setRowCount(rows + 1) #увеличивает количество строк в таблице с 1 помощью .setRowCount().
            self.view.setItem(rows, 0, QTableWidgetItem(str(query.value(0)))) #id столбцах целыми числами,
                                                                                # необходимо преобразовать их в строки, чтобы иметь возможность хранить их в QTableWidgetItem объекте.
            self.view.setItem(rows, 1, QTableWidgetItem(query.value(1)))
            self.view.setItem(rows, 2, QTableWidgetItem(query.value(2)))
            self.view.setItem(rows, 3, QTableWidgetItem(query.value(3)))
        self.view.resizeColumnsToContents()
        self.setCentralWidget(self.view)


# def createConnection():
#     con = QSqlDatabase.addDatabase("QSQLITE")
#     con.setDatabaseName("contacts.sqlite")
#     if not con.open():
#         QMessageBox.critical(
#             None,
#             "QTableView Example - Error!",
#             "Database Error: %s" % con.lastError().databaseText(),
#         )
#         return False
#     return True


def select_sql():
    # Навигация по записям в запросе
    """
    QSqlQuery предоставляет набор методов навигации , которые можно использовать для перемещения по записям в результате запроса:

    Методика	Извлечение
    .next()	Следующая запись
    .previous()	Предыдущая запись
    .first()	Первая запись
    .last()	Последняя запись
    .seek(index, relative=False)	Рекорд на позиции index

    все они возвращают либо True или False,
    вы можете использовать их в цикле while для навигации по всем записям за один раз.
    Как только активный запрос находится в допустимой записи,
    вы можете получить данные из этой записи с помощью .value(index).
    """
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("contacts.sqlite")
    con.open()
    # Create and execute a query
    query = QSqlQuery()
    query.exec("SELECT name, job, email FROM contacts")

    # Этот запрос возвращает данные о name, job и email все контакты ,
    # хранящиеся в contacts таблице. После .exec() возврата True
    # запрос был успешным и теперь является активным запросом.
    # Вы можете перемещаться по записям в этом запросе, используя любой из методов навигации,
    # которые вы видели ранее. Вы также можете получить данные в любом столбце записи, используя .value():
    # First record
    query.first()
    # Named indices for readability
    name, job, email = range(3)
    print(f"{name}, {job}, {email} ")  # 0, 1, 2
    # Retrieve data from the first record
    print(query.value(name))  # Linda

    # Next record
    query.next()
    print(query.value(job))  # Senior Web Developer

    # Last record
    query.last()
    print(query.value(email))  # jane@example.com
    print('\n\n\n')
    # С помощью методов навигации вы можете перемещаться по результату запроса.
    # С помощью .value() вы можете получить данные в любом столбце данной записи.

    # Вы также можете перебирать все записи в своем запросе, используя while цикл вместе с .next():

    query.exec()
    while query.next():
        print(query.value(name), query.value(job), query.value(email))
    print('\n\n\n')
    # выполнить цикл в обратном порядке, используя .previous():
    # .previous() работает аналогично .next(), но итерация выполняется в обратном порядке.
    while query.previous():
        print(query.value(name), query.value(job), query.value(email))

    # получить индекс, который идентифицирует данный столбец в таблице,
    # используя имя этого столбца. Для этого вы можете вызвать
    # .indexOf() возвращаемое значение .record():
    # Обращение к .indexOf() результату .record() возвращает индекс "name" столбца.
    # Если "name" не существует, то .indexOf() возвращается -1.
    # Это удобно, когда вы используете SELECT* оператор, в котором порядок столбцов неизвестен.
    query.first()
    # Get the index of name
    name = query.record().indexOf("name")
    print(query.value(name))
    query.finish()  # Наконец, если вы закончили с объектом запроса, вы можете отключить его, вызвав .finish().
    # Это освободит системную память, связанную с рассматриваемым объектом запроса.

    # print(query.isActive())


def query_dynamic():
    # 1 Выполнение динамических запросов:
    # 1.1 Форматирование строк
    # позволяет быстро создавать динамические запросы. Однако, чтобы безопасно использовать этот подход, вы должны быть уверены, что ваши значения параметров
    # поступают из надежного источника. В противном случае вы можете столкнуться с атаками SQL - инъекций.
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("contacts.sqlite")
    con.open()

    name = "Linda"
    job = "Technical Lead"
    email = "linda@example.com"

    query = QSqlQuery()
    query.exec(
        f"""INSERT INTO contacts (name, job, email)
        VALUES ('{name}', '{job}', '{email}')"""
    )
    # для работы такого динамического запроса необходимо чтобы
    # вставляемые значения имеют правильный тип данных.
    # Таким образом, вы используете одинарные кавычки вокруг заполнителя в f-строке,
    # потому что эти значения должны быть строками.

    # 1.2 Выполнение динамических запросов: Параметры-заполнители
    """ Выполнение динамических запросов: Параметры-заполнители
    Второй подход к выполнению динамических запросов требует предварительной подготовки запросов с использованием шаблона с заполнителями для параметров. PyQt поддерживает два стиля заполнителей параметров:

    1.Стиль Oracle использует именованные заполнители, такие как :name или :email.
    2.Стиль ODBCиспользует знак вопроса (?) в качестве позиционного заполнителя. 
        ODBC означает Открытое подключение к базе данных."""


# Если шаблон имеет какие-либо проблемы, такие как синтаксическая ошибка SQL, то .prepare() не удается скомпилировать шаблон и возвращает False.


def query_static():
    # Выполнение статических SQL-запросов
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

    # Вернитесь к скрипту, созданному в разделе Выполнение статических SQL-запросов, и добавьте следующий код сразу после вызова
    # Creating a query for later execution using .prepare()
    insertDataQuery = QSqlQuery()  # Первым шагом является создание объекта QSqlQuery.
    # Затем вы вызываете функцию .prepare() для объекта запроса.
    # Затем вы создаете некоторые образцы данных для заполнения базы данных.
    # Данные содержат список кортежей, и каждый кортеж содержит три элемента: name, job и email каждого контакта.
    insertDataQuery.prepare(
        """
        INSERT INTO contacts (
            name,
            job,
            email
        )
        VALUES (?, ?, ?)
        """
    )
    # Sample data
    data = [("Joe", "Senior Web Developer", "joe@example.com"),
            ("Lara", "Project Manager", "lara@example.com"),
            ("David", "Data Analyst", "david@example.com"),
            ("Jane", "Senior Python Developer", "jane@example"),
            ]
    # Use .addBindValue() to insert data
    # Обратите внимание, что вы используете позиционные заполнители,
    # поэтому порядок, в котором вы вызываете .addBindValue (),
    # будет определять порядок, в котором каждое значение передается соответствующему заполнителю.
    # Всякий раз, когда вы принимаете ввод пользователя для выполнения запроса к базе данных,
    # вы сталкиваетесь с угрозой безопасности SQL-инъекции.
    # В PyQt объединение .prepare (), .bindValue () и .addBindValue() защищает вас от атак SQL-инъекций,
    for name, job, email in data:
        insertDataQuery.addBindValue(name)
        insertDataQuery.addBindValue(job)
        insertDataQuery.addBindValue(email)
        insertDataQuery.exec()


def message():
    # Create the connection
    con = QSqlDatabase.addDatabase("QSQLITE")
    # con.setDatabaseName("/home/contacts.sqlite")
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
    con1 = QSqlDatabase.addDatabase("QSQLITE", "con1")  # name_db contacts.sqlite
    con1.setDatabaseName("contacts.sqlite")  # name_connect "con1" or "qt_sql_default_connection"
    # Second connection
    con2 = QSqlDatabase.addDatabase("QSQLITE", "con2")
    con2.setDatabaseName("contacts.sqlite")

    name_db = con1.databaseName()
    name_connect = con1.connectionName()
    print(name_db, " ", name_connect)

    db = QSqlDatabase.database("con1", open=False)  # Если open True (по умолчанию)
    # и соединение не открыто, открывается автоматически.

    name_db = db.databaseName()
    name_connect = db.connectionName()
    open_connect = db.open()  # db.isOpen()
    # .open() в соединении, использующем драйвер SQLite, а файл базы данных не существует, то новый и пустой файл базы данных будет создан автоматически.
    print(name_db, " ", name_connect, open_connect)

    # 2. Открытие соединения с базой данных

    # Как только у вас есть подключение к базе данных, вам нужно открыть это соединение, чтобы иметь возможность взаимодействовать с вашей базой данных. Для этого вы вызываете функцию .open() для объекта .open() имеет следующие два варианта:
    #
    # 1. .open() открывает соединение с базой данных с использованием текущих значений соединения.
    # 2. .open(username, password) открывает соединение с базой данных с использованием предоставленных имени пользователя и пароля.

    # Обертывание вызова функции .open() в условный оператор позволяет обрабатывать любую ошибку, возникающую при открытии соединения.
    if not db.open():
        print("Unable to connect to the database")
        sys.exit(1)


# в графических приложениях вместо print () обычно используется объект QMessageBox.
# С помощью QMessageBox вы можно небольшие диалоги для представления информации

def createConnection():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("contacts.sqlite")
    if not con.open():
        QMessageBox.critical(
            None,
            "QTableView Example - Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        return False
    return True


def createConnection_view():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("contacts.sqlite")
    if not con.open():
        QMessageBox.critical(
            None,
            "QTableView Example - Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        return False
    return True


def start_app_edit():
    app = QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    win = Contacts_edit()
    #win = Contacts_view()
    win.show()
    sys.exit(app.exec_())

def start_app_view():
    app = QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    win = Contacts_view()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    # main()
    # message()
    # query_static()
    # query_dynamic()
    #select_sql()
    #start_app_view()
    start_app_edit()

# con = QSqlDatabase.addDatabase("QSQLITE")
# con.setDatabaseName("contacts.sqlite")

################# CLOSE()
# Чтобы закрыть соединение в PyQt, вы вызываете .close() соединение. Этот метод закрывает соединение и освобождает все полученные ресурсы. Это также делает недействительными любые связанные QSqlQuery объекты, потому что они не могут работать должным образом без активного соединения.
"""
Вот пример того, как закрыть активное соединение с базой данных, используя .close():

>>> from PyQt5.QtSql import QSqlDatabase
>>> con = QSqlDatabase.addDatabase("QSQLITE")
>>> con.setDatabaseName("contacts.sqlite")
>>> con.open()
True
>>> con.isOpen()
True
>>> con.close()
>>> con.isOpen()
False
Вы можете вызвать .close() соединение, чтобы закрыть его и освободить все связанные с ним ресурсы. Чтобы убедиться, что соединение закрыто, вы звоните .isOpen().

Обратите внимание, что QSqlQuery объекты остаются в памяти после закрытия связанного с ними соединения, поэтому вы должны сделать свои запросы неактивными, вызвав .finish() или .clear(), или удалив QSqlQueryобъект перед закрытием соединения. В противном случае в вашем объекте запроса не будет остаточной памяти.

Вы можете повторно открыть и повторно использовать любое ранее закрытое соединение. Это потому, .close() что не удаляет соединения из списка доступных соединений, поэтому они остаются пригодными для использования.

Вы также можете полностью удалить соединения с базой данных, используя .removeDatabase(). Чтобы сделать это безопасно, сначала завершите свои запросы с помощью .finish(), затем закройте базу данных с помощью .close() и, наконец, удалите соединение. Вы можете использовать .removeDatabase(connectionName) для удаления вызываемого соединения connectionNameс базой данных из списка доступных соединений. Удаленные соединения больше не доступны для использования в текущем приложении.

Чтобы удалить соединение с базой данных по умолчанию, вы можете вызвать .connectionName() возвращаемый объект .database()и передать результат в .removeDatabase():

>>> # The connection is closed but still in the list of connections
>>> QSqlDatabase.connectionNames()
['qt_sql_default_connection']
>>> # Remove the default connection
>>> QSqlDatabase.removeDatabase(QSqlDatabase.database().connectionName())
>>> # The connection is no longer in the list of connections
>>> QSqlDatabase.connectionNames()
[]
>>> # Try to open a removed connection
>>> con.open()
False
Здесь вызов .connectionNames() возвращает список доступных подключений. 
В этом случае у вас есть только одно соединение по умолчанию. 
Затем вы удаляете соединение с помощью .removeDatabase().

Примечание. 
Перед закрытием и удалением подключения к базе данных необходимо убедиться, 
что все, что использует подключение, удалено или настроено на использование другого источника данных. 
В противном случае возможна утечка ресурсов .
"""
