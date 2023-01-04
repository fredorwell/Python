def input_number() -> int:
    while True:
        try:
            numbers = int(input('Введите число: '))
            return numbers
        except:
            print('Ошибка')


def input_operation():
    while True:
        operation = input('Введите операцию: ')
        if operation in ['+', '-', '*', '/', '=']:
            return operation
        else:
            print('Введите конкретную операцию')


def print_to_console(value_text):
    print(value_text)


def log_off():
    print('До свидания!')


def print_division_by_zero():
    print('На ноль делить нельзя!')
