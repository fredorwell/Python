# Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).

def CoordinateQuart(num):
    match num:
        case 1:
            print('В первой четверти - x > 0 y > 0')
        case 2:
            print('Во второй четверти - x < 0 y > 0')
        case 3:
            print('В третьей четверти - x < 0 y < 0')
        case 4:
            print('В четвертой четверти - x > 0 y < 0')
        case _:
            print(f'{num}-й четверти не существует')


num_quart = int(input('Введите номер четверти: '))
CoordinateQuart(num_quart)



