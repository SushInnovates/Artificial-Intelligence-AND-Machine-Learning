"""
Topic: Operators in Python
Day: 11
Description: Examples of different types of operators in Python.
Learning Source: CampusX Python Playlist
"""

""" 
Types of Operators
 1. Arithmetic Operators
 2. Comparison Operators
 3. Logical Operators
 4. Assignment Operators
 5. Bitwise Operators
 6. Membership Operators
 7. Identity Operators

"""
 


# 1. Arithmetic Operators

a = 10
b = 3

print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)


# 2. Comparison Operators

print("\nComparison Operators:")
print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)
print("a != b:", a != b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


# 3. Logical Operators

x = True
y = False

print("\nLogical Operators:")
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)


# 4. Assignment Operators

num = 5

num += 2
print("\nAssignment Operators (+=):", num)

num -= 1
print("Assignment Operators (-=):", num)

num *= 3
print("Assignment Operators (*=):", num)

num /= 2
print("Assignment Operators (/=):", num)


# 5. Bitwise Operators

p = 5
q = 3

print("\nBitwise Operators:")
print("p & q:", p & q)
print("p | q:", p | q)
print("p ^ q:", p ^ q)
print("~p:", ~p)
print("p << 1:", p << 1)
print("p >> 1:", p >> 1)


# 6. Membership Operators

text = "Python Programming"

print("\nMembership Operators:")
print("'Python' in text:", "Python" in text)
print("'Java' not in text:", "Java" not in text)


# 7. Identity Operators

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("\nIdentity Operators:")
print("a is b:", a is b)
print("a is c:", a is c)
print("a is not c:", a is not c)