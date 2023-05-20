# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

print('Введите номер билета')

ticket = int(input())
if ticket < 100000:
    print('Цифр в билете, менее шести')
elif ticket > 999999:
    print('Цифр в билете, более шести')
else:
    left_side = ticket // 1000
    right_side = ticket % 1000
    sum_of_left_side = 0
    sum_of_right_side = 0
    while left_side > 0:
        sum_of_left_side += left_side % 10
        left_side = left_side // 10
    while right_side > 0:
        sum_of_right_side += right_side % 10
        right_side = right_side // 10
    if sum_of_left_side == sum_of_right_side:
        print('Бомба, билет счастливый!')
    else:
        print('Не повезло, увы')