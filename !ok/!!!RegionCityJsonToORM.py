import json
from pathlib import Path
from logging import getLogger
import json
import sqlite3

#from aparser.models import Category
#from aparser.models import Category
#from aparser.models import Region
#from aparser.models import City
# from logging import getLogger
# from django.core.management.base import BaseCommand
# from django.core.management.base import CommandError

logger = getLogger(__name__)
def search_city(name):
    reg1 = name+'%'

    print(f'ПОИСК {reg1}')

    with sqlite3.connect('realty.db') as connection:
        cursor = connection.cursor()
        #SELECT * FROM cityes WHERE name LIKE 'Тар%'
        #SELECT name FROM cityes WHERE id = (?)
        #SELECT name FROM regions WHERE name LIKE 'Тарас%' ORDER BY name;

        cursor.execute("""
        SELECT name FROM regions WHERE name LIKE ? ORDER BY name
          """, (reg1,))
        result = cursor.fetchone()
        print(f'result cursor.fetchone() = {result}')

def create_city_tab():
    '''Создаем базу населенных пунктов'''
    connection = sqlite3.connect('realty.db')
    cursor = connection.cursor()
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    #id_key Text,
    cursor.execute("""
        Create Table if not exists cityes(
            id INTEGER PRIMARY KEY ,
            name Text,
            parent_id INTEGER,
            url_name text,
            index_post text
            )     
    """)#,(reg_id,))
    connection.commit()
    connection.close()

def create_regions_tab():
    '''Создаем базу регионов'''
    connection = sqlite3.connect('realty.db')
    cursor = connection.cursor()
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    #id_key Text,
    #sqlite_select_query = """SELECT * from sqlitedb_developers"""
    #https://pythonru.com/biblioteki/poluchenie-dannyh-iz-tablicy-sqlite
    cursor.execute("""
        Create Table if not exists regions(
            id INTEGER PRIMARY KEY ,
            name Text,
            url_name text,
            index_post text
            )     
    """)
    connection.commit()
    connection.close()

def list_dict(dicts):

    print("__РЕКУРСИЯ___111_LIST_DICT_111_____")
    for k, v, in dicts.items():
    #for k, v in data:
        try:
            print("key:\t" + k)
            list_dict(v)
        except AttributeError:
            print("value:\t" + str(v))
            print(type(v))


def check_city(reg):
    reg1 = reg

    print(reg1)
    reg_id = reg1["id"]
    id_int = int(reg1["id"])

    print(reg_id)
    with sqlite3.connect('realty.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
              SELECT id FROM cityes WHERE id = (?)
          """, (reg_id,))
        result = cursor.fetchone()
        print(f'result cursor.fetchone() = {result}')

        if result is None:
            with sqlite3.connect('realty.db') as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO regions VALUES (
                     :id, :name, :parent_id, :url_name, :index_post 
                    )
                    """, reg1)
                connection.commit()
        print(f'Объявление {reg_id} добавлено в базу данных')
    ##connection.close()


def check_region(reg):

    reg1 = reg

    print(reg1)
    reg_id = reg1["id"]
    id_int = int(reg1["id"])
    
    print(reg_id)
    with sqlite3.connect('realty.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
              SELECT id FROM regions WHERE id = (?)
          """, (reg_id,))
        result = cursor.fetchone()
        print(f'result cursor.fetchone() = {result}')

        if result is None:
            with sqlite3.connect('realty.db') as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO regions VALUES (
                     :id, :name, :url_name, :index_post 
                    )
                    """, reg1)
                connection.commit()
        print(f'Объявление {reg_id} добавлено в базу данных')
    ##connection.close()

def list_region(data):
    print(f'###################### data {type(data["data"])}')

    all_id = []
    for dataitems in data['data']:
        if dataitems['id'] in all_id:
            print('IIIIDDDD Поймали ДУБЛЯЖ!!!!!!!!!!!!!!!!!!!!!')
            break
        all_id.append(dataitems['id'])
        # Добавляем количество полей для корректного запроса заполнения SQL
        dataitems.setdefault('url_name', 'None')  # , value)
        dataitems.setdefault('index_post', 'None')  # , value)
        check_region(dataitems)
        print(dataitems)

    all_id.sort()
    print(all_id)
       #except AttributeError:

def list_city(data):

    all_id = []
    for dataitems in data['data']:
        if dataitems['id'] in all_id:
            print('IIIIDDDD Поймали ДУБЛЯЖ!!!!!!!!!!!!!!!!!!!!!')
            break
        all_id.append(dataitems['id'])
        dataitems.setdefault('url_name', 'None')  # , value)
        dataitems.setdefault('index_post', 'None')  # , value)
        check_region(dataitems)

    all_id.sort()
    print(all_id)
       #except AttributeError:


def Open_json_region():

    with open("Data/avito_region.json", encoding='utf-8') as file:
        data = json.load(file)
        #list_dict(data)
        list_region(data)
        #print(data)

def Open_json_city():
    with open("Data/avito_city.json", encoding='utf-8') as file:
        data = json.load(file)
        # list_dict(data)
        list_city(data)
        # print(data)


if __name__ == '__main__':
    name = "Тарасов"
    search_city(name)
    #create_city_tab()
    #create_regions_tab()
    #Open_json_region()
    #reg = {'id': '777777', 'name': 'ЁЁЁЁ', 'parent_Id': '777776', 'url_name': 'None', 'index_post': 'None'}
    #check_region(reg)
    #Open_json_city()
