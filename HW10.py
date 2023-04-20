from collections import UserDict

dict_of_known_numbers = dict()


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phone = []
        if phone:
            self.phone.append(phone)

    def add_value(self, phone: Phone):
        self.phone.append(phone)
        return "was add"

    def delite(self, delete):
        for i in self.phone:
            if i.value == delete:
                self.phone.remove(i)
                return f"{delete} was deleete from adressbook"
        return f"{delete} not in adres"

    def update(self, changeWhat: Phone, changeTo: Phone):
        for i in range(len(self.phone)):
            if self.phone[i].value == changeWhat:
                self.phone[i].value = changeTo
                return f"{changeWhat} data was change to {changeTo}"
        return f"{changeWhat} data was not change to {changeTo}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
        return f"enter next command"


ad = AddressBook()


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError or ValueError or KeyError:
            return "wrong data. for help input 'help'"
        except AttributeError:
            return "you dont have such name in dict"

    return inner


def show_all(*args):
    for j in ad.values():
        i = [m.value for m in j.phone]
        print(f"{j.name} {i} ")
    return "enter next command"


@input_error
def phone(*args):
    data = args[0].split()
    r = Record(Name(data[0]), Phone(data[1]))
    return ad.add_record(r)


@input_error
def change(*args):
    data = args[0].split()
    r = ad.get(data[0])
    return r.update(data[1], data[2])


def hello(*args):
    return "How can I help you?"


def help(*args):
    return "phone name number - to add number\nchange name number number - to change number\ndell name number - to delete number \nadd name number -to add number to name\nshow all - to see dict\nexit - to exit"


def exit(*args):
    return "bye"


@input_error
def addV(*args):
    data = args[0].split()
    r = ad.get(data[0])
    return r.add_value(Phone(data[1]))


@input_error
def dell(*args):
    data = args[0].split()
    r = ad.get(data[0])
    return r.delite(data[1])


COMANDS = {exit: ("exit", "close", "good bye"),
           help: ("help",),
           change: ("change",),
           show_all: ("show all",),
           phone: ("phone",),
           hello: ("hello",),
           dell: ("dell",),
           addV: ("add",)}


def undefind_comand(*args):
    return "I don`t know this command.Try help"


def input_normilize(data):
    for key, value in COMANDS.items():
        for i in value:
            if not data.find(i):
                comand = i
                return key, data.replace(comand, '').strip()
    return undefind_comand, None


def main():
    while True:
        user_input = input(">>>")
        command, data = input_normilize(user_input)
        print(command(data))
        if command == exit:
            break


if __name__ == "__main__":
    main()
