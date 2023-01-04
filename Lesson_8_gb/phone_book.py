phone_book = []


def get_phone_book():
    global phone_book
    return phone_book


def set_phone_book(new_pb):
    global phone_book
    phone_book = new_pb


def add_contact(contact: list):
    global phone_book
    phone_book.append(contact)


def remove_contact(id):
    global phone_book
    name = phone_book[id - 1][0]
    confirm = input(f'Вы действительно хотите удалить контакт {name}? (y/n)')
    if confirm.lower() == 'y':
        phone_book.pop(id - 1)
        return True
    return False


def edit_contact(id, upd_contact):
    global phone_book
    phone_book[id - 1] = upd_contact


def search_contact(search_str: str):
    global phone_book
    result = []
    for contact in phone_book:
        if search_str in contact:
            result.append(contact)
    return result
