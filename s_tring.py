import time

# Операции:
# (конкатинировать строка + строка, из строки чисел, сделать числа,
# узнать длину строки, узнать регистр букв или привести в регистр,
# как привести строку к булиеву значению,
# замена без регулярного выражения АвГА заменить букву А на 5, чтобы получить 5вГ5)
start_time = time.time()
str_concat = 'lol ' + 'kek'

str_integer = int('4343')

str_length = len('0123456789')

str_isupper = 'FFF'.isupper()

str_islower = 'lll'.islower()

str_is_number = '4444'.isnumeric()

str_question = '444ff'.isupper()

str_is_boolean1 = bool('')

str_is_boolean2 = bool(' ')

str_is_boolean3 = bool('23')

str_replace1 = '(lol'.replace('(', '')

str_replace2 = '(lol('.replace('(', '', 1)

str_to_upper = 'lll'.upper()

str_to_lower = 'FFF'.lower()

str_name_default = 'khalitov'

str_first = str_name_default[0]

str_all_from_first = str_name_default[1:]

str_name_done = str_first.upper() + str_all_from_first.lower()

array_from_str = list(str_name_done)

str_from_array = ''.join(array_from_str)

str_raw = ' 121323123@ 123123123. '

str_clear = str_raw.strip()

str_index = str_raw.index('@')
print(round(time.time() - start_time, 4))

print()
