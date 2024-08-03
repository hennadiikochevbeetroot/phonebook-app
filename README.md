# Phone Book CLI App

### Functionality:
- 0 - An option to exit the program
- 1 - Add new entries
- 9 - Print contents of dictionary

### Features to develop:
- Search by first name 
- Search by last name 
- Search by telephone number 
- Search by city or country 
- Delete a record for a given telephone number 
- Update a record for a given telephone number

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
