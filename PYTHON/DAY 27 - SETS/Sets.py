# sets 

# 1 > sets do not allow duplicates
# 2 > sets have no indexing nor slicing
# 3 > sets dont allow mutable datatypes ig list
# 4 > sets itself is a mutable datatype

s1 = {}
print(s1) # but it is not a set
print(type(s1)) # it will create a empty set

s2 = set()
print(s2)
print(type(s2))

s1 = {1,2,3,4,5}
print(s1)   # homogenous set

s2 = {1,2,3.5,'Hello',True}
print(s2)   # hetrogenous set

s3 = {1,1,2,2,3,3,4,4}
print(s3)   # it will show {1, 2, 3, 4} as sets do not allow duplicates

# s4 = {[1,2,3],'Hello'}
# print(s4) # it will throw error as sets do not allow mutable datatype and here list is a mutable datatype

s5 = {(1,2,3),'Hii'}
print(s5) # as tuple and string is immutable so it will not throw error
# here we wrote hii as last item but in output it is prined first because sets do not follow indexing
# it is basically due to hashing behaviour

# s6 = {1,2,3,{4,5}}
# print(s6)   # we cannot create 2D,3D,4D sets as set itself is a mutable datatype

# Access Item
s1 = {1,2,3,4,5}
# print(s1[0]) # it will throw error due to sets do not follow indexing

# print(s1[-1]) # it will throw error due to sets do not follow indexing

# print(s1[:3]) # it will throw error due to sets do not follow indexing
 
# Edit Items 
s1 = {1,2,3,4,5}
# s1[2]=100
print(s1)

# editing will not work in same set
print(id(s1))

L = list(s1)
L[0]=100
print(L)

s1 = set(L)
print(s1)
print(id(s1))

# although set is mutable dattype but we cannot edit the set

# add
s1 = {1,2,3,4,5}
s1.add(18)
print(s1)

# Delete
# 1 > del 2> remove 3> pop
s2 = {1,2,3.5,'Hello',True}
del s2
# print(s2)

# del s1[0] will not work as their is no indexing

s8 = {1,2,3.5,'Hello',True}
s8.remove(3.5)
print(s8)

s8.pop()
print(s8) # it will remove the last element but it will be True 

# operations
s1 = {1,2,3,4,5}
# print(s1+s2) # it will throw error as their is no concatenation

# print(s1*3) # it will throw error as their is no repetation

for i in s1:
    print(i)

# function
s1 = {1,2,3,4,5}
print(len(s1))
print(min(s1))
print(max(s1))
print(sum(s1))
print(sorted(s1))
print(sorted(s1,reverse=True))

s1 = {1,2,3,4,5,11}
s2 = {11,22,33,44,55}

print(s1.union(s2))

print(s1.intersection(s2))

print(s1.difference(s2))
print(s2.difference(s1))

print(s1.symmetric_difference(s2))

print(s1.isdisjoint(s2))

print(s1.issubset(s2))

print(s1.issuperset(s2))

s1.clear()
print(s1)