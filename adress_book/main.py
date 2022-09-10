from datetime import datetime
import pickle
import re
from Class import Record, AdressBook, Iterable
from add_cont_func import add_contact

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            save_data(book)
            with open("data.bin", "rb") as file:
                return pickle.load(file)
    return inner

def close(*_):
    pass 

def save_data(book):
    with open("data.bin", "wb") as file:
        pickle.dump(book, file)

@input_error
def load_data():
    with open("data.bin", "rb") as file:
        return pickle.load(file)

def menu_help():
    help_text = "\nList of commands:\n"
    i = 0
    for help_com in HELP_DICT.values():
        help_text += "".join(f"{i}: {help_com}" + "\n") 
        i += 1
    return help_text



def find_change_contact(book:AdressBook):
    user_input = input("\nEnter the text to find a contact that you want to change: ").strip()
    find_contact = "\n"
    i = 1
    key_list = []
    Iterable(book)
    for _ in book:
        pass

    i = 1
    for value in book:
        key_name, value = value
        if user_input in value:
            find_contact += "".join(f"{i}) {value}") + "\n"
            key_list.append(key_name)
            i += 1

    if find_contact == "\n":
        print("\nCan't find anything.")
    else:
        print(find_contact)

    # user_input = input(">>> 0: To enter the contact menu.\n\nChose number contact to change it: ").strip()
    take_contact()
    # change_contact(book)

def take_contact():
    for i in book:
        a, b = i


def change_contact(book):
    
    user_chose = ""

    while user_chose not in STOP_WORD:
        rec_list_print =  f"Phones: {', '.join(rec.phone)}", f"Email: {', '.join(rec.email)}", f"Adress: {'; '.join(rec.ardess_live)}", \
                            f"Birthday date: {rec.birthday}", f"Notes: {'; '.join(rec.notes)}"
        list_fiel_text = f"\nContact name: {rec.name.value}\n\nAdd to field:\n"
        
        i = 1
        for items in rec_list_print:
            key_name, value = items
            list_fiel_text += f"{i}: {value}\n"
            i += 1

        list_fiel_text += f"\n>>> 0: Exit to main menu\n"

        print(list_fiel_text)

        user_chose = input("Select the field number to fill in: ").strip()
        user_chose = ADD_FUNC_DICT.get(str(user_chose), error_chose)
        user_chose = user_chose(rec)
        print(user_chose)
        book.add_record(rec)

    

def delete_contact(book:AdressBook):
    pass


def main():
    user_input = ""
    while user_input not in STOP_WORD:
        print(menu_help())
        user_input = input("Chose your command number: ").strip()
        command_func = FUNC.get(user_input, close)
        command_func = command_func(book)
        if command_func != None:
            print(command_func)
    book.save_data()
    print('Good bye!')


STOP_WORD = ("0", "stop", "exit", "good bye")

FUNC = {        
        "0" : close,                             # ready
        "1" : add_contact,                        # ready, file add_cont_func.py
        "2" : find_change_contact,                  # 
        "3" : delete_contact,                #                                     
        "4" : find,                              # ready
        "5" : show,                              # ready
        "6" : show_all,                      # ready      
        }   

HELP_DICT = {   
            "close" : "Enter the menu",
            "add_contact" : "Add new contact",                  # add {name} *{phones} {birthday}
            "find_change_contact" : "Change contact",                # change {name} {phone}
            "delete_contact" : "Delete contact",                # delete {name}                   
            "find" : "Find similar",                    # find {text}
            "show" : "Show contact",                    # show {number}
            "show_all" : "Show all contacts",           # show all           
            }   


if __name__ == "__main__":
    book = AdressBook()
    book.load_data()    
    main()


# def parse_date(user_input):
#     date_input = re.findall(r"\d{2}[ /.,\\]\d{2}[ /.,\\]\d{4}", user_input)
#     if len(date_input) > 0:
#         return date_input[-1] 
#     else:
#         return user_input
