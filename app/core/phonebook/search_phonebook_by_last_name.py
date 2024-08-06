from ..constants.types import Phonebook


def search_phonebook_by_last_name(phonebook: Phonebook) -> None:
    last_name_to_search = input('Enter a last name to search: ').strip().lower()
    for (first_name, last_name), (phone, city, country) in phonebook.items():
        if last_name_to_search in last_name.lower():
            print(f'Found result: {first_name} {last_name} - {phone} {city} {country}')
