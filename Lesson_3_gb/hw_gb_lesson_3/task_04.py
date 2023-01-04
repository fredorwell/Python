# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без применения
# встроенных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def IntToBinary(num):
    result = ""
    while num != 0:
        result = str(num % 2) + result
        num //= 2
    return result


number = int(input('Введите чилсло: '))
print(IntToBinary(number))
