# Looping in other languages:
# for(i = 0; i < num; i++) {
#     // code
# }

# In Python, we use the range() function

# Basic range examples
 # first number : starting , second number : ending , third number : step (means increament value by 1 or any other number)
print(list(range(1, 10)))   # start=1, stop=10 (exclusive)
print(list(range(7)))       # start defaults to 0

# Range with step
print(list(range(1, 101, 5)))   # start=1, stop=101, step=5

# Reverse step
print(list(range(21, 1, -2)))   # start=21, stop=1, step=-2

# -------------------------------
# Looping examples

# Sequence: numbers
for i in range(1, 11):
    print(i)

# Sequence with step
for i in range(1, 11, 2):
    print(i)

# Backward counting
for i in range(20, 0, -1):
    print(i)

# -------------------------------
# Iterating over different sequences

# String
for i in "kolhapur":
    print(i)

# List
for i in [1, 2, 34, 5, 7]:
    print(i)

# Tuple
for i in (1, 2, 34, 5, 7):
    print(i)

# Set
for i in {1, 2, 34, 5, 7}:
    print(i)
