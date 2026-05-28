# -------------------------------
# Dictionary in Python
# -------------------------------

# A dictionary is a mutable data type in Python that stores key-value pairs.
# Keys must be immutable (string, tuple, int, etc.) and unique.
# Values can be mutable (list, dict, set, etc.) or immutable.

# Example dictionary
D1 = {'Name': 'CampusX', 'Gender': 'Male'}
print(D1)

# -------------------------------
# Properties of Dictionary
# -------------------------------
# 1. Dictionary has no indexing like lists or tuples.
# 2. Dictionary is mutable (can be changed).
# 3. Keys must be immutable, values can be mutable.
# 4. Keys should be unique; duplicate keys overwrite previous values.

# Mutable types: list, set, dict
# Immutable types: string, tuple, int, float, bool, complex

# -------------------------------
# Creating Dictionaries
# -------------------------------
D = {}  # Empty dictionary
print(D)
print(type(D))

D1 = {'Name': 'CampusX', 'Gender': 'Male'}
print(D1)

# Invalid example: list as key (lists are mutable, so not allowed)
# D2 = {[1, 2, 3]: "CampusX"}  # ❌ Error

# Valid example: tuple as key (tuples are immutable)
D3 = {(1, 2, 3): "CampusX"}
print(D3)

# Duplicate keys: last value overwrites previous
D4 = {'Name': 'Rahul', 'Name': 'Rohit'}
print(D4)  # Output: {'Name': 'Rohit'}

# Nested dictionary (2D dictionary)
D5 = {'Name': 'Rohit', 'College': 'HIT', 'Marks': {'M1': 45, 'DS': 54, 'ENG': 67}}
print(D5)

# -------------------------------
# Accessing Dictionary Items
# -------------------------------
D1 = {'Name': 'CampusX', 'Gender': 'Male'}
# print(D1[0])  # ❌ Error: dictionaries don’t support index-based access
print(D1['Name'])   # Access using key
print(D1['Gender'])

# Access nested dictionary
print(D5['Marks']['DS'])  # Output: 54

# -------------------------------
# Editing Dictionary
# -------------------------------
D1 = {'Name': 'CampusX', 'Gender': 'Male', 'CGPA': 6}
D1['Name'] = 'Nitish'  # Update value
print(D1)

D1['CGPA'] = 9  # Update another value
print(D1)

# Editing nested dictionary
D5['Marks']['DS'] = 90
print(D5)

# Using get() method (safe access)
print(D1.get('Name'))

# -------------------------------
# Adding New Key-Value Pairs
# -------------------------------
D1['College'] = 'HIT'
print(D1)

D5['Marks']['ML'] = 79  # Add new subject in nested dictionary
print(D5)

# -------------------------------
# Deleting Items
# -------------------------------
D6 = {'Name': 'CampusX', 'Gender': 'Male', 'CGPA': 6}
del D6['Gender']  # Delete specific key
print(D6)

D6.clear()  # Clear entire dictionary (empty dict remains)
print(D6)

# -------------------------------
# Dictionary Operations
# -------------------------------
D1 = {'Name': 'CampusX', 'Gender': 'Male'}
D2 = {'Name': 'Nitish', 'Gender': 'Male'}

# Arithmetic operations like + or * are not supported
# print(D1 + D2)  # ❌ Error
# print(D1 * 4)   # ❌ Error

# Iterating over dictionary
for i in D2:
    print(i)  # Prints keys only

for i in D2:
    print(i, D2[i])  # Prints keys with values

# Membership check
D7 = {'Name': 'CampusX', 'Gender': 'Male', 'CGPA': 6}
print('Rohit' in D7)   # False (checks keys only)
print('Name' in D7)    # True

# Dictionary functions
print(len(D7))          # Number of key-value pairs
print(max(D7))          # Max key (lexicographically)
print(min(D7))          # Min key (lexicographically)
print(sorted(D7))       # Sorted keys
print(sorted(D7, reverse=True))  # Reverse sorted keys

# Getting keys and values
print(D7.keys())    # Returns all keys
print(D7.values())  # Returns all values
