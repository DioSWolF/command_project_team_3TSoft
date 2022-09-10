from collections import UserDict
import pickle
from datetime import datetime
class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

class Article(Field):
    pass

class TextNote(Field):
    pass

class KeyWords(Field):
    pass
class DateNote(Field):
    pass

class Notes():
    def __init__(self, article: Article, text_note: TextNote=None, key_words: KeyWords=None, date_note: DateNote=datetime.now()) -> None:
        self.article = article
        self.date_note = date_note
    
        if text_note is None:
            self.text_note = ""
        else:
            self.text_note = text_note

        if key_words is None:
            self.key_words = ""
        else:
            self.key_words = key_words
    
class NotesSave(UserDict):
    
    def add_record(self, notes: Notes)-> None:
        self.data[notes.article.value] = [notes.text_note, notes.key_words]
    
    def __repr__(self, notes: Notes) -> str:
        return f'{notes.article}, {notes.text_note}, {notes.key_words}'
    
    def save_data(self):
        with open("data.bin", "wb") as file:
            pickle.dump(self.data, file)

    def load_data(self):
        try:
            with open("data.bin", "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            with open("data.bin", "wb") as file:
                pickle.dump("", file)
            with open("data.bin", "rb") as file:
                return pickle.load(file)




