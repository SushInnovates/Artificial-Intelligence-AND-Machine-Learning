# Tuples
# Create
# Access
# Edit
# Add
# Delete
# Operations
# Function

# Create
T1 = ()
print(T1)

T2= (1,2,3,4)
print(T2)   # homogeneous

T3 = (1,2,3.5,'hello',True)
print(T3)   # Hetrogenous

T4 = (1,2,43,(4,5))
print(T4) #2D Tuple

T5 = ((1,3),(4,5,(7,8)))
print(T5)

print(type(T5))

T7 = tuple("Hello")
print(T7)
print(type(T7))

# we can create a tuple from a list too
T8 = tuple([1,2,3,4])
print(T8)

# Access
T2= (1,2,3,4)
print(T2[0])
print(T2[-1])
print(T2[::-1])
print(T2[:3])

T4 = (1,2,43,(4,5))
print(T4[-1][0])

# Edit 
L = [1,2,3,4,5]
L[0] = 100
print(L)

# Tuples are immutable
T2= (1,2,3,4)
# T2[0] = 100
# print(T2)

# Delete 

print(T1)
del T1
# print(T1)

# del T2[-1] #  not possible

# Operations
T2 = (1,2,3,4,5)
T3 = (6,7,8,9,10)
print(T2 + T3)

print(T2*3)

for i in T2:
    print(T2)

print(1 in T2)

# Functions
print(len(T2))
print(min(T2))
print(max(T2))
print(sorted(T2))
print(sorted(T2,reverse=True))

# tuples are read only datatype

