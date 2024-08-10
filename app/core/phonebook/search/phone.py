from app.core.constants.types import Phonebook, PhonebookKey, PhonebookValue

from .base import search_base


def search_phonebook_by_phone(phonebook: Phonebook) -> None:
    def criteria_func(key: PhonebookKey, value: PhonebookValue, item_to_search: str) -> bool:
        phone, _, _ = value
        return item_to_search in phone

    prompt = 'Enter a phone number to search: '
    search_base(phonebook, prompt, criteria_func)
