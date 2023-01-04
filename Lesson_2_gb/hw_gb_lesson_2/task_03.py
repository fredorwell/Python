# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод
import random


def ShuffleList(list):
    last_index = len(list) - 1

    while last_index > 0:
        rand_index = random.randint(0, last_index)
        list[last_index], list[rand_index] = list[rand_index], list[last_index]
        last_index -= 1

    return list


old_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(old_list)
new_list = ShuffleList(old_list)
print(new_list)

