from typing import Callable, Dict
from notes import Article, TextNote, KeyWords, Notes, NotesSave


def add_new_note():
    article = input("\n>>> 0: Exit to main menu\n\nWrite article note: ").strip()

    if article == "0":
        return
    
    if article in notes_save.data:
        return "\nYou have a note with this article! Choose another articl."

    article = Article(article)

    text_note = TextNote("")
    key_words = [KeyWords('')]
    note = Notes(article, text_note, key_words)
    notes_save.add_record(note)
    return write_in_field(notes_save, note)

def write_in_field(notes_save: NotesSave, note : Notes):
    user_chose = ""

    while user_chose != '0':
        rec_list_print =  f"Article: {note.article.value}", f"text_notes: {note.text_note.value}", f"Key words: {(', ').join([i.value for i in note.key_words][0])}"
        list_fiel_text = f"\nArticle: {note.article.value}\n\nAdd to note:\n"
        
        i = 1
        for items in rec_list_print:
            list_fiel_text += f"{i}: {items}\n"
            i += 1

        list_fiel_text += f"\n>>> 0: Exit to main menu\n 1: write text notes field\n 2: write kye words field\n"

        print(list_fiel_text)
        
        user_chose = input("Select the field number to fill in: ").strip()
        user_chose = ADD_FUNC_DICT.get(str(user_chose), error_chose)
        user_chose = user_chose(note)
        print(user_chose)
        notes_save.add_record(note)

def write_kye_words_field(note: Notes) -> None:
    user_input = input("\n>>> 0: To enter the notes menu.\n\nWrite keywords with a space: ").split(' ')

    if user_input == "0":
        return

    note.key_words = [KeyWords(user_input)]


def write_text_notes_field(note: Notes) -> None:
    user_input = input("\n>>> 0: To enter the notes menu.\nʼтWrite text notes: ").strip()

    if user_input == "0":
        return

    note.text_note = TextNote(user_input)

def error_chose(*_):
    return "\n<<<You chose invalid. Try again>>>"

def close_bot(*_):
    return "0"

ADD_FUNC_DICT = {   "0" : close_bot, 
                    "1" : write_text_notes_field,
                    "2" : write_kye_words_field,
                }


def exit_handler():  
    raise SystemExit('Good bye!')

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
            notes_save.save_data()
            break



if __name__ == "__main__":
    notes_save = NotesSave()
    notes_save.load_data()
    main()
