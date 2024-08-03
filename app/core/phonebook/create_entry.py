from ..constants.types import Phonebook


def create_entry(phonebook: Phonebook) -> None:
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    phone = input('Enter phone: ')
    city = input('Enter city: ')
    country = input('Enter country: ')

    key = (first_name, last_name)
    value = (phone, city, country)
    phonebook[key] = value
