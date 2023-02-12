# n = int(input("Введите число: "))
# c = 0
# for i in range(2, n // 2+1):
#     if (n % i == 0):
#         c = c+1
# if (c <= 0):
#     print("Число простое")
# else:
#     print("Число не является простым")

# c = "helloh79s8dfg07abP3BC,DGSIC98Fewo   23r6dfghdgfhworld"
# k = sorted(c)
# print(k)
import re

txt = ("Мама",
"авТо",
"гриБ",
'Яблоко', 'яБлоко', 'ябЛоко', 'яблОко', 'яблоКо', 'яблокО', 'агент007', "стриж", "ГТО", 'Три богатыря')

for x in txt:
    c = re.findall(r"(^[а-я]*[А-Я][а-я]*)$", x)
    print(c)