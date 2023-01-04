import random
# list comprehension
my_list = [random.randint(0, 9) for i in range(5)]
print(f'Исходный список: {my_list}')
# filter
even_list = list(filter(lambda x: x%2 == 0, my_list))
print(f'Четные элементы: {even_list}')
# map + lambda
x10_list = list(map(lambda x: x * 10, my_list))
print(f'Список с элементами умноженными на 10: {x10_list}')
# zip
name_list = ['Александр', 'Алексей','Антон']
secondName_list = ['Александров', 'Алексеев','Антонов']
fullName_list = list(zip(secondName_list, name_list))
print(fullName_list)


