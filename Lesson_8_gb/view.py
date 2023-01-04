def main_menu():
    print('\nВыберите пункт меню:')
    print('1. Показать телефонную книгу')
    print('2. Открыть файл телефонной книги')
    print('3. Сохранить файл телефонной книги')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('0. Выход\n')
    return choice_main_menu()


def choice_main_menu():
    while True:
        try:
            choice = int(input('Выберите команду из меню: '))
            if choice in range(0, 8):
                print()
                return choice
            else:
                print('Такого пункта нет, повторите попытку')
        except:
            print('Ошибка ввода! Некорректные данные')


def print_phone_book(phone_book: list):
    if len(phone_book) > 0:
        for id, contact in enumerate(phone_book, 1):
            print(id, *contact)
    else:
        print('Телефонная книга пуста или не загружена')


def log_off():
    print('До свидания.')


def load_success():
    print('Телефонная книга загружена.')


def save_success():
    print('Телефонная книга сохранена.')


def input_new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий к контакту: ')
    return [name, phone, comment]


def input_remove_contact():
    id = int(input('Введите номер контакта которого хотите удалить: '))
    return id


def remove_success():
    print('Контакт удален!')

def input_edit_contact():
    id = int(input('Введите номер контакта которого хотите изменить: '))
    return id

def update_contact_info(upd_cont: list):
    confirm = input(f'Вы хотите изменить имя контакта {upd_cont[0]}? (y/n)')
    if confirm.lower() == 'y':
        new_name = input(f'Введите новое имя контакта {upd_cont[0]}: ')
        confirm = ''
    else:
        new_name = upd_cont[0]
    confirm = input(f'Вы хотите изменить телефон контакта {upd_cont[0]}? (y/n)')
    if confirm.lower() == 'y':
        new_phone = input(f'Введите новый телефон контакта {upd_cont[0]}: ')
        confirm = ''
    else:
        new_phone = upd_cont[1]
    confirm = input(f'Вы хотите изменить комментарий контакта {upd_cont[0]}? (y/n)')
    if confirm.lower() == 'y':
        new_comm = input(f'Введите новый комментарий контакта {upd_cont[0]}: ')
        confirm = ''
    else:
        new_comm = upd_cont[2]
    return [new_name, new_phone, new_comm]

def input_search():
    search_str = input('Введите строку для поиска: ')
    return search_str

def print_result_search(result_search: list):
    if len(result_search) > 0:
        print('Результаты поиска: \n')
        for id, contact in enumerate(result_search, 1):
            print(id, *contact)
    else:
        print('Данная строка не обнаружена')