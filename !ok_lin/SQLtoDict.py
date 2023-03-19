import sqlite3

#Общая структура запроса выглядит следующим образом:
#
#SELECT ('столбцы или * для выбора всех столбцов; обязательно')
#FROM ('таблица; обязательно')
#WHERE ('условие/фильтрация, например, city = 'Moscow'; необязательно')
#GROUP BY ('столбец, по которому хотим сгруппировать данные; необязательно')
#HAVING ('условие/фильтрация на уровне сгруппированных данных; необязательно')
#ORDER BY ('столбец, по которому хотим отсортировать вывод; необязательно')
#
##############################################
#import sqlite3

print('\n', 'PRIMER 1 ')
conn = sqlite3.connect(":memory:")
conn.execute('create table t (a text, b text, c text)')
conn.execute('insert into t values ("aaa", "bbb", "ccc")')
conn.execute('insert into t values ("AAA", "BBB", "CCC")')
conn.row_factory = sqlite3.Row
c = conn.cursor()
c.execute('select * from t')
for r in c.fetchall():
    print(dict(r))


print('\n', 'PRIMER 2 ')
#db = sqlite3.connect("test.sqlite3")

#db = sqlite3.connect('Pcsparse.db')
db = sqlite3.connect('Pcsparent.db')
cur = db.cursor()
res = cur.execute("select * from PCSparent ").fetchall()
data = dict(zip([c[0] for c in cur.description], res[0]))
print(data) #печать наименований
#print(*data, sep='\n')

################################################################
#db2 = sqlite3.connect('Pcsparse.db')
parname = "Азитромицин"
cursor = db.execute('SELECT * FROM PCSparent')# WHERE PAR_NAME_short = "Азитромицин"') # ORDER BY CREATE_AT')
studentList = cursor.fetchall()

columnNames = list(map(lambda x: x[0], cursor.description)) #students table column names list
studentsAssoc = {} #Assoc format is dictionary similarly

#THIS IS ASSOC PROCESS

for lineNumber, student in enumerate(studentList):
        studentsAssoc[lineNumber] = {}

        for columnNumber, value in enumerate(student):
            studentsAssoc[lineNumber][columnNames[columnNumber]] = value


print(studentsAssoc)
#print(*studentsAssoc, sep='\n')

print("Мой вариант")

parname = "Азитромицин"
cursor = db.execute('SELECT * FROM PCSparent WHERE PAR_NAME_short = "Азитромицин"') # ORDER BY CREATE_AT')
studentList = cursor.fetchall()

columnNames = list(map(lambda x: x[0], cursor.description)) #students table column names list
studentsAssoc = {} #Assoc format is dictionary similarly

#THIS IS ASSOC PROCESS

for lineNumber, student in enumerate(studentList):
        studentsAssoc[lineNumber] = {}

        for columnNumber, value in enumerate(student):
            studentsAssoc[lineNumber][columnNames[columnNumber]] = value


print(studentsAssoc)


#  ПРимер 3
# print('PRIMER 3')
# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#         print(d)
#     return d
#
# #conn = sqlite3.connect(":memory:")
# #conn.row_factory = dict_factory
# db.row_factory = dict_factory
# #print(f"{company['id']} - {company['name']} - {company['employees']} - {company['established']}")
# #conn.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(c.description)])
# db.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(c.description)])
# c = conn.cursor()
# c.execute("select 1 as a")
# print(db.row_factory)


# def select_column_and_value1(db, sql, parameters=()):
#     execute = db.execute(sql, parameters)
#     fetch = execute.fetchone()
#     return {k[0]: v for k, v in list(zip(execute.description, fetch))}
#
# con = sqlite3.connect('Pcsparse.db')
# c = con.cursor()
# print(select_column_and_value1(c, 'SELECT * FROM PCSparse WHERE id=?', (id,)))
#Но если ваш запрос ничего не возвращает, это приведет к ошибке. В этом случае…​

# def select_column_and_value2(self, sql, parameters=()):
#     execute = self.execute(sql, parameters)
#     fetch = execute.fetchone()
#
#     if fetch is None:
#         return {k[0]: None for k in execute.description}
#
#     return {k[0]: v for k, v in list(zip(execute.description, fetch))}
# #or
# print(select_column_and_value2(c, 'SELECT * FROM PCSparse WHERE id=?', (id,)))
#
# def select_column_and_value3(self, sql, parameters=()):
#     execute = self.execute(sql, parameters)
#     fetch = execute.fetchone()
#
#     if fetch is None:
#         return {}
#
#     return {k[0]: v for k, v in list(zip(execute.description, fetch))}
#
# print(select_column_and_value3(c, 'SELECT * FROM PCSparse WHERE id=?', (id,)))
#


#cnx = mysql.connector.connect(database='world')
#cursor = cnx.cursor(dictionary=True)
#cursor.execute("SELECT * FROM country WHERE Continent = 'Europe'")
#
#print("Countries in Europe:")
#for row in cursor:
#    print("* {Name}".format(Name=row['Name']
#
########################
#cursor.execute("SELECT Name, Population FROM country WHERE Continent = 'Europe'")
#
#print("Countries in Europe with population:")
#for row in cursor:
#        print("* {Name}: {Population}".format(**row))

#######################################################
#query_result = [ dict(line) for line in [zip([ column[0] for column in crs.description], row) for row in crs.fetchall()] ]
#print (query_result)