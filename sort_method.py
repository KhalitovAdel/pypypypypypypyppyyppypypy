ex = [21, 53, 54, 896, 21, 354, 3, 5, 42, 45, 1]


def sum_digits(num):
    """функция, которая возвращает сумму цифр числа"""
    digits = [int(x) for x in str(num)]
    return sum(digits)


numbers = [23, 77, 19, 310, 219]

numbers.sort(reverse=True, key=sum_digits)  # сортировка списка по уменьшению сумм цифр числа
ex.sort(reverse=False, key=sum_digits)  # сортировка списка по возрастанию
print()
