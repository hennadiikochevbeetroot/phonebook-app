from typing import Callable

from .exit import exit_program
from .message import print_help_message, print_invalid_message
from .validate import validate_option
from ..constants.cli import PHONEBOOK_TEST_DATA
from ..constants.types import Phonebook
from ..phonebook.create_entry import create_entry
from ..phonebook.delete_entries_by_phone import delete_entries_by_phone
from ..phonebook.print_phonebook import print_phonebook
from ..phonebook.search.first_name import search_phonebook_by_first_name
from ..phonebook.search.full_name import search_phonebook_by_full_name
from ..phonebook.search.last_name import search_phonebook_by_last_name
from ..phonebook.search.phone import search_phonebook_by_phone
from ..phonebook.search.location import search_phonebook_by_location
from ..phonebook.update_name_by_phone import update_name_by_phone

OPTION_TO_FUNCTION: dict[int, Callable[[Phonebook], None]] = {
    1: create_entry,
    2: search_phonebook_by_first_name,
    3: search_phonebook_by_last_name,
    4: search_phonebook_by_full_name,
    5: search_phonebook_by_phone,
    6: search_phonebook_by_location,
    7: update_name_by_phone,
    8: delete_entries_by_phone,
    9: print_phonebook,
}


def cli_app() -> None:
    print_help_message()
    phonebook: Phonebook = {**PHONEBOOK_TEST_DATA}
    while True:
        user_input = input('Choose an option: ')
        is_valid, option = validate_option(user_input)
        if not is_valid:
            print_invalid_message()
            continue

        if option == 0:
            exit_program()

        OPTION_TO_FUNCTION[option](phonebook)
