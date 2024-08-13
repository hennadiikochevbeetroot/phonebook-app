from ..constants.types import Phonebook


def update_name_by_phone(phonebook: Phonebook) -> None:
    """Updates one record with entered phone"""
    phone_to_update = input('Enter a phone to modify: ').strip()
    first_name_to_update = input('Enter first name: ').strip()
    last_name_to_update = input('Enter last name: ').strip()
    for (first_name, last_name), (phone, _, _) in phonebook.items():
        if phone_to_update in phone:
            new_key = (first_name_to_update, last_name_to_update)
            phonebook[new_key] = phonebook.pop((first_name, last_name))
            return
