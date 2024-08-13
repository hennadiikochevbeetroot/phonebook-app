from ..constants.types import Phonebook, PhonebookKey


def delete_entries_by_phone(phonebook: Phonebook) -> None:
    """Deletes all entries which contain entered phone number"""
    phone_to_remove = input('Enter a phone to remove: ').strip()
    keys_to_remove: set[PhonebookKey] = set()
    for key, (phone, _, _) in phonebook.items():
        if phone_to_remove in phone:
            keys_to_remove.add(key)

    for key_to_remove in keys_to_remove:
        del phonebook[key_to_remove]

    print(f'Total deleted with phone {phone_to_remove}: {len(keys_to_remove)}')
