from app.core.constants.types import Phonebook, PhonebookKey, PhonebookValue

from .base import search_base


def search_phonebook_by_location(phonebook: Phonebook) -> None:
    def criteria_func(key: PhonebookKey, value: PhonebookValue, item_to_search: str) -> bool:
        _, city, country = value
        return item_to_search in city.lower() or item_to_search in country.lower()

    prompt = 'Enter a location (city or country) to search: '
    search_base(phonebook, prompt, criteria_func)
