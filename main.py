from collections import UserDict
from datetime import datetime, date


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value is None or not value:
            raise ValueError(f"Error! There isn't name. Please, enter name!\n")
        else:
            self._value = value


class Phone(Field):
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if len(value) != 10:
            raise ValueError(f" -> Error of length the number phone => {value}")
        elif not value.isdigit():
            raise ValueError(f" -> Error! Phone number must be only numbers => {value}")
        else:
            self._value = value


class Birthday:
    def __init__(self, value):
        self._birthday = None
        self.birthday = value

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        try:
            self._birthday = datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError as e:
            print(e)

    def __str__(self):
        return str(self.birthday)


class Record:
    def __init__(self, name: str = None, birthday: str = None):
        try:
            self.name = Name(name)
        except ValueError as e:
            print(e)

        self.phones = []

        if birthday:
            self.birthday = Birthday(birthday)
        else:
            self.birthday = ''

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
        except ValueError as e:
            print(e)

    def remove_phone(self, phone):
        for number in self.phones:
            if str(number) == phone:
                self.phones.remove(number)

    def edit_phone(self, *args, **kwargs):
        if args[0] in (p.value for p in self.phones):
            try:
                for number in self.phones:
                    if str(number) == args[0]:
                        ind = self.phones.index(number)
                        self.phones[ind] = Phone(args[1])
            except ValueError as e:
                print(e)
        else:
            raise ValueError

    def find_phone(self, phone):
        try:
            for number in self.phones:
                if str(number) == str(Phone(phone)):
                    return number
        except ValueError as e:
            print(e)

    def days_to_birthday(self):
        if self.birthday:
            today_data = date.today()
            birthday = datetime.strptime(str(self.birthday), '%Y-%m-%d').date()
            birthday_now = birthday.replace(year=today_data.year)

            if today_data <= birthday_now:
                delta = birthday_now - today_data
            else:
                birthday_now = birthday.replace(year=today_data.year + 1)
                delta = birthday_now - today_data
            return delta.days


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"



class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, find_name):
        if self.data.get(find_name):
            our_name = self.data.get(find_name)
            return our_name
        else:
            return None

    def delete(self, name):
        if name in self.data.keys():
            del self.data[name]
        else:
            print(f"=>Name {name} isn't exists")

    def iterator(self, len_list):
        list_book = []
        start_ind = 0
        for name, value in self.data.items():
            list_book.append(f"{name}: {value}")

        while True:
            my_list = list_book[start_ind:len_list]
            start_ind = len_list
            len_list += len_list
            yield my_list
            StopIteration




