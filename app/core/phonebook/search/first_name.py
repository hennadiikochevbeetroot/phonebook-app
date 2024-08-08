from app.core.constants.types import Phonebook, PhonebookKey, PhonebookValue

from .base import search_base


def search_phonebook_by_first_name(phonebook: Phonebook) -> None:
    def criteria_func(key: PhonebookKey, value: PhonebookValue, item_to_search: str) -> bool:
        first_name, last_name = key
        return item_to_search in first_name.lower()

    prompt = 'Enter a first name to search: '
    search_base(phonebook, prompt, criteria_func)
