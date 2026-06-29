# Lambda Function - 
#     it is also known as anonymous function

# creating lambda function
# syntax : lambda input: expression

# square of  number
x = lambda x:x**2
print(x(9))

# addition of  number
y = lambda c,d:c+d
print(y(10,5))

# difference between normal function and lambda function
# 1 > lambda has no return Value
# 2 > type(y) - function
# 3 > one line
# 4 > not used for code reusability
# 5 > no name

# why should we use lambda function
# along with higher order function

# check if the input starts with letter 'a'
b =lambda x:x[0]=='a'
print(b("apple"))
print(b("mapple"))

# check if the number is even or odd
c = lambda x:"Even" if x%2==0 else "odd"
print(c(23))


# Higher order function

def return_sum(func,L):
    result  = 0
    for i in L:
        if func(i):
            result = result + i
    
    return result


L = [11,14,21,23,56,78,45,29,28]
even = lambda l:l%2==0
odd = lambda l:l%2!=0
DivBy3 = lambda l:l%3==0
print(return_sum(even,L))
print(return_sum(odd,L))
print(return_sum(DivBy3,L))

# map
L = [10,20,30,40,50,81]
# if we want to make the list to double
M = map(lambda x:x*2,L)
# it will give us the map object then we have to convert to see the new list
print(list(M))

print(list(map(lambda x:x%2==0,L)))


# we have a data then we have to retrieve the name only from the data
student = [
    {
    "name" : 'jacob martin',
    "fathers name" : 'Ros Martin',
    "Address" : "123 hill street"
},
{
    "name" : 'angela stevens',
    "fathers name" : 'Robert stevens',
    "Address" : "3 upper street"
},
{
    "name" : 'ricky smart',
    "fathers name" : 'william smart',
    "Address" : "unknown"
}
]

c = map(lambda x:x['name'],student)
print(list(c))


# filter
# reduce