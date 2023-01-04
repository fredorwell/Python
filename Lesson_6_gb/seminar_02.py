# 1. Напишите программу вычисления арифметического выражения заданного строкой.Используйте операции +, -, /, *.приоритет
# операций стандартный.
#
# *Пример: *
# 2 + 2 = > 4;
# 1 + 2 * 3 = > 7;
# 1 - 2 + 5 = > -5;


string = "1 - 2 + 5 * 8 / 2 + 6 * 3"
print(string)
list = string.split()
print(list)
for i in range(len(list)):
    if list[i].isdigit():
        list[i] = int(list[i])
print(list)

result = 0

while len(list) != 1:
    i = 0
    while ('*' in list or '/' in list) and i < len(list):
        if list[i] == '*':
            result = list[i-1] * list[i+1]
            list.pop(i)
            list.pop(i)
            list[i-1] = result

        elif list[i] == '/':
            result = list[i-1] / list[i+1]
            list.pop(i)
            list.pop(i)
            list[i-1] = result
        else:
            i += 1
        print(list)

    while ('+' in list or '-' in list) and i < len(list):
        if list[i] == '+':
            result = list[i-1] + list[i+1]
            list.pop(i)
            list.pop(i)
            list[i-1] = result

        elif list[i] == '-':
            result = list[i-1] - list[i+1]
            list.pop(i)
            list.pop(i)
            list[i-1] = result
        else:
            i+=1
        print(list)



print(list)

# string = '1 + 2'
# string = string.split()
# print(string)
#
# for i in range(len(string)):
#     if string[i].isdigit():
#         string[i] = int(string[i])
# print(string)
#
# while '+' in string:
#     i = string.index('+')
#     string[i] = +

