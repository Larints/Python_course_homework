# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

some_list = [random.randint(0, 30) for i in range(0, 30)]

max_value = int(input('Введите заданный максимум: '))
min_value = int(input('Введите заданный минимум: '))

for i in range(len(some_list)):
    if min_value <= some_list[i] <= max_value:
        print(some_list[i])