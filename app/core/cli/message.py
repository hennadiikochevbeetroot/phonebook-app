from ..constants.cli import HELP_MESSAGE, POSSIBLE_OPTIONS


def print_help_message():
    print(HELP_MESSAGE)


def print_invalid_message():
    possible_options = ', '.join([str(option) for option in POSSIBLE_OPTIONS])
    print(f'Incorrect option, possible are: {possible_options}')
