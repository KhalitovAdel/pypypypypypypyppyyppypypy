from functools import reduce

days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб']
print('вс' in days)
print('ср' in days)
print(days.count('пн'))  # count выводит количество 'пн' в списке

days.append('вс')
print(days)

month = [i for i in range(31)]  # создание  массива-месяц
month.pop(0)  # удаление дня 0
'''rda = [0,1,2,3,4,5,6,7,8,27,54,8]
rda.pop(2)
rda = [0,1,3,4,5,6,7,8]'''

del month[20:30]  # удаление от 20 до 30 элементов
del month[10]
month.insert(10, 11)  # вставляет что-то по определенному индексу,
# 10 это индекс, 11 это то, что нужно вставить
month.pop(5)  # вынимает и удаляет из списка по индексу
month.remove(8)  # удаляет первы элемент из списка
month.reverse()  # меняет местами элементы списка
# TODO:       домашка: привести примеры
month.sort()  # сортировка списка
print(month)
# range(start:stop:step)
day_hours = tuple(range(24))  # создание кортежа (неизменяемого массива)
print(day_hours)
# TODO: уточнить
March = month.copy()  # создание копии
print(March)
March.clear()  # чистка массива
print(March)
# day_hours.append(5): error
# day_hours.extend(5): error
# day_hours.reverse(): error
# day_hours.sort(): error
x = (1, 2, 3, 4)
y = (5, 6, 7, 8)

# Объединение двух кортежей для формирования нового кортежа
z = x + y
print(z)
''' к кортежу можно применять: count,
len, min,max,sum, sorted (но при его использовании возвращется список)'''
# mup method:
a = [-1, 2, -5, 10, -12]  # создаем список
b = list(map(abs, a))  # применяем map с функцией abs (значение по модулю) к списку а
# TODO: написать пример с функцией
print(b)
c = map(lambda x: x ** 2, a)  # функция внутри скобок создается с помощью lambda
print(c)

s = list(map(int, input().split()))  # заносит в список строку чисел, введенную пользователем
lol = list('po klsd ikdt s'.split())
print(s)
# filter method:
q = [i * 3 for i in range(7)]
print(q)
res = list(filter(lambda x: x % 2, q))  # если выполняется условие, то значение из q заносится в список
print(res)
# zip method: объединяет по каждому элементу с каждого списка, делая кортеж из них, см. пример короче
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = 'abcdefghij'
piz = list(zip(a, b, c))
print(piz)
# reduce method: функции с помощью lambda
items = [1, 24, 17, 14, 9, 32, 2]
all_max = reduce(lambda a, b: a if (a > b) else b, items)
print(all_max)
# TODO написать пример с reduce
