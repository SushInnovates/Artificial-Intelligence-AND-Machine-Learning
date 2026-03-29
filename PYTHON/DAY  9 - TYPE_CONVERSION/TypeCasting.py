"""
Topic: Type Casting in Python
Description: Examples of converting one data type into another in Python.
"""

# Example 1: Integer to Float

num = 10
print("Original value:", num)
print("Original type:", type(num))

converted_num = float(num)

print("After typecasting:", converted_num)
print("New type:", type(converted_num))


# Example 2: Float to Integer

price = 99.99
print("\nOriginal value:", price)
print("Original type:", type(price))

int_price = int(price)

print("After typecasting:", int_price)
print("New type:", type(int_price))


# Example 3: String to Integer

num_str = "25"
print("\nOriginal value:", num_str)
print("Original type:", type(num_str))

num_int = int(num_str)

print("After typecasting:", num_int)
print("New type:", type(num_int))


# Example 4: Integer to String

age = 21
print("\nOriginal value:", age)
print("Original type:", type(age))

age_str = str(age)

print("After typecasting:", age_str)
print("New type:", type(age_str))


# Example 5: User Input Typecasting

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

sum_result = num1 + num2

print("Sum of numbers:", sum_result)