import sqlite3


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
    temp = c.execute("SELECT * FROM categories")
    # result = [{k: item[k] for k in item.keys()} for item in temp] #print(f'!!!!!!!!!!!!!! result = {result}')
    rst = c.fetchall()  # rst is a list of dict
    # pprint(rst)#, depth=0) #print(json.dumps(rst, sort_keys=False, indent=4))
    #list_id(rst)
    #conn.close()
    return rst #jsonify(rst)
