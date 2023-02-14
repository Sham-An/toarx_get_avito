import json
import sqlite3

connection = sqlite3.connect('realty')
cursor = connection.cursor()
cursor.execute('Create Table if not exists Student (name Text, course Text, roll Integer)')

traffic = json.load(open('json_file.json'))
columns = ['name','course','roll']
for row in traffic:
    keys= tuple(row[c] for c in columns)
    cursor.execute('insert into Student values(?,?,?)',keys)
    print(f'{row["name"]} data inserted Succefully')

connection.commit()
connection.close()
 