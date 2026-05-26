# Tuples in Python
# ----------------
# Tuples are Immutable Data Structures (cannot be changed after creation).
# They can store heterogeneous data types and support indexing, slicing, and operations.

# Create Tuples

T1 = ()  
print(T1)  # Output: ()

T2 = (1, 2, 3, 4)
print(T2)  # Output: (1, 2, 3, 4)  # Homogeneous tuple

T3 = (1, 2, 3.5, 'hello', True)
print(T3)  # Output: (1, 2, 3.5, 'hello', True)  # Heterogeneous tuple

T4 = (1, 2, 43, (4, 5))
print(T4)  # Output: (1, 2, 43, (4, 5))  # Nested tuple (2D)

T5 = ((1, 3), (4, 5, (7, 8)))
print(T5)  # Output: ((1, 3), (4, 5, (7, 8)))

print(type(T5))  # Output: <class 'tuple'>

T7 = tuple("Hello")
print(T7)  # Output: ('H', 'e', 'l', 'l', 'o')
print(type(T7))  # Output: <class 'tuple'>

# Creating tuple from a list
T8 = tuple([1, 2, 3, 4])
print(T8)  # Output: (1, 2, 3, 4)

# Access Elements

T2 = (1, 2, 3, 4)
print(T2[0])     # Output: 1 (first element)
print(T2[-1])    # Output: 4 (last element)
print(T2[::-1])  # Output: (4, 3, 2, 1) (reversed tuple)
print(T2[:3])    # Output: (1, 2, 3) (slicing)

T4 = (1, 2, 43, (4, 5))
print(T4[-1][0])  # Output: 4 (accessing nested tuple element)

# Edit Elements

L = [1, 2, 3, 4, 5]
L[0] = 100
print(L)  # Output: [100, 2, 3, 4, 5] (lists are mutable)

# Tuples are immutable, so editing is not possible:
T2 = (1, 2, 3, 4)
# T2[0] = 100  # This will raise a TypeError

# Delete Tuples

print(T1)  # Output: ()
del T1
# print(T1)  #  This will raise a NameError (T1 is deleted)

# del T2[-1]  #  Not possible, tuples are immutable

# Tuple Operations

T2 = (1, 2, 3, 4, 5)
T3 = (6, 7, 8, 9, 10)

print(T2 + T3)  # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) (concatenation)
print(T2 * 3)   # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5) (repetition)

for i in T2:
    print(i)  # Prints each element of T2

print(1 in T2)  # Output: True (membership check)

# Tuple Functions

print(len(T2))               # Output: 5 (length of tuple)
print(min(T2))               # Output: 1 (minimum element)
print(max(T2))               # Output: 5 (maximum element)
print(sorted(T2))            # Output: [1, 2, 3, 4, 5] (sorted list)
print(sorted(T2, reverse=True))  # Output: [5, 4, 3, 2, 1] (descending order)

# Note:
# Tuples are read-only data types in Python.
# They are useful when you want to store fixed collections of items.
