# 1.Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# *Примеры: *
#
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8, 9 -> нет

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))

if ((num_1 ** 2) == num_2 or (num_2 ** 2) == num_1):
    print(f'Да, является квадратом числа')
else:
    print(f'Нет, число не является квадратом другого числа')