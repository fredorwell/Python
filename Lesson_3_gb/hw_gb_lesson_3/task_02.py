# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]
import random


def CreateRandList(num):
    new_list = []
    for i in range(num):
        new_list.append(random.randint(0, 9))
    return new_list


def PairMultiplicationList(list):
    result = []
    if int(len(list))%2 == 0:
        for i in range(int(len(list) / 2)):
            result.append(list[i] * list[(len(list) - 1) - i])
    else:
        for i in range(int(len(list)/ 2) + 1):
            result.append(list[i] * list[(len(list) - 1) - i])
    return result


count_element = int(input('Какого размера сгенерировать массив: '))
my_list = CreateRandList(count_element)
print(my_list)
print(PairMultiplicationList(my_list))

