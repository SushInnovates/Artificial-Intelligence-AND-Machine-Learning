# ============================================
# 📘 Python Lists - Complete Guide
# ============================================

# 1️⃣ What is a List?
# A list in Python is an ordered, mutable collection of elements.
# It can store multiple items of different data types (heterogeneous).
# Lists are defined using square brackets [].

# 2️⃣ List vs Array
# Arrays are homogeneous — all elements must be of the same data type.
# Lists are heterogeneous — elements can be of different data types.
# Arrays store elements in contiguous memory locations, making them faster.
# Lists are not stored contiguously, but they are more flexible and programmer-friendly.

# ============================================
# 🧩 Creating Lists
# ============================================

L = []  # Empty list
print(L)

L1 = [1, 2, 3, 4, 5]
print(L1)

L2 = ["hello", 12, True, 11.2]  # Mixed data types
print(L2)

# Multi-dimensional lists
# 2D list
L3 = [1, 2, 3, [4, 5]]
print(L3)

# 3D list
L4 = [[[1, 2], [3, 4], [5, 6]]]
print(L4)

# Using list() constructor
L5 = list('mumbai')
print(L5)

L6 = list()
print(L6)

# ============================================
# 🔍 Accessing Elements
# ============================================

print(L1[0])      # First element
print(L1[-1])     # Last element
print(L1[1:3])    # Slicing
print(L1[::-1])   # Reverse list

# Accessing nested lists
L3 = [1, 2, 3, [4, 5]]
print(L3[3][0])   # Access element inside nested list

L4 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(L4[1][1][0])  # Access deeply nested element

L5 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(L5[0][1][1])

# ============================================
# ✏️ Editing Lists
# ============================================

L = [1, 2, 3, 4, 5, 6]
L[0] = 100  # Lists are mutable
print(L)

print(L[-1])

# Replace a slice
L[1:3] = [100, 200, 300]
print(L)

# ============================================
# ➕ Adding Elements
# ============================================

# append() - adds a single element
L.append(600)
L.append("Hello")
print(L)

# extend() - adds multiple elements
L.extend([700, 800, 900])
print(L)

# append() with list adds as a single element
L.append([5, 6])
print(L)

# extend() with string adds each character separately
L.extend("Mumbai")
print(L)

# insert() - adds element at specific position
L9 = [1, 2, 3, 4, 5]
L9.insert(1, "Hello")
print(L9)

# ============================================
# ❌ Deleting Elements
# ============================================

# del - delete by index or entire list
del L2  # Deletes entire list

del L1[0]  # Deletes element at index 0
print(L1)

L10 = [100, 100, 200, 300, 4, 5, 6, 600, 'Hello', 700, 800, 900, [5, 6], 'M', 'u', 'm', 'b', 'a', 'i']
del L10[1]
print(L10)

del L10[-6:]  # Delete last 6 elements
print(L10)

# remove() - delete by value
L10.remove("Hello")
print(L10)

# pop() - removes last element and returns it
print(L10.pop())
print(L10)

# clear() - empties the list
L10.clear()
print(L10)

# ============================================
# ⚙️ Operations on Lists
# ============================================

# Concatenation
L1 = [1, 2, 3, 4, 5]
L2 = [10, 20, 30, 40, 50]
print(L1 + L2)  # Creates new list

# Repetition
print(L1 * 3)

# Iteration
for i in L1:
    print(i)

L3 = [1, 2, 3, [4, 5]]
for i in L3:
    print(i)

# Membership
print(4 in L3)
print([4, 5] in L3)

# ============================================
# 🧮 Built-in Functions
# ============================================

L1 = [1, 2, 3, 4, 8, 5]
print(len(L1))          # Length
print(min(L1))          # Minimum
print(max(L1))          # Maximum
print(sorted(L1))       # Sorted ascending
print(sorted(L1, reverse=True))  # Sorted descending

L = [1, 2, 3, 4]
L.sort(reverse=True)
print(L)

print(L.index(4))       # Find index of element

# String function example
D = "hello how are you"
print(D.title())

# ============================================
# 🧠 Example Questions
# ============================================

# Q1: Implement title() manually
sample = input("Enter a string: ")
L = []
for i in sample.split():
    L.append(i.capitalize())
print(" ".join(L))

# Q2: Extract username from email
s = input("Enter Mail: ")
print(s[:s.find('@')])

# Q3: Remove duplicates from list
L1 = [1, 1, 2, 3, 4, 3, 4, 2]
L = []
for i in L1:
    if i not in L:
        L.append(i)
print(L)
