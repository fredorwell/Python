# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывестив консоль сам список и сумму его элементов.


def CreateList(num):
    result = []
    for i in range(1, num + 1):
        result.append(round((1 + 1 / i) ** i, 2))
    return result

def SumOfList(list):
    result = 0
    for i in list:
        result += float(i)
    return result


number = int(input("Введите число: "))
my_list = CreateList(number)
print(my_list)
print(f'Сумма всех элементов списка: {SumOfList(my_list)}')


