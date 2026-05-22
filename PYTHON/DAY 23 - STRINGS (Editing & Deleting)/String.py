# Editing and Deleting in Strings

# Strings are immutable in Python, meaning we cannot change individual characters.

c = "Hello"
print(c)

# Attempting to modify a character will throw an error:
# c[0] = 'x'  #  'str' object does not support item assignment

print(c)

# We can reassign the entire string, but not modify it in place.
c = "world"
print(c)

# Similarly, we cannot add characters at specific positions:
# c[5] = 'X'  #  Not allowed

# Deletion
print("DELETION:")
d = "python"
del d

# After deletion, trying to access 'd' will cause an error:
# print(d)  #  NameError: name 'd' is not defined
