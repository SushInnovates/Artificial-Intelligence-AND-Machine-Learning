# 1 > print() : displays output
print("Hello World")

# 2 > input() : takes user input
input("Enter Your name : ")

# 3 > type() : returns the data type of a variable
a = 3
print(type(a))   # <class 'int'>
b = True
print(type(b))   # <class 'bool'>

# 4 > int(), float(), str(), list(), tuple() : type conversion
print(int(5.7))   # converts float to int

# 5 > abs() : returns absolute value
print(abs(4))     # 4
print(abs(-4))    # 4

# 6 > pow() : returns power (x^y)
print(pow(2, -3)) # 2^-3 = 0.125

# 7 > min(), max() : returns smallest/largest value
print(max([2, 3, 6, 83, 5]))
print(min([2, 3, 6, 83, 5]))
print(max("mumbai"))   # based on ASCII value

# 8 > round() : rounds a number
c = 22 / 7
print(c)
d = 12 / 7
print(round(d))   # rounded result

# 9 > divmod() : returns quotient and remainder
print(divmod(5, 2))    # (2, 1)

# 10 > bin(), oct(), hex() : converts to binary, octal, hex
print(bin(4))    # 0b100
print(hex(34))   # 0x22
print(oct(32))   # 0o40

# 11 > id() : returns unique identifier of an object
a = 3
print(id(a))

# 12 > ord() : returns ASCII value of a character
print(ord('c'))   # 99

# 13 > len() : returns length of a sequence
print(len('mumbai'))
print(len([1, 2, 3, 45]))

# 14 > sum() : returns sum of elements
print(sum({1, 2, 3, 4, 5}))

# 15 > help() : displays documentation of objects/functions
print(help('sum'))
