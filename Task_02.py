# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

print('Введите трёхзначное число: ')
n = int(input())
summ = 0

if 100 <= n <= 999:
    while n > 0:
        summ += n % 10
        n = n // 10
    print(summ)
else:
    print('Число не является трёхзначным')