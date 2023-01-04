# Написать программу, которая будет выводить в консоль заданный текст (Python - один из самых популярных языков
# программирования в мире), затем принимать из консоли шаблон подстроки и удалять в заданом тексте все слова в
# которых присутствует введенный шаблон

old_str = 'Python - один из самых популярных языков один программирования в мире'
search_str = 'один'


# поиск
list_str = old_str.split(sep=' ')
print(list_str)
delete_index =[]
for i in range(len(list_str) -1):
    if list_str[i].find(search_str) != -1:
        delete_index.append(i)
print(list_str)
print(delete_index)

for i in range(len(delete_index), 0):
    list_str.pop(delete_index[i])

print(list_str)
print(delete_index)
