from ..constants.cli import POSSIBLE_OPTIONS


def validate_option(user_input: str) -> tuple[bool, int | None]:
    user_input = user_input.strip()
    is_valid = user_input.isdigit() and int(user_input) in POSSIBLE_OPTIONS
    option = int(user_input) if is_valid else None

    return is_valid, option
