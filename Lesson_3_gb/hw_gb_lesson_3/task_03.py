# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# Прим: Данный вариант программы работает исключительно с дробными частями от 0.001 до 0.9


import random


def FloatSide(num):
    result = num - int(num)
    return round(result, 3)


def DiffMinMaxFloat(list):
    min_float = FloatSide(list[0])
    max_float = FloatSide(list[0])

    for i in range(len(list)):
        if FloatSide(list[i]) > max_float:
            max_float = FloatSide(list[i])
        if FloatSide(list[i]) < min_float:
            min_float = FloatSide(list[i])

    result = (max_float - min_float)
    return round(result, 3)


def CreateRandList(num):
    result_list = []
    for i in range(num):
        f = random.uniform(0, 9)
        fl_part = random.randint(1, 3)
        result_list.append(round(f, fl_part))
    return result_list


number = int(input('Введите размер списка '))
my_list = CreateRandList(number)
print(my_list)
diff_float = DiffMinMaxFloat(my_list)
print(f' Разница - {diff_float}')