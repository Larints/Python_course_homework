# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

print('Введите число А: ')

A = int(input())

print('Введите число B: ')

B = int(input())


def exponentiation(a, b):
   if b == 1:
       return a
   elif b == 0:
       return 1
   else:
       return a * exponentiation(a, b - 1)

print(exponentiation(A, B))