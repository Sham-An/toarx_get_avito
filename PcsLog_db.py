import psycopg2
import sqlite3

import sqlite3
from contextlib import closing

database = 'PcsLog.db'

with closing(sqlite3.connect(database)) as connection:
    cursor = connection.cursor()
    cursor.execute("""
                   select LogContext from PCSLog
                   """)
    # получаем все значения
    print(f'{cursor.fetchall()}\n')
