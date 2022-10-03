import pandas as pd
import openpyxl

dict_list = [
            {'PCS_id': 3982, 'kod_start': '20191', 'Log_Time': '2020-12-29 13:11:04.663', 'start': '2020-12-29 13:11:04.897', 'kod_stop': '29321', 'stop': '2020-12-29 13:47:40.445', 'parent_group_file': 'ФЛУКОНАЗОЛ', 'kalibr': '500', 'kog_group': '000000039', 'file_dir': 'Флуконазол 150', 'Full_path': 'FULL PATH', 'file_name': 'Флуконазол 500-000000039.VDF', 'GTIN_kod': '--', 'GTIN_name': '--', 'last_kod_id': '--', 'last_kod': '--', 'status': '--'},
            {'PCS_id': 3991, 'kod_start': '29322', 'Log_Time': '2020-12-29 13:52:19.974', 'start': '2020-12-29 13:52:20.192', 'kod_stop': '30499', 'stop': '2020-12-29 13:57:16.935', 'parent_group_file': 'ФЛУКОНАЗОЛ', 'kalibr': '500', 'kog_group': '000000039', 'file_dir': 'Флуконазол 150', 'Full_path': 'FULL PATH', 'file_name': 'Флуконазол 500-000000039.VDF', 'GTIN_kod': '--', 'GTIN_name': '--', 'last_kod_id': '--', 'last_kod': '--', 'status': '--'},
            {'PCS_id': 3998, 'kod_start': '30500', 'Log_Time': '2020-12-29 15:19:49.869', 'start': '2020-12-29 15:19:50.073', 'kod_stop': '31506', 'stop': '2020-12-29 15:24:15.198', 'parent_group_file': 'ФЛУКОНАЗОЛ', 'kalibr': '500', 'kog_group': '000000039', 'file_dir': 'Флуконазол 150', 'Full_path': 'FULL PATH', 'file_name': 'Флуконазол 500-000000039.VDF', 'GTIN_kod': '--', 'GTIN_name': '--', 'last_kod_id': '--', 'last_kod': '--', 'status': '--'},
            ]

df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
                  index=['one', 'two', 'three'], columns=['a', 'b', 'c'])



#
    # {‘Student_Name’: ‘Samreena’, ‘Course_Title’: ‘SQA’, ‘GPA’: 3.1},
    # {‘Student_Name’: ‘Raees’, ‘Course_Title’: ‘SRE’, ‘GPA’: 3.3},
    # {‘Student_Name’: ‘Sara’, ‘Course_Title’: ‘IT Basics’, ‘GPA’: 2.8},
    # {‘Student_Name’: ‘Sana’, ‘Course_Title’: ‘Artificial Intelligence’, ‘GPA’: 4.0}
    # ]

# Create the DataFrame


def prnDataframe():
    df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
                   index=['one', 'two', 'three'], columns=['a', 'b', 'c'])
    #
    # print(df)
    # Create a list of dictionaries

    # Create the DataFrame
    dframe = pd.DataFrame(dict_list)
    print(dframe)

def pandasToExcel():
    df2 = df[['a', 'c']]
    print(df2)
    with pd.ExcelWriter('pandas_to_excel.xlsx') as writer:
        df.to_excel(writer, sheet_name='sheet1')
        df2.to_excel(writer, sheet_name='sheet2')


if __name__ == '__main__':

    #prnDataframe()
    pandasToExcel()
