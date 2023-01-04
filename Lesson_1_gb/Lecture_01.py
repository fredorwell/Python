# Типы данных
value = None;
a = 123
b = 1.23
s = 'qwerty'
print(type(a))
print(type(b))
print(type(value))
print(type(s))

print(a, '-', b,'-', s)
print('{} - {} - {}'.format(a,b,s))
print(f'{a} - {b} - {s}')
f = True
print(f)

# Списки
list = ['1', '2', '3', 1, 2, 1.23]
print(list)

# Ввод и вывод данных
print('Введите A')
a = int(input())
print('Введите B')
b = int(input())
print(a, ' + ', b, ' = ', a+b)

# Арифметические операции
# +, -,*, /, %, //,**
# Приоритет операций
# **, ⊕, ⊖,*, /, //, %, +, -
# ( ) Скобки меняют приоритет

a = 1.3
b = 3
c = round(a*b, 3)
print(c)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |,^
# Кое-что ещё: is, is not, in, not in
a = 1 < 4 and 5 > 2
print(a)

# ветвление

a = int(input('A = '))
b = int(input('B = '))
if a>b:
    print(a)
else:
    print(b)

# Циклы while

original = 1223
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

# Циклы while - else

original = 1223
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит )')
print(inverted)

# Циклы for
list = [2, 4, 8, 16, 32]
for i in list:
    print(i)

# Строки
text = "qwert asdfg zxcv"
print(len(text)) #кол-во символов
print('qwe' in text) #поиск значения в строке
print(text.isdigit()) #проверка на числа ли в строке
print(text.islower()) #Проверка на нижний регистр
print(text.replace('qwe', 'QWE'))#Замена значений

# ф-ции
def f(x):
    if x == 1:
        return 'целое'
    elif x == 2.3:
        return 23
    else:
        return


arg = 2.3
print(f(arg))
print(type(f(arg)))