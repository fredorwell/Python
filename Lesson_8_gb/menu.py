import view
import phone_book as pb
import data_base as db


def main_menu(choice: int):
    match choice:
        case 1:
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book)
        case 2:
            db.load_data_base()
            view.load_success()
        case 3:
            db.save_data_base()
            view.save_success()
        case 4:
            contact = view.input_new_contact()
            pb.add_contact(contact)
        case 5:
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book)
            id = view.input_edit_contact()
            update_contact = view.update_contact_info(phone_book[id-1])
            pb.edit_contact(id, update_contact)
        case 6:
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book)
            id = view.input_remove_contact()
            if pb.remove_contact(id):
                view.remove_success()
        case 7:
            search_str = view.input_search()
            result_search = pb.search_contact(search_str)
            view.print_result_search(result_search)

        case 0:
            return True


def start():
    while True:
        choice = view.main_menu()
        if main_menu(choice):
            view.log_off()
            break
