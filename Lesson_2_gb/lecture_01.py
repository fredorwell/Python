# Запись и создание файла
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.close()

# # Запись и создание файла
# with open('file.txt', 'a') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# Чтение файла
# path = "file.txt"
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
# exit()


# Заранее определенные значения параметров
# def new_string(symbol, count = 3):
#     return symbol * count
#
# print(new_string('!', 5))
# print(new_string('!'))
# print(new_string(5))

# Неограниченное кол-во параметров
# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
#
#
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2

# Рекурсии
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
#
# list = []
# for e in range(1, 10):
#  list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34


# Кортежи
# a = (3, 4, 5)
# print(a)
# print(a[0])
#
# for item in a:
#     print(item)

# Словари

# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
# print(dictionary)
# print(dictionary['left'])
#
# for k in dictionary.keys():
#     print(k)
#
# for k in dictionary.values():
#     print(k)

# Работа с множествами
# colors = {'red', 'green', 'blue'}
# print(colors)  # {'red', 'green', 'blue'}
# colors.add('red')  # Не уникальное значение не добавиться в множество
# print(colors)  # {'red', 'green', 'blue'}
# colors.add('gray')  # Уникальное значение добавиться в множество
# print(colors)  # {'red', 'green', 'blue', 'gray'}
# colors.remove('red')  # удаление элемента, повторно удалить нельзя
# print(colors)  # {'green', 'blue', 'gray'}
# colors.discard('red')  # Софт удаление значения
# print(colors)  # {'green', 'blue', 'gray'}
# colors.clear()  # очистка множеств
# print(colors)  # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#  .union(b) \
#     .difference(a.intersection(b))
# # {1, 21, 3, 13}
#
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)  # замороженное или неизменяемое множество
# print(b) # frozenset({1, 2, 3, 5, 8})