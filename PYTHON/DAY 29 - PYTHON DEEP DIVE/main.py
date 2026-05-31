"""
Python Deep Dive : Mutability / Garbage Collection / Variable Referencing
"""

# VARIABLE AND MEMORY REFERENCE
print("VARIABLE AND MEMORY REFERENCE :")

# Call by Reference:
# You give the function a direct link to your variable.
# If the function changes it, the original changes too.
print("Call by Reference : ")
print("\tYou give the function a direct link to your variable. If the function changes it, the original changes too.")

# Call by Object:
# You give the function a copy of the reference to an object.
# If the object is mutable (like a list), changes persist.
# If immutable (like int, str, tuple), the original does not change.
print("Call by Object : ")
print("\tYou give the function a copy of the reference to an object. If mutable, changes stay. If immutable, the original doesn’t change.")

# Call by Value → Copy is sent → Original value does not change.
# Call by Reference → Actual variable/reference is sent → Original value changes.
# Call by Object → Reference to the object is passed → Object data can be modified and changes may be visible outside the function.


# ALIASING
print("ALIASING :")

# Aliasing means two or more variables refer to the same memory location (same object).
A = 11
B = 11
C = B
print(id(A))    # same memory location
print(id(B))    # same memory location
print(id(C))    # same memory location

# Example 1: Deleting one alias does not delete the object if another reference exists
a = 5
b = a
del a
print(b)    # still 5, because 'b' holds a reference

# Example 2: Reassigning one alias does not affect the other
a = 5
b = a
a = 7
print(b)    # remains 5


# REFERENCE COUNTING
print("REFERENCE COUNTING :")

# Reference counting means tracking how many variables point to a certain memory location.
import sys
x = "campusX"
y = x
z = y
print(id(x))
print(id(y))
print(id(z))
print(sys.getrefcount(x))  
# Note: getrefcount adds +1 because the function itself temporarily references the object.


# GARBAGE COLLECTION
print("GARBAGE COLLECTION :")

# Garbage Collection in Python is the automatic process of freeing memory
# occupied by objects that are no longer referenced or used.
# Python primarily uses reference counting and a garbage collector to manage memory automatically.


# WEIRD BEHAVIOUR
print("WEIRD BEHAVIOUR : ")

# Example 1: Small integers are cached internally, so refcount may look strange
a = 2
b = a
c = b
print(sys.getrefcount(a))   # may show a higher number due to internal references

d = 663
e = d
f = e
print(sys.getrefcount(d))   # more predictable


# Example 2: Integer caching
a = 4
b = 4
print(id(a), id(b))   # same id due to caching

a = 256
b = 256
print(id(a), id(b))   # still cached

a = 257
b = 257
print(id(a), id(b))   # different ids, not cached


# Example 3: String interning
a = "mumbai"
b = "mumbai"
print(id(a), id(b))   # same id

a = "indian institute of technology mumbai"
b = "indian institute of technology mumbai"
print(id(a), id(b))   # may differ

a = "indian_institute_of_technology_mumbai"
b = "indian_institute_of_technology_mumbai"
print(id(a), id(b))   # valid identifier-like strings are interned → same id


# MUTABILITY
print("MUTABILITY : ")

# Mutability refers to the ability to change or edit data in its memory location.
# If changed in the same location → mutable.
# If changed in a new location → immutable.

# Strings (immutable)
a = "Hello"
print(id(a))
a = a + "World"
print(id(a))   # new id → immutable

# Tuples (immutable)
T = (1, 2, 3)
print(id(T))
T = T + (5, 6)
print(id(T))   # new id → immutable

# Lists (mutable)
L = [1, 2, 3]
print(id(L))
L.append([5, 6])
print(id(L))   # same id → mutable


# CLONING TO AVOID SIDE EFFECTS
# Side effect: Mutating one list can affect another if they share references.
# Solution: Use cloning to create a separate copy.

a = [1, 2, 3, 4]
b = a[:]    # cloning using slicing
b.append(5)
print(b)
print(id(a))    # different memory location
print(id(b))    # different memory location

# Nested mutability
a = [1, 2, 3, [4, 5]]
a[-1][-1] = 500
print(a)    # inner list is mutable, so it changes

# Tuples containing lists are immutable at the top level, but lists inside remain mutable.
# Example:
# a = [1,2,3,(4,5)]
# a[-1][-1] = 500   # ERROR → tuple is immutable
