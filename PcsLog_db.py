import psycopg2
import sqlite3
import os
#from os import path
from pathlib import Path
import pathlib
from pathlib import Path
import sqlite3
from contextlib import closing

datamain = 'PcsLog.db'
conn_PCS_main = sqlite3.connect(datamain)

database = 'Pcsparse.db'
conn_PCS_db = sqlite3.connect(database)

def open_cur():
    #with closing(sqlite3.connect(database)) as connection:
    with closing(conn_PCS_db) as connection:
        cursor = connection.cursor()

    return cursor

def check_database(offer):
    print('check_database\n')
    print(offer)
    # offer = {'offer_id': 2465411376, 'id_item': 2465411375, 'category_name': 'category_name',
    #          'category_kod': 'category_kod',
    #          'date': '2022-09-06 15:37:49', 'time': '1662467869', 'title_desk': 'Error title',
    #          'title_full': 'Error title',
    #          'img': 'img', 'price': 3000000, 'address': 'Москва', 'coords': 'coords',
    #          'url': 'url',
    #          'uri': 'uri',
    #          'uri_mweb': 'uri_mweb',
    #          'area': 100,
    #          'rooms': 'E',
    #          'floor': 5,
    #          'total_floor': 'r',
    #          }

    # offer2 = {'offer_id': 2465411376, 'id_item': 1, 'category_name': '2', 'category_kod': '3',
    #           'date': '4', 'time': "5", 'title_desk': '6', 'title_full': '7',
    #           'img': '8', 'price': '9', 'address': '10', 'coords': '11',
    #           'url': '12',
    #           'uri': '13',
    #           'uri_mweb': '14',
    #           'area': '15',
    #           'rooms': '16',
    #           'floor': '17',
    #           'total_floor': '18',
    #           }

    offer_id = offer["offer_id"]
    print(type(offer))
    with sqlite3.connect('Pcsparse.db') as connection:
        cursor = connection.cursor()

        # cursor.execute("""
        #     SELECT offer_id FROM offers WHERE offer_id = (?)
        # """, (offer_id,))
        # result = cursor.fetchone()
        # print(f'result cursor.fetchone() = {result}')
        #
        # if result is None:

        cursor.execute("""
                INSERT INTO offers 
                VALUES (NULL, :id_item, :category_name, :category_kod, 
                :date, :time, :title_desk, :title_full, :img, :price,
                :address, :coords, :url, :uri, :uri_mweb, :offer_id, :area,
                :rooms, :floor, :total_floor)
                """, offer)
        connection.commit()
        print(f'добавлено в базу данных')


def prnpcs():
    #offer = {}
    #
    #offer["offer_id"] = id_item
    #offer["id_item"] = id_item

    # cursor.execute("""
    #     INSERT INTO offers
    #     VALUES (NULL,: id_item,: category_name,: category_kod,
    #     : date,: time,: title_desk,: title_full,: img,: price,
    #     : address,: coords,: url,: uri_mweb,: offer_id,: area,
    #     : rooms,: floor,: total_floor)
    # """, offer)

    #with closing(conn_PCS_db) as connpcs:
    #conn = sqlite3.connect
    connpcs = sqlite3.connect('Pcsparse.db')
    cur = connpcs.cursor()

    #select LogContext from PCSLog
    database = 'PcsLog.db'
    key1 = 'Печать работы:'#Печать работы: C:\Users\Solmark\Desktop\СЕРИИ\Омепразол 30\бланк1.VDF
    key2 = 'Старт Печати Индекс текущей записи'#Старт Печати Индекс текущей записи 2636.
    key3 = 'Стоп печати Индекс текущей записи' #Стоп печати Индекс текущей записи 2666.
    insert_db = 0
    PCS = "" #{}
    #with closing(sqlite3.connect(database)) as connection:
    with closing(conn_PCS_main) as connection:
        #conn = sqlite3.connect

        cursor = connection.cursor()
        #cursor = open_cur()
        cursor.execute("""
                       select * from PCSLog
                       """)
        # получаем все значения
        rows = cursor.fetchall()
        for row in rows:
            #PCS = {}

            #ID_PCS = row[0]
            Log_Time = row[3]
            cont = str(row[4])
            if key1 in cont:
                PCS = {}
                ID_PCS = row[0]
                #print('key1', cont)
                PCS["PCS_id"] = ID_PCS
                PCS["Log_Time"] = Log_Time
                PCS["cont"] = cont

                #'C:\\Users\\Solmark\\Desktop\\СЕРИИ\\Омепразол 30\\бланк1.VDF')
                #full_path = path
                cont_txt = cont
                full_path = str(Path(cont.replace(key1, "").strip()))
                print('cont1 ', cont_txt)
                cont_txt.replace("\\", "/")
                print('cont2 ', cont_txt)
                path: Path = Path(full_path)

                fulll_path =full_path

                print(path)
                name = os.path.basename(full_path)
                name.replace("\\", "/")

                print('name win32', name)
                path: Path = Path(name)
                #name = path.splitext(name)[0]
                name = pathlib.Path(name).stem
                print('name', name)

                PCS["Full_path1"] = name# path #os.path.basename(full_path)

                #name = os.path.splitext(os.path.basename(full_path))[1]#.replace('\', "")))[0]


                filesurvey = []
                for row in os.walk(fulll_path):  # row beinhaltet jeweils einen Ordnerinhalt
                    print(f'row = {row}')
                    for filename in row[2]:  # row[2] ist ein tupel aus Dateinamen
                        print(filename)
                        full_path1: Path = Path(row[0]) / Path(filename)  # row[0] ist der Ordnerpfad
                        filesurvey.append([full_path1, filename, full_path1.stat().st_mtime, full_path1.stat().st_size])
                PCS["file_name"] = name

                PCS["start"] = ""
                PCS["stop"] = ""
                print(' \n Печать работы:   ')
                insert_db = 'Insert  '
                #print('PCS ++++++++++++====', PCS)

                ## "INSERT INTO PCSparse (PCS_time,PCS_context) VALUES (Log_Time, cont)"
                # cur.execute(
                #     """INSERT INTO PCSparse (PCS_time,PCS_context) VALUES (Log_Time, cont);"""
                # )
                #
                # connpcs.commit()
                #print("Record inserted successfully")

            elif key2 in cont:
                #print('key2', cont, PCS)

                PCS["start"] = cont
                #print('PCS 2222 ++++++++++++====', PCS)

                #cur.execute("UPDATE STUDENT set AGE = 20 where ADMISSION = 3420")
                #con.commit()
                insert_db = "Update 1"

            elif key3 in cont:
                #print('key3', cont, '\n')
                #cur.execute("UPDATE STUDENT set AGE = 20 where ADMISSION = 3420")
                #con.commit()
                #print('key3', cont, PCS)

                PCS["stop"] = cont
                #print('PCS 3333 ++++++++++++====', PCS)
                insert_db = "Update 2"

            #else:
                #state3
            #else: #delete
            if insert_db:
                print(f'PCS {insert_db} == {PCS}')
                insert_db = 0
                #PCS = {}

            #cur.execute("DELETE from STUDENT where ADMISSION=3420;")
            #con.commit()
            #print("ID =", row[0], ' \n')
            #print("Log_Time =", row[3])
            #print("Log_Context =", cont)
   #print("Operation done successfully")

def CreateLogDB():

    # При подключении к базе, автоматически создается realty.db
    connection = sqlite3.connect('Pcsparse.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE PCSparse (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            PCS_start integer,
            PCS_time_start text,
            PCS_time_print text,
            PCS_context text,
            Parent_name text,
            gtin_kod text,
            gtin_name text,
            last_kod_id text,
            last_kod text,
            status text            
            )     
    """)
    connection.close()


if __name__ == '__main__':
    #CreateLogDB()
    prnpcs()
