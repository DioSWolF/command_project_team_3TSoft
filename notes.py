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
    
    def write_notes(self, notes: Notes):
        self.data[notes.article.value] 
        
    def save_notes(self, *args):
        with open("notes.bin", "wb") as file:
            pickle.dump(self.data, file)
        return "The notes has been saved"

    def load_notes():
        with open("notes.bin", "rb") as file:
            return pickle.load(file)




