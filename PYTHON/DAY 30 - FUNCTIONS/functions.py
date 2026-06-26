# what is function?
# it is a block of code which is used to perform a specific task for perticular task
# "It is a block of code which is used to perform a specific task"
#   syntax :  
# #             def is_even(i):
#  where def : which is  a python keyword which is used to create a function
#        is_even : is a function name ,function name can be anything
#         i : is a parameter



# creating a function

# def is_Even(number):
#     """
#     this function tell if the given number is even or odd
#     input - any valid number
#     output - odd/even
#     Created by - CampusX
#     Last Edited - 21 june 2026
#     """
#      if type(number) == int:
#           if number % 2 == 0:
#                 return 'Even'
#           else:
#                 return 'Odd'
        # else: 
        #     return 'Not Allowed'
# import EvenOdd

# when we want to import the created function 
# we can do that by 2 ways 
# 1 > create a function and save the file , save the file in same directory and u can import that function like import function Name
# 2 > create a function and copy the function file inside the pythons library folder and u can import the function



# for i in range(1,11):
    # print(EvenOdd.is_Even(i))

# to get the documentation of the function
# print(EvenOdd.is_Even.__doc__)


def flex(*number):
    product = 1
    for i in number:
        product = product * i
    print(product)

flex(1,2,3,4,5,6,7)
# we had used *number coz it takes as multiple input as a tuple

def func_a():
    print('inside func_a')

def func_b(y):
    print('inside func_b')
    return y

def func_c(z):
    print('inside func_c')
    return z()

print(func_a())
print(5+func_b(2))
print(func_c(func_a))

# ex 1 
print("Example 1")
def f(y):
    x = 1
    x += 1
    print(x)
x = 5
f(x)
print(x)

# ex 2
print("Example 2")
def g(y):
    print(x)
    print(x+1)

x = 5
g(x)
print(x)

# ex 3
def f(x):
    x = x + 1
    print('in f(x) : x = ',x)
    return x

x = 3
z = f(x)
print('in main program scope : z = ',z)
print('in main program scope : x = ',x)

# nested function
def g():
    print("Inside g")
    def h():
        print('inside g')
        f()

g() 


# ex 4
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x) : x =',x)
    h()
    return x

x = 3
z = g(x)

# functions as object
def f(num):
    return num**2

f(3)

x = f
print(x)

L = [1,2,3,4,x(5)]
print(L)