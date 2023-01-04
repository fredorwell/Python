# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
# плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4 -> 1
# x=-34; y=-30 -> 3

def QuarterCheck(coor_x, coor_y):
    if coor_x == 0:
        print(f' x = {coor_x}, а это не корректные координаты')
    elif coor_y == 0:
        print(f' y = {coor_y}, а это не корректные координаты')
    elif coor_x > 0 and coor_y > 0:
        print(f'X = {coor_x}, Y = {coor_y}, точка находится в первой четверти')
    elif coor_x < 0 and coor_y > 0:
        print(f'X = {coor_x}, Y = {coor_y}, точка находится во второй четверти')
    elif coor_x < 0 and coor_y < 0:
        print(f'X = {coor_x}, Y = {coor_y}, точка находится в третьей четверти')
    elif coor_x > 0 and coor_y < 0:
        print(f'X = {coor_x}, Y = {coor_y}, точка находится в четвертой четверти')

print('Вам необходимо ввести координаты не равные нулю')
x = int(input('Введите координату X: '))
y = int(input('Введите координату Y: '))
QuarterCheck(x, y)
