from src.local_storage import contacts_storage


def hello():
    return 'How can I help you?'


def add_contact(args):
    try:
        name, phone = args
    except ValueError:
        return 'You need to provide name and phone arguments'

    if name in contacts_storage:
        return 'Contact already exists.'

    contacts_storage[name] = phone
    return 'Contact added.'


def change_contact(args):
    try:
        name, phone = args
    except ValueError:
        return 'You need to provide name and phone arguments'

    if name not in contacts_storage:
        return 'Contact doesn`t exist.'

    contacts_storage[name] = phone
    return 'Contact changed.'


def show_phone(args):
    try:
        name = args[0]
    except ValueError:
        return 'You need to provide name argument'

    if name not in contacts_storage:
        return 'Contact doesn`t exist.'

    return contacts_storage[name]


def show_all():
    return '\n'.join([f'{name} - {phone}' for name, phone in contacts_storage.items()])


def close():
    return 'Good bye!'


def invalid_command():
    return 'Invalid command.'
