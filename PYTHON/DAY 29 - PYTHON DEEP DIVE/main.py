print("Python Deep Dive : Mutability / Garbage Collection / Variable Referencing")

print("VARIABLE AND MEMORY REFERENCE :")
print("CAll BY REFERENCE : ")
print("/tYou give the function a direct link to your variable. If the function changes it, the original changes too.")
print("CAll BY OBJECT : ")
print("/t You give the function a copy of the reference to an object. If the object is something that can be changed (like a list), the changes stay. If it’s something fixed (like a number), the original doesn’t change.")

# Call by Value → Copy is sent → Original value does not change.
# Call by Reference → Actual variable/reference is sent → Original value changes.
# Call by Object (Python/Java objects) → Reference to the object is passed → Object data can be modified and changes may be visible outside the function.

print("ALIASING :")
# Q. What does aliasing means?
# Two or more variables refering to the same memory location (same object)
A = 11
B = 11 
C = B
print(id(A))    # same memory location
print(id(B))    # same memory location
print(id(C))    # same memory location

# ex- 
a = 5
b = a 
del a 
# Q what will happen?? will the b remain or be deleted?
print(b)    # still it will be 5

# ex 
a = 5
b = a
a = 7
print(b)
# what will be the value of b? 5 or 7?

print("REFERNCE COUNTING :")
# It means to get the count of how many variables are pointing to the certain memory location

# ex -
import sys
x = "campusX"
y = x
z = y
print(id(x))
print(id(y))
print(id(z))
print(sys.getrefcount(x)) # when we use the getrefcount so the total number of countings will be ' the total count of number + 1( which is getrefcount because when this function works to get the number of variables pointing to that perticular memory location this getrefcount will also points to that memory locations thats why)

print("GARBAGE COLLECTION : ")
#Garbage Collection in Python is the automatic process of freeing memory occupied by objects that are no longer referenced or used. Python primarily uses reference counting and a garbage collector to manage memory automatically.

print("WEIRD BEHAVIOUR : ")
print("1 : ")
a = 2
b = a
c = b
print(sys.getrefcount(a))   # here it should have gave 3 + 1 = 4 count but when we run it gives weird number
# because here 2 is very common number so in machine there are lot of function are running so they got referenced to it thats why it is showing weird number

d = 663
e = d
f = e
print(sys.getrefcount(d))

print("2 : ")
a = 4
b = 4
print(id(a))
print(id(b))

a = 256
b = 256
print(id(a))
print(id(b))

a = 257
b = 257
print(id(a))
print(id(b))
# all the ids will be same but for some cases it will be different

