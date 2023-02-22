import json
import os
import sqlite3
from pprint import pprint
from urllib.parse import urlparse


def get_dict_files_dir():

    path_json = 'F:\Data\json\\'
    file_path = path_json + "cat_633350.json"
    x = [f.name for f in os.scandir(path_json) if f.is_file()]
    print(x)
    print(f'\n\n\n {file_path}')

def url_parser(url):

    parts = urlparse(url)
    directories = parts.path.strip('/').split('/')
    queries = parts.query.strip('&').split('&')

    elements = {
        'scheme': parts.scheme,
        'netloc': parts.netloc,
        'path': parts.path,
        'params': parts.params,
        'query': parts.query,
        'fragment': parts.fragment,
        'directories': directories,
        'queries': queries,
    }

    return elements


def parse_url_path(file_name):

    with open(file_name, 'r', encoding='utf-8') as file:
        #json.dump(ress, file, indent=2, ensure_ascii=False)
        data = json.load(file)
        try:
            buf = data['shops']
        except KeyError:
            print('Файл Пуст')
            return False

        url_path_cat = buf['uri_mweb']
        frame = url_parser(url_path_cat)
        dirLst = frame['path'].split("/")
        url_path = dirLst[-1].strip()
        id_cat = (buf["uri"].strip())[-6:]
        print(f'{url_path}  {id_cat}')


def find_file(file_path):

    file_path = file_path
    path_json = 'F:\Data\json\\'
    full_path = path_json + file_path

    with sqlite3.connect('realty.db', timeout=300) as connection:
        cursor = connection.cursor()

        query_str = f"""UPDATE cityes 
        SET index_post = '1' WHERE id = ?
        """

        if os.path.exists(full_path):
            print(full_path)
            #            cursor.execute((query_str), (cit_id,))  # !!!!OK
            #            connection.commit()
            print('Update ', connection.total_changes)  # rowcount())#total_changes total_changes() )
            parse_url_path(full_path)
            #connection.commit()

        else:
            print(f' NOT full_path {full_path}')


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        # col[0] is the column name
        d[col[0]] = row[idx]
    return d
    #         variant 2
    # fields = [column[0] for column in cursor.description]
    # return {key: value for key, value in zip(fields, row)}


def get_data_to_json():
    database = 'realty.db'
    conn = sqlite3.connect(database)  # conn.row_factory = sqlite3.Row
    conn.row_factory = dict_factory
    c = conn.cursor()
    temp = c.execute("SELECT * FROM cityes WHERE url_path = 'None'")
    # result = [{k: item[k] for k in item.keys()} for item in temp] #print(f'!!!!!!!!!!!!!! result = {result}')
    rst = c.fetchall()  # rst is a list of dict
    # pprint(rst)#, depth=0) #print(json.dumps(rst, sort_keys=False, indent=4))
    #list_id(rst)
    #conn.close()
    return rst #jsonify(rst)


if __name__ == '__main__':
    city_dict = get_data_to_json()
    for elem in city_dict:

        #print(f'{elem["name"]}  {elem["id"]}')
        #"cat_633350.json"
        full_name = f'cat_{elem["id"]}.json'
        #print(full_name)
        find_file(full_name)
    #pprint(city_dict)

    #get_from_file(file_path)
    #get_dict_files_dir()

# Another example with `scandir` (a little variation from docs.python.org)
# This one is more efficient than `os.listdir`.
# In this case, it shows the files only in the current directory
# where the script is executed.

#import os
# with os.scandir(path_json) as i:
#     print(i)
    # for entry in i:
    #     if entry.is_file():
            #print(entry.name)