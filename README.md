# Phone Book CLI App

### Functionality:
- 0 - An option to exit the program
- 1 - Add new entries
- 2 - Search by first name
- 3 - Search by last name
- 4 - Search by full name
- 5 - Search by phone number
- 6 - Search by location
- 7 - Update name by phone number
- 8 - Delete record by phone number
- 9 - Print contents of dictionary

### Key points:
1. all program logic should be split to different functions;
2. store all entries in the dict, where
3. key is the full name (tuple with length 2 - first name, last name)
and value another tuple with (all other data):
```python
{
    ('John', 'Smith'): ('+12423535', 'Minnesota', 'US')
}
```
