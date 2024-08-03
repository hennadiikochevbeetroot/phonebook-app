from .message import print_help_message, print_invalid_message
from .validate import validate_option
from ..types import Phonebook


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
            quit(option)
