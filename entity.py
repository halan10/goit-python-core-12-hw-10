from collections import UserDict


        
        
class Field:
    def __init__(self, value):
        if not isinstance(value,str):
            raise ValueError("Value must be a string")
        self.value = value
    def __str__ (self)->str:
        return self.value
    
class Name(Field):
    pass

class Phone(Field):
    pass


class Record:
    def __init__(self,name, phone:Phone = None):
        self.name = name
        self.phones = [] 
        if phone:
            self.add_phone(phone)

    def add_phone(self, phone):
        self.phones.append(phone)

    def change_phone(self, index, phone):
        self.phones[index]=phone

    def __repr__(self) -> str:
        return ','.join([p.value for p in self.phones])

class AddressBook(UserDict):
    def add_record(self, record:Record):
        self.data[record.name.value]= record

