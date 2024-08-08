from ..constants.types import Phonebook


def search_phonebook_by_phone(phonebook: Phonebook) -> None:
    phone_to_search = input('Enter a phone to search: ')
    for (first_name, last_name), (phone, city, country) in phonebook.items():
        if phone_to_search in phone:
            print(f'Found result: {first_name} {last_name} - {phone} {city} {country}')
