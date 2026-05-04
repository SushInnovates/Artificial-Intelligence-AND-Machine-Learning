# in programming, a keyword is a word that is reserved by a program because the word has a special meaning. 
# keywords can be commands or parameters, Every programming language has a set of keywords that cannot be used as variable names

# python has 33 keywords
import keyword
print(keyword.kwlist)

# Idenfiers : a Pythopn Identifier is a name used to identify a variable, function,, class, module or other object
# Rules  : 1> can only start with an alphabet or _  
#          2> Followed by 0 or more letter, _ and digit
#          3> keywords cannot be used as an identifiers

name = "CampusX"
print(name)

# 1> # = 2 print(#) is not allowed
# 2> 1Name = "CampusX" is not allowed

First_Name = "Campus"
print(First_Name)