from ..constants.types import Phonebook


def search_phonebook_by_full_name(phonebook: Phonebook) -> None:
    full_name_to_search = input('Enter a full name to search: ').strip().lower()
    for (first_name, last_name), (phone, city, country) in phonebook.items():
        full_name = f'{first_name} {last_name}'.lower()
        if full_name_to_search in full_name:
            print(f'Found result: {first_name} {last_name} - {phone} {city} {country}')
