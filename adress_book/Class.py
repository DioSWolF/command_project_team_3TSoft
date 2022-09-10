from collections import UserDict
from datetime import datetime
import pickle
import re


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value


class Name(Field):
    pass
class Email(Field):
    pass
class ArdessLive(Field):
    pass
class Notes(Field):
    pass


class Birthday(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value): 
        parse = " .,\/"
        for it in parse:
            value = value.replace(it, ".")
        value = datetime.strptime(value ,"%d.%m.%Y")
        self.__value = value


class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        new_value = re.findall(r"(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}", value)
        for i in new_value:
            new_value = i
        if len(value) >= 9 and len(new_value) > 0:
            self.__value = new_value
        else:
            self.__value = None

class Record:
    def __init__(self, name: Name, phone: Phone = None, email: Email = None, ardess_live: ArdessLive = None, birthday: Birthday = None, notes: Notes = "") -> None:  
            self.name = name
            self.notes = notes

            if phone is None:
                self.phone = ""
            else:
                self.phone = phone

            if email is None:
                self.email = ""
            else:
                self.email = email

            if ardess_live is None:
                self.ardess_live = ""
            else:
                self.ardess_live = ardess_live

            if birthday is None:
                self.birthday = ""
            else:
                self.birthday = birthday
            

class AdressBook(UserDict):

    def add_record(self, rec: Record)-> None:
        self.data[rec.name.value] = rec


    def __iter__(self):
        return Iterable(self.data, number_of_records)
    
    def save_data(self):
        with open("data.bin", "wb") as file:
            pickle.dump(self.data, file)

    def load_data(self):
        try:
            with open("data.bin", "rb") as file:
                self.data = pickle.load(file)
                return self.data 
        except FileNotFoundError:
            with open("data.bin", "wb") as file:
                pickle.dump("", file)
            with open("data.bin", "rb") as file:
                return 

list_index = 0
number_of_records = 0


class Iterable:
    def __init__(self, data, iter_number_of_records = None):
        global number_of_records
        self.current_index = 0
        self.data = data
        self.start_list_index = list_index
        if iter_number_of_records == None:
            number_of_records = len(self.data)
        else:
            number_of_records = iter_number_of_records
        self.iter_number_of_records = number_of_records
        
    def __next__(self):
        global list_index
        if self.current_index <  self.iter_number_of_records:
            self.current_index += 1
            self.start_list_index += 1
            data_key = list(self.data.keys())
            data_value = list(self.data.values())
            try:    
                return data_key[self.start_list_index - 1], f"Name {data_key[self.start_list_index - 1]}, Phones: {', '.join(data_value[self.start_list_index - 1].phone)}; Email: {', '.join(data_value[self.start_list_index - 1].email)}; "\
                    f"Adress: {', '.join(data_value[self.start_list_index - 1].ardess_live)}; Birthday date: {data_value[self.start_list_index - 1].birthday}; Notes: {'; '.join(data_value[self.start_list_index - 1].notes)};"
            except IndexError:
                list_index = 0
                raise StopIteration
        list_index = self.start_list_index
        if list_index >= len(self.data):
            list_index = 0
        raise StopIteration