# Python Sets - Key Properties

# 1. Sets do not allow duplicates
# 2. Sets have no indexing or slicing
# 3. Sets do not allow mutable datatypes (like lists) as elements
# 4. Sets themselves are mutable (we can add/remove elements)

# Creating sets
s1 = {}  # This creates an empty dictionary, not a set
print(s1)
print(type(s1))  # <class 'dict'>

s2 = set()  # Correct way to create an empty set
print(s2)
print(type(s2))  # <class 'set'>

# Homogeneous set
s1 = {1, 2, 3, 4, 5}
print(s1)

# Heterogeneous set
s2 = {1, 2, 3.5, 'Hello', True}
print(s2)

# Duplicate elements are removed automatically
s3 = {1, 1, 2, 2, 3, 3, 4, 4}
print(s3)  # Output: {1, 2, 3, 4}

# Sets cannot contain mutable datatypes like lists
# s4 = {[1,2,3], 'Hello'}  #  Error

# Tuples and strings are immutable, so they can be elements of a set
s5 = {(1, 2, 3), 'Hii'}
print(s5)

# Nested sets are not allowed (since sets are mutable)
# s6 = {1, 2, 3, {4, 5}}  #  Error

# Accessing Items

s1 = {1, 2, 3, 4, 5}
# Indexing and slicing are not supported
# print(s1[0])   #  Error
# print(s1[:3])  #  Error

# Editing Items

s1 = {1, 2, 3, 4, 5}
print(s1)
print(id(s1))  # Memory address of set

# Convert to list to edit
L = list(s1)
L[0] = 100
print(L)

# Convert back to set
s1 = set(L)
print(s1)
print(id(s1))  # Different memory address

# Adding Elements

s1 = {1, 2, 3, 4, 5}
s1.add(18)  # Adds a single element
print(s1)

# Deleting Elements

s2 = {1, 2, 3.5, 'Hello', True}
del s2  # Deletes the entire set
# print(s2)  #  Error

s8 = {1, 2, 3.5, 'Hello', True}
s8.remove(3.5)  # Removes specific element
print(s8)

s8.pop()  # Removes an arbitrary element (not truly "last")
print(s8)

# Iteration

s1 = {1, 2, 3, 4, 5}
for i in s1:
    print(i)

# Built-in Functions

s1 = {1, 2, 3, 4, 5}
print(len(s1))              # Number of elements
print(min(s1))              # Minimum value
print(max(s1))              # Maximum value
print(sum(s1))              # Sum of elements
print(sorted(s1))           # Sorted list (ascending)
print(sorted(s1, reverse=True))  # Sorted list (descending)

# Set Operations

s1 = {1, 2, 3, 4, 5, 11}
s2 = {11, 22, 33, 44, 55}

print(s1.union(s2))              # Union of sets (combines)
print(s1.intersection(s2))       # Common elements
print(s1.difference(s2))         # Elements in s1 but not in s2
print(s2.difference(s1))         # Elements in s2 but not in s1
print(s1.symmetric_difference(s2))  # Elements in either set but not both

print(s1.isdisjoint(s2))         # True if no common elements
print(s1.issubset(s2))           # True if s1 is subset of s2
print(s1.issuperset(s2))         # True if s1 is superset of s2

s1.clear()  # Removes all elements
print(s1)

# - Union = everything together
# - Intersection = common things
# - Difference = unique things
# - Symmetric Difference = non-common things
# - isdisjoint = no overlap
# - issubset = fully inside another
# - issuperset = fully contains another
