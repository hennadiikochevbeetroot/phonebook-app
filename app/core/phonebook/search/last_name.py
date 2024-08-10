from app.core.constants.types import Phonebook, PhonebookKey, PhonebookValue

from .base import search_base


def search_phonebook_by_last_name(phonebook: Phonebook) -> None:
    def criteria_func(key: PhonebookKey, value: PhonebookValue, item_to_search: str) -> bool:
        _, last_name = key
        return item_to_search in last_name.lower()

    prompt = 'Enter a last name to search: '
    search_base(phonebook, prompt, criteria_func)
