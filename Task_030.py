# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_el = int(input('Введите значение первого элемента прогрессии: '))

difference = int(input('Введите разность прогрессии: '))

count_of_elements = int(input('Введите количество элементов: '))

progression_list = []

for i in range(0, count_of_elements):
    progression_list.append(first_el)
    first_el += difference
print(progression_list)
