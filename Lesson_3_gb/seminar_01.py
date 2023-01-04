# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некий символ.



my_list = ['qwe421', '421444', 'asd123', 'asadasdsd', 'fg111h']
search_char = input('Введите символ: ')

for item in my_list:
    for char in item:
        if char == search_char:
            print(f'Символ {search_char} - присутсвует в элементе {item}')
            break
    else:
        print(f'Символ {search_char} - отсутствует в элементе {item}')


# for item in my_list:
#     if search_char in item:
#         print(f'Символ {search_char} - присутсвует в элементе {item}')
#     else:
#         print(f'Символ {search_char} - отсутствует в элементе {item}')