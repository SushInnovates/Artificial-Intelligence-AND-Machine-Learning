# String Functions in Python
# ~ Common Functions
# 1. len()   2. max()   3. min()   4. sorted()

c = "mumbai"

# len() - returns the length of the string
print(len(c))   # Output: 6

# max() - returns the character with the maximum ASCII value
print(max(c))   # Output: 'u'

# min() - returns the character with the minimum ASCII value
print(min(c))   # Output: 'a'

# sorted() - sorts characters by ASCII value (ascending by default)
print(sorted(c))   # Output: ['a', 'b', 'i', 'm', 'm', 'u']

# sorted() with reverse=True - sorts in descending order
print(sorted(c, reverse=True))   # Output: ['u', 'm', 'm', 'i', 'b', 'a']


# 1 : Capitalize / Title / Upper / Lower / Swapcase
c = "mumbai"

# capitalize() - makes only the first letter uppercase
print(c.capitalize())   # Output: 'Mumbai'

d = "it is raining today"
print(d.capitalize())   # Output: 'It is raining today'

# title() - makes the first letter of every word uppercase
print(d.title())   # Output: 'It Is Raining Today'

# upper() - converts all characters to uppercase
f = " heLlo"
print(f.upper())   # Output: ' HELLO'

# lower() - converts all characters to lowercase
print(f.lower())   # Output: ' hello'

# swapcase() - swaps uppercase to lowercase and vice versa
print(f.swapcase())   # Output: ' HEllO'


# 2 : Count
g = " it is raining outside"

# count() - counts occurrences of a substring
print(g.count('i'))       # Output: 4
print(g.count('ing'))     # Output: 2
print(g.count('is'))      # Output: 2
print(g.count('rain'))    # Output: 1
print(g.count('f'))       # Output: 0


# 3 : Find / Index
h = " it is raining outside"

# find() - returns the index of first occurrence, -1 if not found
print(h.find('g'))        # Output: 13
print(h.find('x'))        # Output: -1
print(h.find('raining'))  # Output: 7

# index() - similar to find(), but raises an error if not found
# print(h.index('X'))  # ❌ ValueError


# 4 : startswith() / endswith()
h = "it is raining outside"
print(h.startswith('it'))   # Output: True
print(h.endswith('e'))      # Output: True
print(h.endswith('t'))      # Output: False


# 5 : format()
# Using positional arguments
k = "hello my name is {} and my age is {}".format("Gojo", 27)
print(k)

# Using index positions
k = "hello my name is {1} and my age is {0}".format("Gojo", 27)
print(k)

# Using named placeholders
k = "hello my name is {name} and my age is {age}".format(name="Gojo", age=27)
print(k)


# 6 : isalnum / isalpha / isdigit / isidentifier
print("FLAT20".isalnum())     # True (letters + numbers)
print("FLAT20%".isalnum())    # False (contains %)
print("FLAT20".isalpha())     # False (contains numbers)

print("20a".isdigit())        # False (contains letter)
print("20".isdigit())         # True (only digits)

print("Hello world".isidentifier())   # False (space
