import sqlite3

def check_category_path(id_find, url_str):

    id_find = id_find
    url_str = url_str

    reg_in = id_find
    reg1 = reg_in + "%"
    reg2 = "%" + reg_in.lower() + "%"
    trupl_str = (reg1, reg2)
    print(f'trupl_str {trupl_str}')

    list_str = []
    list_str.append(reg1)
    list_str.append(reg2)
    print(f"list_str {list_str}")

    dict_str = dict()
    values = [reg1, reg2]

    param_names = [f"reg{i + 1}" for i in range(len(values))]
    in_str = ", ".join(":" + p for p in param_names)  # print(",".join("Python")) >>>P,y,t,h,o,n
    params = dict(zip(param_names, values))

    query_str = """
    SELECT name, id FROM categories WHERE id LIKE ? ORDER BY id
      """

    query_str_3 = """
    SELECT name, id FROM categories WHERE (lower(id) LIKE ?) OR (lower(id) LIKE ?) ORDER BY id 
      """

    with sqlite3.connect('realty.db') as connection:
        cursor = connection.cursor()
        # cursor.execute((query_str),(reg1,))
        cursor.execute((query_str), (reg_in,))
        # str30 OK!!!!
        # cursor.execute((query_str_3), (reg1, reg2))
        # str31 list_str OK!!!!
        # cursor.execute((query_str_3), (list_str))
        # str32 trupl_str OK!!!!
        # cursor.execute((query_str_3), (trupl_str))

    connection.commit()
    ##connection.close()

'''
# (UPDATE table1 SET url_name = ? WHERE id = ), (url_str, id_find) ;
# UPDATE table1 SET name = ‘Людмила Иванова’ WHERE id = 2;
#
# Убедимся, что модификация данных прошла успешно, выполнив команду SELECT:
# sqlite> SELECT * FROM table1;
# 2|Людмила Иванова|21|Бухгалтер|35232.2
'''

def search_category_id(id):

        reg_in = id
        reg1 = reg_in + "%"
        reg2 = "%" + reg_in.lower() + "%"
        trupl_str = (reg1, reg2)
        print(f'trupl_str {trupl_str}')

        list_str = []
        list_str.append(reg1)
        list_str.append(reg2)
        print(f"list_str {list_str}")

        dict_str = dict()
        values = [reg1, reg2]

        param_names = [f"reg{i + 1}" for i in range(len(values))]
        in_str = ", ".join(":" + p for p in param_names)  # print(",".join("Python")) >>>P,y,t,h,o,n
        params = dict(zip(param_names, values))

        sql = f"""SELECT name, id FROM categories
                 WHERE name in ({in_str})"""
        print(f'params {params} , in_str {in_str}, sql {sql}')
        dict_str.setdefault("reg1", reg1)  # append("reg1",reg1) # + reg2
        dict_str.setdefault("reg2", reg2)  # append("reg1",reg1) # + reg2
        # val.append("reg2", reg2)
        # for key, value in values:
        #    countries_hdi[key] = value
        print(f'ПОИСК dict_str {dict_str["reg1"]} и {dict_str["reg2"]} ')

        with sqlite3.connect('realty.db') as connection:
                cursor = connection.cursor()
                # sql = ("CREATE INDEX index_my_table ON my_table (Field1, field2)")
                query_str = """
            SELECT name, id FROM categories WHERE id LIKE ? ORDER BY id
              """
                # Без регистра: like lower('%value%');
                # Для исключения символов: where column regexp '^[A-Za-z0-9]+$'
                # where lover(column_name) regexp '^[a-zа-яё]+$';
                # SELECT *FROM [table] WHERE ([table].[column] like <parameter>) OR (<parameter> = '%')

                query_str_3 = """
            SELECT name, id FROM categories WHERE (lower(id) LIKE ?) OR (lower(id) LIKE ?) ORDER BY id 
              """

                query_str_4 = """
            SELECT name, id FROM categories WHERE (lower(id) LIKE :reg1) OR (lower(id) LIKE :reg2) ORDER BY id 
              """

                query_str_5 = """
             SELECT name, id FROM categories WHERE (lower(id) LIKE ?) OR (lower(id) LIKE ?) ORDER BY id
               """

                # str переменные
                # cursor.execute((query_str),(reg1,))
                cursor.execute((query_str), (reg_in,))
                # str30 OK!!!!
                # cursor.execute((query_str_3), (reg1, reg2))
                # str31 list_str OK!!!!
                # cursor.execute((query_str_3), (list_str))
                # str32 trupl_str OK!!!!
                # cursor.execute((query_str_3), (trupl_str))
                # str4 OK dict_str!!!!
                # cursor.execute((query_str_4), (dict_str))  # [0], val[1]))
                # str5 OK sql динамически сформирован весь запрос!!!!
                # cursor.execute(sql, (params))#[0], val[1]))
                # cursor.execute("""
                # SELECT name FROM regions WHERE name LIKE ? ORDER BY name
                #   """, (reg1,))
                # result = cursor.fetchone()
                result = cursor.fetchall()
                print(f'result cursor.fetchall() = {len(result)} {result}')
                # print(result[0])


def search_category_name(name):

    reg_in = name
    reg1 = reg_in + "%"
    reg2 = "%" + reg_in.lower() + "%"
    trupl_str = (reg1, reg2)
    print(f'trupl_str {trupl_str}')

    list_str = []
    list_str.append(reg1)
    list_str.append(reg2)
    print(f"list_str {list_str}")

    dict_str = dict()
    values = [reg1, reg2]

    param_names = [f"reg{i + 1}" for i in range(len(values))]
    in_str = ", ".join(":" + p for p in param_names)  # print(",".join("Python")) >>>P,y,t,h,o,n
    params = dict(zip(param_names, values))

    sql = f"""SELECT name, id FROM categories
             WHERE name in ({in_str})"""
    print(f'params {params} , in_str {in_str}, sql {sql}')
    dict_str.setdefault("reg1", reg1)  # append("reg1",reg1) # + reg2
    dict_str.setdefault("reg2", reg2)  # append("reg1",reg1) # + reg2
    # val.append("reg2", reg2)
    # for key, value in values:
    #    countries_hdi[key] = value
    print(f'ПОИСК dict_str {dict_str["reg1"]} и {dict_str["reg2"]} ')

    with sqlite3.connect('realty.db') as connection:
        cursor = connection.cursor()
        # sql = ("CREATE INDEX index_my_table ON my_table (Field1, field2)")
        query_str = """
        SELECT name, id FROM categories WHERE name LIKE ? ORDER BY name
          """
        # Без регистра: like lower('%value%');
        # Для исключения символов: where column regexp '^[A-Za-z0-9]+$'
        # where lover(column_name) regexp '^[a-zа-яё]+$';
        # SELECT *FROM [table] WHERE ([table].[column] like <parameter>) OR (<parameter> = '%')

        query_str_3 = """
        SELECT name, id FROM categories WHERE (lower(name) LIKE ?) OR (lower(name) LIKE ?) ORDER BY name 
          """

        query_str_4 = """
        SELECT name, id FROM categories WHERE (lower(name) LIKE :reg1) OR (lower(name) LIKE :reg2) ORDER BY name 
          """

        query_str_5 = """
         SELECT name, id FROM categories WHERE (lower(name) LIKE ?) OR (lower(name) LIKE ?) ORDER BY name 
           """

        # str переменные
        #cursor.execute((query_str),(reg1,))
        cursor.execute((query_str), (reg_in,))
        # str30 OK!!!!
        # cursor.execute((query_str_3), (reg1, reg2))
        # str31 list_str OK!!!!
        # cursor.execute((query_str_3), (list_str))
        # str32 trupl_str OK!!!!
        # cursor.execute((query_str_3), (trupl_str))
        # str4 OK dict_str!!!!
        #cursor.execute((query_str_4), (dict_str))  # [0], val[1]))
        # str5 OK sql динамически сформирован весь запрос!!!!
        # cursor.execute(sql, (params))#[0], val[1]))
        # cursor.execute("""
        # SELECT name FROM regions WHERE name LIKE ? ORDER BY name
        #   """, (reg1,))
        # result = cursor.fetchone()
        result = cursor.fetchall()
        print(f'result cursor.fetchall() = {len(result)} {result}')
        # print(result[0])


if __name__ == '__main__':

    id = '105'
    name = "Товары для компьютера"
    #search_category_name(name)
    search_category_id(id)
