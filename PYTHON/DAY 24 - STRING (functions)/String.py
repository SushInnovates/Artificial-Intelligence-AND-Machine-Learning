# String functions 
# ~ Common Functions
# 1>len 2> max 3> min 4> sorted

c = "mumbai"

# it returns the length of the String
print(len(c))

# it return the maximum ASCII value element 
print(max(c))

# it return the minimum ASCII value element
print(min(c))

# sorted - it sorts it according to ASCII value its by default is ascending order
print(sorted(c)) 

# to get it in descending order we have to use the hidden parameter which is 'reverse=True'
print(sorted(c,reverse=True))  

# 1 : Capitalize/Title/Upper/Lower/Swapcase

# capitalize - it only makes the first letter capital
print(c.capitalize())
d = 'it is raining today'
print(d.capitalize()) 

#title - it makes first letter of all the words capital
print(d.title())

# upper - it makes everything uppercase
f = " heLlo"
print(f.upper())

# lower - it makes everything lowercase
print(f.lower())

#swapcase - makes lowercase to uppercase and uppercase to the lowercase
print(f.swapcase())

# 2 : Count
# count - it counts the specified value
g = " it is raining outside"
print(g.count('i'))
print(g.count('ing'))
print(g.count('is'))
print(g.count('rain'))
print(g.count('f'))

# 3 - Find/index
h = " it is raining outside"
print(h.find('g')) # if there are mupliple value then it will return the first occurance of that value

print(h.find('x')) # it returns -1 when the value does not exits
print(h.find('raining')) 

# print(h.index('X'))

# 4 : endswith/startswith
h = "it is raining outside"
print(h.startswith('it'))
print(h.endswith('e'))
print(h.endswith('t'))

# 5 : format
k = "hello my name is {} and my age is {}".format("Gojo",27)
print(k)

k = "hello my name is {1} and my age is {0}".format("Gojo",27)
print(k)

k = "hello my name is {name} and my age is {age}".format(name = "Gojo",age = 27)
print(k)

# 6 : isalnum/isalpha/isdecimal/isdigit/isidentifier
l = "FLAT20".isalnum()
print(l)
l = "FLAT20%".isalnum()
print(l)
l = "FLAT20".isalpha()
print(l)

j = "20a".isdigit()
print(j)
j = "20".isdigit()
print(j)

z = "Hello world".isidentifier()
print(z)
z = "Hello_world".isidentifier()
print(z)

# 7 : Split 
x = " who is the prime minister of india".split()
print(x)

v = " who is the pm of india".split('pm')
print(v)

# 8 : join
b = " ".join(['who', 'is', 'the', 'prime', 'minister', 'of', 'india'])
print(b)
n = "~".join(['who', 'is', 'the', 'prime', 'minister', 'of', 'india'])
print(n)

# 9 : Replace
m = " hi my name is Gojo"
m1 = m.replace("Gojo","HonoredOne")
print(m1)

# 10 : Strip
name = "        gojo        "
print(name.strip())