# Accessing Substrings from a String
# Concept of Indexing

print("INDEXING : ")
c = "hello"
print(c)

# Positive Indexing
print(c[0])  # h
print(c[1])  # e
print(c[2])  # l
print(c[3])  # l
print(c[4])  # o

# Types of Indexing
# 1 > Positive Indexing
# 2 > Negative Indexing

print(c[1])   # e
print(c[-1])  # o

# Note: If we select an index beyond the number of substrings,
# it will throw an error like 'IndexError: string index out of range'

# Slicing
print("\nSLICING : ")
c = "Hello World"
print(c)

print(c[0:5])     # Hello
print(c[2:])      # llo World
print(c[:4])      # Hell
print(c[:])       # Hello World
print(c)          # Hello World

print(c[2:6:2])   # lo
print(c[0:8:3])   # Hlw
print(c[0:6:-1])  # (no output, step direction mismatch)
print(c[-5:-1:2]) # Wr
print(c[::-1])    # dlroW olleH
print(c[-1:-5:-1])# dlro
