from ..constants.types import Phonebook


def search_phonebook_by_first_name(phonebook: Phonebook) -> None:
    first_name_to_search = input('Enter a first name to search: ').strip().lower()
    for (first_name, last_name), (phone, city, country) in phonebook.items():
        if first_name_to_search in first_name.lower():
            print(f'Found result: {first_name} {last_name} - {phone} {city} {country}')
