from collections import UserDict
import pickle

class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

class Article(Field):
    pass

class TextNotes(Field):
    pass

class KeyWords(Field):
    pass

class Notes():
    def __init__(self, article: Article, text_notes: TextNotes=None, key_words: KeyWords=None) -> None:
        self.article = article
        self.text_notes = text_notes
        self.key_words = key_words

    
class NotesSave(UserDict):
    
    def add_record(self, notes: Notes)-> None:
        self.data[notes.article.value] = notes
        
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




