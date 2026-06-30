"""
Lambda Functions, Higher Order Functions, Map, Filter, Reduce,
List Comprehension, and Dictionary Comprehension in Python
"""

# -------------------------------
# Lambda Function (Anonymous Function)
# -------------------------------
# Syntax: lambda arguments: expression
# Lambda functions are small, one-line functions without a name.
# They are often used with higher-order functions like map, filter, and reduce.

# Example: Square of a number
square = lambda x: x**2
print(square(9))  # Output: 81

# Example: Addition of two numbers
add = lambda c, d: c + d
print(add(10, 5))  # Output: 15

# Example: Check if input starts with letter 'a'
starts_with_a = lambda x: x[0] == 'a'
print(starts_with_a("apple"))   # True
print(starts_with_a("mapple"))  # False

# Example: Check if number is even or odd
even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even_or_odd(23))  # Output: Odd


# -------------------------------
# Higher Order Function
# -------------------------------
# A higher-order function takes another function as an argument.

def return_sum(func, L):
    """Return the sum of elements in L that satisfy the condition in func."""
    result = 0
    for i in L:
        if func(i):
            result += i
    return result

L = [11, 14, 21, 23, 56, 78, 45, 29, 28]
even = lambda l: l % 2 == 0
odd = lambda l: l % 2 != 0
div_by_3 = lambda l: l % 3 == 0

print(return_sum(even, L))     # Sum of even numbers
print(return_sum(odd, L))      # Sum of odd numbers
print(return_sum(div_by_3, L)) # Sum of numbers divisible by 3


# -------------------------------
# Map Function
# -------------------------------
# Map applies a function to each element of a list.

L = [10, 20, 30, 40, 50, 81]
M = map(lambda x: x * 2, L)
print(list(M))  # Doubled values

print(list(map(lambda x: x % 2 == 0, L)))  # Check even numbers


# Example: Extract names from student data
students = [
    {"name": 'jacob martin', "fathers name": 'Ros Martin', "Address": "123 hill street"},
    {"name": 'angela stevens', "fathers name": 'Robert stevens', "Address": "3 upper street"},
    {"name": 'ricky smart', "fathers name": 'william smart', "Address": "unknown"}
]

names = map(lambda x: x['name'], students)
print(list(names))


# -------------------------------
# Filter Function
# -------------------------------
# Filter extracts elements from a list based on a condition.

L = [1, 2, 3, 4, 5, 6, 7]
print(list(filter(lambda x: x > 4, L)))  # Numbers greater than 4

fruits = ['mango', 'watermelon', 'guava', 'banana', 'Orange']
filtered_fruits = filter(lambda fruit: 'e' in fruit, fruits)
print(list(filtered_fruits))  # Fruits containing 'e'


# -------------------------------
# Reduce Function
# -------------------------------
# Reduce applies a function cumulatively to elements of a list.

import functools

L = [1, 2, 3, 4, 5, 6, 7]
total_sum = functools.reduce(lambda x, y: x + y, L)
print(total_sum)  # Sum of all elements

# Largest number
L1 = [12, 34, 65, 78, 98, 45]
largest = functools.reduce(lambda x, y: x if x > y else y, L1)
print(largest)

# Smallest number
L2 = [12, 34, 123, 5, 63, 6, 73]
smallest = functools.reduce(lambda x, y: x if x < y else y, L2)
print(smallest)


# -------------------------------
# List Comprehension
# -------------------------------
# Compact way to create lists.

L3 = [item * 2 for item in L1]
print(L3)

L4 = [i ** 2 for i in range(10)]
print(L4)

L5 = [i ** 2 for i in range(10) if i % 2 != 0]
print(L5)

L6 = [fruit for fruit in fruits if fruit[0] == 'O']
print(L6)


# -------------------------------
# Dictionary Comprehension
# -------------------------------
# Compact way to create dictionaries.

D = {'Name': 'Nitish', 'Gender': 'Male', 'Age': 24}
print(D.items())

D1 = {key: value for key, value in D.items() if len(key) > 3}
print(D1)

List = [1, 2, 3, 4, 5, 6, 7]
D2 = {item: item ** 2 for item in List}
print(D2)

# Corrected version: filter odd numbers and square them
D3 = {item: item ** 2 for item in List if item % 2 != 0}
print(D3)
