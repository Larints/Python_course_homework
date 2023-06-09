# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть


import random

print('Введите количество монеток: ')

n = int(input())
heads_count = 0
tails_count = 0

for i in range(n):
    coin = random.randint(0,1)
    print(coin, end = ' ')
    if coin == 0:
        tails_count += 1
    else:
        heads_count += 1

if heads_count == n:
    print(f'\nВсе монеты выпали орлом вверх')
elif tails_count == n:
    print(f'\nВсе монеты выпали решкой вверх')
elif heads_count > tails_count:
    print(f'\nКоличество монеток орлом вверх составило {heads_count}, '
          f'их больше, чем монет лежащих вверх решкой, следовательно нужно перевернуть монетки, '
          f'лежащие вверх решкой, всего {tails_count} монет(ы)')
elif tails_count > heads_count:
    print(f'\nКоличество монеток решкой вверх составило {tails_count}, '
          f'их больше, чем монет лежащих вверх орлом, следовательно нужно перевернуть монетки, '
          f'лежащие вверх орлом, всего {heads_count} монет(ы)')
else:
    print(f'\nКоличество монет на столе орлом и решкой вверх одинаково')