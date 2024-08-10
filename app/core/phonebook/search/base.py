from typing import Callable

from app.core.constants.types import Phonebook, PhonebookKey, PhonebookValue


def search_base(phonebook: Phonebook, prompt: str, criteria_func: Callable[[PhonebookKey, PhonebookValue, str], bool]):
    item_to_search = input(prompt).strip().lower()
    for key, value in phonebook.items():
        (first_name, last_name), (phone, city, country) = key, value
        if criteria_func(key, value, item_to_search):
            print(f'Found result: {first_name} {last_name} - {phone} {city} {country}')
