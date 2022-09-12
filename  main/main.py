from notes.class_notes import NotesSave
from notes.main_notes import main_by_notes
from typing import Callable, Dict


def adress_book_boat():
    pass

def sorted_boat():
    pass

def notes_boat():
    notes_save = NotesSave()
    notes_save.load_data()
    main_by_notes()

def exit_handler():  
    raise SystemExit('Good bye!')

COMMAND_HANDLERS: Dict[str, Callable] = {
    '0': exit_handler,
    '1': adress_book_boat,
    '2': notes_boat,
    '3': sorted_boat
    }

HELP_DICT = {
    '1': 'menu adress book',
    '2': 'menu notes',
    '3': 'menu sorted'
}

def menu_help():
    help_text = "\nList of commands:\n"
    i = 1
    for help_com in HELP_DICT.values():
        help_text += "".join(f"> {i}) {help_com}" + "\n") 
        i += 1
    return help_text

def parse_user_input(user_input: str):
    command = COMMAND_HANDLERS.get(user_input)
    if command != None:     
        return command()
    raise ValueError('<<<Unknown command>>>')

def main():
    while True:
        print(menu_help())
        user_input = input('>>> 0: Exit to main menu\n\n<< Enter the command: ').strip()
        try:
            resalt = parse_user_input(user_input)
            print(resalt)
        except SystemExit as e:
            print(e)
            break

if __name__ == "__main__":
    main()