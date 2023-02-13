import sqlite3
import time
import requests
from config import token, chat_id


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
    with sqlite3.connect('realty.db') as connection:
        cursor = connection.cursor()
        # #это может быть кортеж с информацией о пользователе.
        #user = ('00002', 'Lois', 'Lane', 'Female')

        # #Если его нужно загрузить в базу данных, тогда подойдет следующий формат:
        #
        # cur3.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
        # conn.commit()

        cursor.execute("""
            SELECT offer_id FROM offers WHERE offer_id = (?)
        """, (offer_id,))
        result = cursor.fetchone()
        print(f'result cursor.fetchone() = {result}')
        user = ('00003', 'Lois2', 'Lane2', 'Female2', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5',
                '5', '6')


        if result is None:

            # send_telegram(offer)
            #ok cursor.execute("INSERT INTO offers VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", user)
            #""" #: id_item,: category_name,: category_kod) """, offer)
            #ok connection.commit()

            #
            #     : date,: time,: title_desk,: title_full,: img,: price,
            #     : address,: coords,: url,: uri_mweb,: offer_id,: area,
            #     : rooms,: floor,: total_floor)
            # """, offer)

            #user1 = {"id": 100, "name": "Rumpelstiltskin", "dob": "12/12/12"}
            #c.execute("INSERT INTO users VALUES (:id, :name, :dob)", user1)
            #or
            #c.execute("INSERT INTO stocks VALUES (?,?,?)", [dict["id"], dict["name"], dict["dob"]])

            cursor.execute("""
                INSERT INTO offers 
                VALUES (NULL, :id_item, :category_name, :category_kod, 
                :date, :time, :title_desk, :title_full, :img, :price,
                :address, :coords, :url, :uri, :uri_mweb, :offer_id, :area,
                :rooms, :floor, :total_floor)
                """, offer)
            connection.commit()
            print(f'Объявление {offer_id} добавлено в базу данных')


        # cursor.execute("""INSERT INTO offers VALUES (NULL,: id_item,: category_name,: category_kod,{date},
        # : " ", : title_desk,: title_full,: img,: price, : address,: coords,: url,"",: uri_mweb,: offer_id,: area,
        # : rooms,: floor,: total_floor)""", offer2)

        # VALUES(NULL,: url,:offer_id,: date,:price,
        # : address,:area,: rooms,:floor,: total_floor)

        # (NULL,: url,:offer_id,: date,:price,: address,: area,: rooms,:floor,: total_floor) id, id_item,
        # : category_name,: category_kod,: date,: time,: title_desk,: title_full,: img,: price,: address,
        # : coords,: url,: uri_mweb,: offer_id,: area,: rooms floor,: total_floor

        # connection.commit()
        #    print(f'Объявление {offer_id} добавлено в базу данных')


def check_database_old(offer):
    print('check_database')
    offer_id = offer["offer_id"]
    # print(offer_id)
    with sqlite3.connect('realty.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT offer_id FROM offers WHERE offer_id = (?)
        """, (offer_id,))
        result = cursor.fetchone()
        print(f'result cursor.fetchone() = {result}')
        if result is None:
            # send_telegram(offer)
            cursor.execute("""
                INSERT INTO offers
                VALUES (NULL,: id_item,: category_name,: category_kod,
                : date,: time,: title_desk,: title_full,: img,: price,
                : address,: coords,: url,: uri_mweb,: offer_id,: area,
                : rooms,: floor,: total_floor)
            """, offer)

            # VALUES(NULL,: url,:offer_id,: date,:price,
            # : address,:area,: rooms,:floor,: total_floor)

            # (NULL,: url,:offer_id,: date,:price,: address,: area,: rooms,:floor,: total_floor)
            #  id, id_item,: category_name,: category_kod,: date,: time,: title_desk,: title_full,: img,: price,: address,: coords,: url,: uri_mweb,: offer_id,: area,: rooms floor,: total_floor
            connection.commit()
            print(f'Объявление {offer_id} добавлено в базу данных')


def format_text(offer):
    title = f"{offer['rooms']}, {offer['area']} м2, {offer['floor']}/{offer['total_floor']} эт."

    d = offer['date']
    date = f"{d[8:10]}.{d[5:7]} в {d[11:16]}"

    text = f"""{offer['price']} ₽
<a href='{offer['url']}'>{title}</a>
{offer['address']}
{date}"""

    return text


def send_telegram(offer):
    text = format_text(offer)
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'HTML'
    }
    response = requests.post(url=url, data=data)
    print(response)


def main():
    pass


if __name__ == '__main__':
    main()
