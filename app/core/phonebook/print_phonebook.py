from ..constants.types import Phonebook


def print_phonebook(phonebook: Phonebook) -> None:
    for (first_name, last_name), (phone, city, country) in phonebook.items():
        print(f'Fullname: {first_name} {last_name}; Place: {city} {country}; Phone {phone}')
