# Способы перебора массива:
# 1) for in
# 2) map
# 3) filter
# 4) reduce

# Методы
# 1) append - добавляет в конец массива
# 2) insert - добавляет элемент не затирая текущий массив на определенную позицию
# 3) extend - lобавляет много элементов в конец массива
# 4) clear -  TODO: пройти потом
# 5) copy - TODO: пройти потом
# 6) count
# 7) index
# 8) pop - удаляет элемент с определенного индекса, уменьшается ли длина массива
# 9) remove - удаляет элемент по его значению из массива
# 10) reverse - переворачивает массив
# 11) sort - сортирует массив

# Домашка: как заполнить массив arr(10) fill(1)


arr_for = [None, 1, 2, 3, 4, 5, 6, 7, 8]

for i in arr_for:
    print('for ' + str(i))


for_test = range(len(arr_for))

for i in for_test:
    print('for ' + str(i))


arr_map = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def map_handler(el):

    result = 0
    if el is not None:
        result = 10
    else:
        result = 0

    return result


result_map = list(map(map_handler, arr_map))

lol = type(None)

print(arr_for)

