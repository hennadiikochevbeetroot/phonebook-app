from app.core.constants.types import Phonebook, PhonebookKey, PhonebookValue

from .base import search_base


def search_phonebook_by_full_name(phonebook: Phonebook) -> None:
    def criteria_func(key: PhonebookKey, value: PhonebookValue, item_to_search: str) -> bool:
        first_name, last_name = key
        full_name = f'{first_name} {last_name}'
        return item_to_search in full_name.lower()

    # criteria_func = lambda key, value, item_to_search: item_to_search in f'{key[0]} {key[1]}'.lower()

    prompt = 'Enter a full name to search: '
    search_base(phonebook, prompt, criteria_func)
