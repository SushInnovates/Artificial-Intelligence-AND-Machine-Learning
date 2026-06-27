# Recursion in Python - 
#                       Recursion is a technique where a function calls itself.
#                       It is often used to solve problems that can be broken down
# into smaller, similar subproblems.

# Iterative vs Recursive Multiplication

def multiply(a, b):
    """Multiply two numbers using iteration."""
    result = 0
    for i in range(b):
        result += a
    print(result)

multiply(3, 5)  # Output: 15


def mul(a, b):
    """Multiply two numbers using recursion."""
    if b == 1:
        return a
    else:
        return a + mul(a, b - 1)

print(mul(3, 4))  # Output: 12


# Example 1: Factorial

def fact(number):
    """Return factorial of a number using recursion."""
    if number == 1:
        return 1
    else:
        return number * fact(number - 1)

print(fact(5))  # Output: 120


# Example 2: Palindrome Check

def palindrome(text):
    """Check if a string is palindrome using recursion."""
    if len(text) <= 1:
        print("Palindrome")
    else:
        if text[0] == text[-1]:
            palindrome(text[1:-1])
        else:
            print("Not Palindrome")

palindrome("madam")       # Palindrome
palindrome("malayalam")   # Palindrome
palindrome("python")      # Not Palindrome


# Example 3: Fibonacci (Rabbit Problem)

def fib(month):
    """Return nth Fibonacci number using recursion (inefficient)."""
    if month == 0 or month == 1:
        return 1
    else:
        return fib(month - 1) + fib(month - 2)

print(fib(12))  # Output: 233


# Memoization for Fibonacci

import time

def memo(m, d):
    """Fibonacci with memoization for efficiency."""
    if m in d:
        return d[m]
    else:
        d[m] = memo(m - 1, d) + memo(m - 2, d)
        return d[m]

start = time.time()
d = {0: 1, 1: 1}
print(memo(30, d))            # Output: 1346269
print("Time taken:", time.time() - start)


# Example 4: Power Set

def power_set(lst):
    """Return the power set of a list using recursion."""
    if len(lst) == 0:
        return [[]]

    first = lst[0]
    rest = power_set(lst[1:])

    new_sets = []
    for subset in rest:
        new_sets.append([first] + subset)

    return rest + new_sets

print(power_set([1, 2, 3]))
# Output: [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
