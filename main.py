from typing import Callable, Dict
from notes import Article, TextNotes, KeyWords, Notes, NotesSave



def exit_handler():  
    raise SystemExit('Good bye!')

def add_new_note():
    pass

def note_change_time():
    pass

def editing_note():
    pass

def sorting_notes():
    pass

def delete_note():
    pass

def find_by_article():
    name = input('\nEnter the name: ')
    notes_list = []
    for note in notes_save.data:
        if name in note:
            notes_list.append(note)
    return f'\n{notes_list}'

def finde_by_keywords():
    pass

COMMAND_HANDLERS: Dict[str, Callable] = {
    '0': exit_handler,
    '1': add_new_note,
    '2': note_change_time,
    '3': editing_note,
    '4': sorting_notes,
    '5': delete_note,
    '6': find_by_article,
    '7': finde_by_keywords
    }

HELP_DICT = {
    '0': 'exit',
    '1': 'add new note',
    '2': 'note change time',
    '3': 'editing note',
    '4': 'sorting notes',
    '5': 'delete note',
    '6': 'find by article',
    '7': 'finde by keywords'
}

def menu_help():
    help_text = "\nList of commands:\n\n"
    i = 0
    for help_com in HELP_DICT.values():
        help_text += "".join(f"{i}: {help_com}" + "\n") 
        i += 1
    return help_text


def parse_user_input(user_input: str):
    command = COMMAND_HANDLERS.get(user_input)
    if command != None:     
        return command()
    raise ValueError('Unknown command')

def main():
    # user_article = "Homework"
    # user_text = "qweqweqwe das dasd qw"
    # user_keys = ["qweqwe", "qweqwe"]

    # article = Article(user_article).value
    # textnotes = TextNotes(user_text).value
    # key_words = [KeyWords(words).value for words in user_keys] 

    # notes = Notes(article, textnotes, key_words)
    while True:
        print(menu_help())
        user_input = input('Enter the command: ').lower()
        try:
            resalt = parse_user_input(user_input)
            print(resalt)
        except SystemExit as e:
            print(e)
            break


if __name__ == "__main__":
    notes_save = NotesSave()
    main()
