from typing import Callable

from .exit import exit_program
from .message import print_help_message, print_invalid_message
from .validate import validate_option
from ..constants.types import Phonebook
from ..phonebook.create_entry import create_entry
from ..phonebook.print_phonebook import print_phonebook
from ..phonebook.search_phonebook_by_first_name import search_phonebook_by_first_name

OPTION_TO_FUNCTION: dict[int, Callable[[Phonebook], None]] = {
    1: create_entry,
    2: search_phonebook_by_first_name,
    9: print_phonebook,
}


def cli_app() -> None:
    print_help_message()
    phonebook: Phonebook = {}
    while True:
        user_input = input('Choose an option: ')
        is_valid, option = validate_option(user_input)
        if not is_valid:
            print_invalid_message()
            continue

        if option == 0:
            exit_program()

        OPTION_TO_FUNCTION[option](phonebook)
