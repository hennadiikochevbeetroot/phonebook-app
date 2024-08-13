HELP_MESSAGE = """
Welcome to PhoneBook.
Options:
0. An option to exit the program
1. Add new entries
2. Search by first name
3. Search by last name
4. Search by full name
5. Search by phone
6. Search by location (city of country)
7. Update name by phone
8. Delete record by phone
9. Print contents of phonebook
"""
POSSIBLE_OPTIONS = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

PHONEBOOK_TEST_DATA = {
    ('Ann', 'Smith'): ('+1232442', 'Boston', 'US'),
    ('Jack', 'Smoggs'): ('+12244434', 'London', 'UK'),
    ('Julie', 'Roth'): ('+124748444', 'Oslo', 'Norway'),
}
