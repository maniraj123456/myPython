"""This module contains a dictionary of programs and their corresponding functions."""

#emptyDict = {}   creating an empty dictionary

dict1 = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
}  # creating a dictionary with some key-value pairs
print(dict1.get("name"))  # accessing the value associated with the key "name"
print(dict1["name"])  # accessing the value associated with the key "name"

print(dict1.get("country"))  # accessing the value associated with the key "country"
# print(dict1["country"])   accessing the value associated with the key "country"
# The above line will raise a KeyError because the key 'country' does not exist in the dictionary.
