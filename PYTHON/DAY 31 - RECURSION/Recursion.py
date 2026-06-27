# Recursion - 
#           recursion is a function which calls itself

# iterative  vs Recursive a*b
def multiply(a, b):
    result = 0

    for i in range(b):
        result = result + a

    print(result)

multiply(3, 5)

# recursion
def mul(a,b):
    if b == 1:
        return a
    else:
        return a + mul(a,b-1)
    
print(mul(3,4))

# ex 1 - factorial
def fact(number):
    if number == 1:
        return 1
    else:
        return number*fact(number-1)

print(fact(5))

# ex 2 - palindrome
def palindrome(text):
    if len(text) <= 1:
        print("Palindrome")
    else:
        if text[0] == text[-1]:
            palindrome(text[1:-1])
        else:
            print("not palindrome")


palindrome("madam")
palindrome("malayalam")
palindrome("python")

# ex 3 - Rabbit Problem
# not efficient
def fib(month):
    if month == 0 or month == 1 :
        return 1
    else :
        return fib(month - 1) + fib(month - 2)
    

print(fib(12))

# memoization 
import time
def memo(m,d):

    if m in d:
        return d[m]
    else:
        d[m]=memo(m-1,d) + memo(m-2,d)
        return d[m]
    
start = time.time()
d = {0:1,1:1}
print(memo(30,d))
print(time.time()-start)

# problem - from the given list print the power set

def power_set(lst):
    if len(lst) == 0:
        return [[]]

    first = lst[0]
    rest = power_set(lst[1:])

    new_sets = []

    for subset in rest:
        new_sets.append([first] + subset)

    return rest + new_sets


print(power_set([1, 2, 3]))