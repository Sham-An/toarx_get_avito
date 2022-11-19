import json
import sqlite3
from datetime import datetime
import pandas as pd
import json


# import sqlite
def open_file_city():
    # Открываем файл
    with open("avito_city.json", encoding='utf-8') as file:  # Без указания кодировки выдает ошибку
        #        print(file)

        data = json.load(file)  # loadS из строки, load из файла
    #        print(data)
    # Поиск filter(lambda x: x['plate']=='E222EE177', str1['cars'])[0]['model']

    data_1 = data['data']
    # print(data_1)
    # for item in data['data']:
    #     print(f"Первый файл {item['id']} = {item['name']}")
    return data_1


def open_file_region():
    # Открываем файл
    with open("avito_region.json", encoding='utf-8') as file:  # Без указания кодировки выдает ошибку
        #        print(file)

        data = json.load(file)  # loadS из строки, load из файла
    #        print(data)
    # Поиск filter(lambda x: x['plate']=='E222EE177', str1['cars'])[0]['model']

    data_1 = data['data']
    print(data_1)
    # for item in data['data']:
    #     print(f"Первый файл {item['id']} = {item['name']}")
    return data_1


def open_json_data():
    conn = sqlite3.connect("region.db")

#data.to_sql('table_name', con=engine, schema = 'dbo', if_exists='replace')

    data = list(open_file_region())
    print(type(data))
    # Create A DataFrame From the JSON Data
    df = pd.DataFrame(data)#, index='id')
    # conn = sqlite3.connect("data.db")
    #conn = sqlite3.connect("region.db")
    c = conn.cursor()
    #df = pd.DataFrame(tuples_list, columns = ['Courses', 'Fee', 'Duration'])
    df.to_sql("region", conn, index=False, index_label='id')#, index_label='id')#,  index_col='id'
    createSecondaryIndex = "CREATE INDEX key_1 ON region(id)"
    conn.execute(createSecondaryIndex)
    #CREATE INDEX IF NOT EXISTS dbname.ixname ON tblname (columnname) WHERE…
    #CREATE INDEX ind_name ON table1 (column_name) WHERE column_name IS NOT NULL;
    #CREATE INDEX id_key ON table1 (column_name) WHERE column_name IS NOT NULL;
    #createSecondaryIndex = "CREATE INDEX index_part_name ON parts(name)"
    # sqliteCursor.execute(createSecondaryIndex)

    data2 = open_file_city()
    print(type(data2))
    df2 = pd.DataFrame(data2)#, index='parent_Id')#, index='id')
    #conn = sqlite3.connect("region.db")
    c = conn.cursor()
    df2.to_sql("city",
               conn,
               index=False,
               index_label='parent_Id'
               ) #index_label='id'index_label='parent_Id'
    createSecondaryIndex = "CREATE INDEX key_2 ON city(parent_Id)"
    conn.execute(createSecondaryIndex)

    #index=False, index_label=‘id’
    #Если имя первичного ключа в вашей базе данныхindexВам не нужно устанавливать эти два элемента, если нет, установите в соответствии с именем первичного ключа!
#DataFrame.to_sql(
#     name,
#     con,
#     schema=None,
#     if_exists='fail',
#     index=True,
#     index_label=None,
#     chunksize=None,
#     dtype=None,
#     method=None
# )



def import_one():
    pass
    #
    # db = sqlite3.connect('C:\myDB.sqlite')
    # with open('C:\myJSON.json', encoding='utf-8-sig') as json_file:
    #     json_data = json.loads(json_file.read())
    #
    #     # Aim of this block is to get the list of the columns in the JSON file.
    #     columns = []
    #     column = []
    #     for data in json_data:
    #         column = list(data.keys())
    #     for col in column:
    #         if col not in columns:
    #             columns.append(col)
    #
    #     # Here we get values of the columns in the JSON file in the right order.
    #     value = []
    #     values = []
    #     for data in json_data:
    #         for i in columns:
    #             value.append(str(dict(data).get(i)))
    #     values.append(list(value))
    #     value.clear()
    #
    #     # Time to generate the create and insert queries and apply it to the sqlite3 database
    #     create_query = "create table if not exists myTable ({0})".format(" text,".join(columns))
    #     insert_query = "insert into myTable ({0}) values(?{1})".format(", ".join(columns), ",?" * (len(columns) - 1))
    #     print("insert has started at " + str(datetime.now()))
    #     c = db.cursor()
    #     c.execute(create_query)
    #     c.executemany(insert_query, values)
    #     values.clear()
    #     db.commit()
    #     c.close()
    #     print("insert has completed at " + str(datetime.now()))
    #


# open_file()
# open_file_city()
#open_file_region()
open_json_data()


# 1. Quick Examples of pandas Set Index Name
# In case you hurry, below are some quick examples of how to set the index name to pandas DataFrame.
#
#
# # Below are quick example
# # Get name of the index column of DataFrame.
# index_name=df.index.name
#
# # set Index Name
# df.index.name='Index1'
#
# # Set column as Index.
# df = pd.DataFrame(technologies).set_index('Courses')
#
# # Rename Index.
# df = df.rename_axis('Courses1')
#
# # Get pandas index title/name by index and columns parameter.
# df = df.rename_axis(index='Courses', columns="Courses1")
#
# # Removing index and columns names to set it none.
# df = df.rename_axis(index=None, columns=None)
#
# # Using df.index.rename get pandas index title/name.
# df.index.rename('Courses1', inplace=True)
#
# # Add Multilevel index using set_index()
# df2 = df.set_index(['Courses', 'Duration'], append=True)
#
# # Rename Single index from multi Level
# df2.index = df2.index.set_names('Courses_Duration', level=2)
#
# # Rename All indexes
# df2.index=df2.index.rename(['Index','Courses_Name','Courses_Duration'])