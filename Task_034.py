# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#
# *Пример:*
#
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

letters_list = ["а", "у", "е", "о", "э", "я", "и", "ю"]

new_string = list(input('Ну ка Винни, вводи считалочку: ').lower().split())

result_array = []

def counting_rhyme(letter_list,phrase_list, result_array):
    i = 0
    count = 0
    while i < len(phrase_list):
        for j in range(len(letter_list)):
            if letter_list[j] in phrase_list[i]:
                count += phrase_list[i].count(letter_list[j])
        result_array.append(count)
        count = 0
        i += 1

    if len(set(result_array)) == 1:
        return 'Парам пам-пам'
    else:
        return 'Пам парам'

print(counting_rhyme(letters_list, new_string, result_array))










