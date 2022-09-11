import pickle
from Class import AdressBook, Record
from add_cont_func import add_contact
from show_find_logic import show, show_all, find
from change_cont_func import change_contact
from del_func import delete_func
import datetime

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:

            with open("data.bin", "rb") as file:
                return pickle.load(file)
    return inner

def close(*_):
    return  "\n>>> You chose invalid <<<\n"\
            "    >>>Try again <<<"

def menu_help():
    help_text = "\nList of commands:\n"
    i = 1
    for help_com in HELP_DICT.values():
        help_text += "".join(f"> {i}) {help_com}" + "\n") 
        i += 1
    return help_text

def days_birthday(book, rec: Record):
    now_date = datetime.now()
    date_birthday = datetime(year = now_date.year, month = book[rec.name.value].birthday.value.month, day = book[rec.name.value].birthday.value.day)
    days_birth = date_birthday - now_date
    return rec.days_to_birthday(days_birth.days)

def main():
    user_input = ""
    while user_input not in STOP_WORD:
        print(menu_help())
        user_input = input(">>> 0: To exit in main menu.\n\n<< Chose your command number: ").strip()
        command_func = FUNC.get(user_input, close)
        command_func = command_func(book)
        if command_func != None:
            print(command_func)
    book.save_data()

def close_bot(*_):
    return "\n    <<< Good bye! >>>\n"

STOP_WORD = ("0","stop", "exit", "good bye")

FUNC = {    
        "0" : close_bot,    
        "1" : add_contact,                        
        "2" : change_contact,               
        "3" : delete_func,                                                    
        "4" : find,                             
        "5" : show,                             
        "6" : show_all,                        
        }   

HELP_DICT = {   
            "add_contact" : "Add new contact",                  # add {name} *{phones} {birthday}
            "change_contact" : "Change contact",                # change {name} {phone}
            "delete_func" : "Delete contact",                # delete {name}                   
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