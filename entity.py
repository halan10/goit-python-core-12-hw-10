from collections import UserDict


        
        
class Field:
    def __init__(self, value):
        if not isinstance(value,str):
            raise ValueError("Value must be a string")
        self.value = value
    def __str__ (self)->str:
        return self.value


class Record:
    def __init__(self,name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def change_phone(self, index, phone):
        self.phones[index]=phone

class AddressBook(UserDict):
    def add_record(self, record:Record):
        self.data[record.name.value]= record

class Name(Field):
    pass

class Phone(Field):
    pass
