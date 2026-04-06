# literals :
# defination :it is a raw data given to variable
# types : 1>numeric Literals 2>String Literals 3>Boolean Literals 4>Special Literals
 
# 1> Numeric Literals
a = 0b1010 #binary Literals
b = 100 #Decimal Literal
c = 0o310 #octal Literal
d = 0x12c #hexadecimal Literal

    #float Literal
float_1 = 10.5
float_2 = 1.5e2
float_3 = 1.5e-3

    #complex literal
x = 3.14j

print(a,b,c,d)
print(float_1,float_2,float_3)
print(x,x.imag,x.real)

# 2> String Literals
string = 'this is python'
string = "this is python"
char = "c" #it is still considered as string so there is no perticular char datatype
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\U0001f600\U0001F606\U0001F923" #emojies 
raw_str = r"raw \n string" #u can write special characters

print(string)
print(string)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

# 3>Boolean Literals
a = True + 4
b = False + 10
print("a : ",a)
print("b : ",b)

# 4>Special Literals 
a = None
print(a) # u cannot declare variable without values so if u  declare then it might cause trouble so by using such syntax u can overcome that trouble  