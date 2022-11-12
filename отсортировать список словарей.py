#https://www.youtube.com/watch?v=-ZHdlWyfL4s
import operator

users = [
    {'name': 'Вася', 'salary': 100, 'age': 55},
    {'name': 'Петя', 'salary': 500, 'age': 28},
    {'name': 'Саша', 'salary': 200, 'age': 21},
    {'name': 'Маша', 'salary': 300, 'age': 37},
    {'name': 'Алла', 'salary': 200, 'age': 24},
]

def get_data_for_sort(x):
    return x['salary'], x['name']


if __name__ == '__main__':
    sort1 = sorted(users, key=get_data_for_sort) # x['salary'], x['name']
    sort2 = sorted(users, key=lambda x: (x['salary'], x['name']), reverse=True)
    sort3 = sorted(users, key=operator.itemgetter('salary', 'name'))

    print("sort1", '\n')
    print(*sort1, sep='\n')
    print("sort2", '\n')
    print(*sort2, sep='\n')
    print("sort3", '\n')
    print(*sort3, sep='\n')