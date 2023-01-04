# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def SummDig(num):
    result = 0
    num = num.replace(',', '.')
    if float(num) < 0:
        num *= -1
    for i in str(num):
        if i != '.':
            result += int(i)
    return result


number = input('Введите число ')
print(f'Сумма чисел равна {SummDig(number)}')
