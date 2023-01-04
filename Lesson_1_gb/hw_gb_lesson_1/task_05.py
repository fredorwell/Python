# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в
# 2D пространстве (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ: найти расстояние в 3D пространстве)
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
import math

# Решение для двумерного пространства
# Примеры для проверки:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
# Аналог задачи на C#:
# https://github.com/fredorwell/eductation/blob/main/C%23/Lesson_3/seminar_02/Program.cs


def DistanceTwoPoint2D(xa, ya, xb, yb):
    result = math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)
    return result


x1 = int(input('Первая точка - введите координату x: '))
y1 = int(input('Первая точка - введите координату y: '))
x2 = int(input('Вторая точка - введите координату x: '))
y2 = int(input('Вторая точка - введите координату y: '))
print(f'{round(DistanceTwoPoint2D(x1, y1, x2, y2), 2)}')


# Решение для трехмерного пространства
# Примеры для проверки:
# A (3,6,8); B (2,1,-7), -> 15.84
# A (7,-5, 0); B (1,-1,9) -> 11.53
# Аналог задачи на C#:
# https://github.com/fredorwell/eductation/blob/main/C%23/Lesson_3/seminar_homework_03/homework_task_21/Program.cs


def DistanceTwoPoint3D(xa, ya, za, xb, yb, zb):
    result = math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2 + (za - zb) ** 2)
    return result


x1 = int(input('Первая точка - введите координату x: '))
y1 = int(input('Первая точка - введите координату y: '))
z1 = int(input('Первая точка - введите координату z: '))
x2 = int(input('Вторая точка - введите координату x: '))
y2 = int(input('Вторая точка - введите координату y: '))
z2 = int(input('Вторая точка - введите координату z: '))
print(f'{round(DistanceTwoPoint3D(x1, y1, z1, x2, y2, z2), 2)}')
