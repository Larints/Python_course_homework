# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

import random

print('Введите количество кустов: ')

bush = int(input())

garden_bed = []

for i in range(bush):
    garden_bed.append(random.randint(1, 10))

print(garden_bed)

result_count = []

for i in range(bush-1):
    summ = garden_bed[i - 1] + garden_bed[i] + garden_bed[i + 1]
    result_count.append(summ)
result_count.append(garden_bed[-2] + garden_bed[-1] + garden_bed[0])

print(f'Максимальное количество ягод - {max(result_count)}')