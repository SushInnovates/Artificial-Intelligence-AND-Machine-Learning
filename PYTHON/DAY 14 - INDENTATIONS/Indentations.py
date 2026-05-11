# in c /c++  we usually write the block of code like
# if num ==10){
#     something;
# }else{
#     something else;
# }

# but in python there is no ; or {} so we write it like
num = 10
if num == 10 :
    print("line1")
    print("line2")
    print("line3")
else:
    print("line1")
    print("line2")
    print("line3")

# we cannot write it like this
# if name == "xyz":
# print(line1)


name = "xyz"
if name == "xyz" :
    print("line 1")
    print("line 2")
    if  10 == 10 :
        print("line 1")
    else :
        print("ine 2")
else :
    print("line 2 of first block")         



             # 1 >   Indentation means adding spaces (or tabs) at the beginning of a line of code to visually separate blocks of code.
        #  2 > It helps show hierarchy, structure, and readability in programming.
    #  3 > In Python, indentation is not just for readability—it is syntactically required.
# 4  > Unlike many other languages (like C, C++, or Java) that use {} braces to define code blocks, Python uses indentation.