from ..constants.types import Phonebook


def create_entry(phonebook: Phonebook) -> None:
    first_name = input('Enter first name: ').strip()
    last_name = input('Enter last name: ').strip()
    phone = input('Enter phone: ').strip()
    city = input('Enter city: ').strip()
    country = input('Enter country: ').strip()

    key = (first_name, last_name)
    value = (phone, city, country)
    phonebook[key] = value
