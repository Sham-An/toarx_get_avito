import sqlite3


def main():
    pass


def delete_records_city():
    try:
        with sqlite3.connect('category.db') as connection:
            cursor = connection.cursor()
            print("Подключен к SQLite")
            cursor.execute('DELETE FROM city;', );
            connection.commit()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            print("Соединение с SQLite закрыто")


def delete_records_category():
    try:
        with sqlite3.connect('category.db') as connection:
            cursor = connection.cursor()
            print("Подключен к SQLite")
            cursor.execute('DELETE FROM category;', );
            connection.commit()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            print("Соединение с SQLite закрыто")


# "id":4,"name":"Недвижимость","children"
def create_tab_category():
    # При подключении к базе, автоматически создается realty.db
    connection = sqlite3.connect('category.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE category(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_category integer,
            name_category_ru text,
            name_category_en text,
            parent_Id integer,
            parent_Id_url integer,
            id_children text,
            id_city_url2 integer,
            showMap text
            )     
    """)
    connection.close()


def create_tab_reg_city():
    # "data": [
    #     {
    #         "id": "621551",
    #         "name": "Чистенькая",
    #         "parent_Id": "621550"
    #     },
    #
    # При подключении к базе, автоматически создается realty.db
    connection = sqlite3.connect('reg_city.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE city(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_city integer,
            name_city_ru text,
            name_city_en text,
            parent_Id integer,
            parent_Id_url integer,
            id_city_url integer,
            id_city_url2 integer,
            index_post text,
            coords text
            )     
    """)
    connection.close()


def create_tab_items():
    # При подключении к базе, автоматически создается realty.db
    connection = sqlite3.connect('realty.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE offers (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_item integer,
            category_name text,
            category_kod text,
            date text,
            time text,
            title_desk text,
            title_full text,
            img text,
            price integer,
            address text,
            coords text,
            url text,
            uri text,
            uri_mweb text,
            offer_id integer,
            area integer,
            rooms text,
            floor integer,
            total_floor
        )     
    """)
    connection.close()


if __name__ == '__main__':
    # main()
    #create_tab_items()
    create_tab_category()
    create_tab_reg_city()
    #delete_records_city()
    #delete_records_category()
'''
#   id_item
    category_name
    category_kod
#    time 
    title 
    images = ''
    price 
    address 
    coords 
    uri 
    uri_mweb 
'''
