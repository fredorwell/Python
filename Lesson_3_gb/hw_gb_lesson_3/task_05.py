# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Fib(num):
    if num in [1, 2]:
        return 1
    else:
        return Fib(num - 1) + Fib(num - 2)


def NegaFib(num):
    if num == 1:
        return 1
    elif num == 2:
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, num):
            num1, num2 = num2, num1 - num2
        return num2


def FibAndNegaFib(num):
    result = []
    for i in range(1, num + 1):
        result.append(Fib(i))
        result.insert(0, NegaFib(i))
    return result


number = int(input('Введите размер списка '))
print(FibAndNegaFib(number))
