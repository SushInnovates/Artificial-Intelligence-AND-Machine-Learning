# Functions in Python - 
#                         A function is a block of code used to perform a specific task.
# Syntax:
#     def function_name(parameters):
#         # function body
#
# Example:
# def is_even(i):
#     # 'def' is a Python keyword used to define a function
#     # 'is_even' is the function name (can be anything)
#     # 'i' is a parameter
#     pass

# Example: Even/Odd Function

def is_Even(number):
    """
    This function tells if the given number is even or odd.
    Input  - any valid integer
    Output - 'Odd' or 'Even'
    Created by - CampusX
    Last Edited - 21 June 2026
    """
    if type(number) == int:
        if number % 2 == 0:
            return 'Even'
        else:
            return 'Odd'
    else:
        return 'Not Allowed'


# Importing Functions

# 1. Save the function in a file in the same directory and import it:
#       import filename
# 2. Copy the function file inside Python’s library folder and import it globally.

# Example usage:
# import EvenOdd
# for i in range(1, 11):
#     print(EvenOdd.is_Even(i))
# print(EvenOdd.is_Even.__doc__)


# Example: Function with *args

def flex(*number):
    """Takes multiple inputs and returns their product."""
    product = 1
    for i in number:
        product *= i
    print(product)

flex(1, 2, 3, 4, 5, 6, 7)  # Output: 5040


# Functions as Parameters

def func_a():
    print('inside func_a')

def func_b(y):
    print('inside func_b')
    return y

def func_c(z):
    print('inside func_c')
    return z()

print(func_a())             # Calls func_a
print(5 + func_b(2))        # Calls func_b
print(func_c(func_a))       # Passes func_a as argument


# Scope Examples

print("Example 1")
def f(y):
    x = 1
    x += 1
    print(x)

x = 5
f(x)        # Prints 2
print(x)    # Prints 5 (global x unchanged)

print("Example 2")
def g(y):
    print(x)
    print(x + 1)

x = 5
g(x)        # Prints 5 and 6
print(x)    # Prints 5


print("Example 3")
def f(x):
    x = x + 1
    print('in f(x): x =', x)
    return x

x = 3
z = f(x)
print('in main scope: z =', z)  # Prints 4
print('in main scope: x =', x)  # Prints 3


# Nested Functions

def g():
    print("Inside g")
    def h():
        print('inside h')
    h()

g()


print("Example 4")
def g(x):
    def h():
        x = 'abc'  # local to h
    x = x + 1
    print('in g(x): x =', x)
    h()
    return x

x = 3
z = g(x)


# Functions as Objects

def f(num):
    return num ** 2

print(f(3))   # Prints 9

x = f         # Assign function to variable
print(x)      # Prints function object reference

L = [1, 2, 3, 4, x(5)]  # Calls f(5) → 25
print(L)     # Prints [1, 2, 3, 4, 25]
