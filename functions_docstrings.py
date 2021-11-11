#BuiltinFunction
a=29
b=28
c=sum((a,b))#Sum of the Numbers
d=sorted((a,b))#It wil sorted the numbers
print (c)
print (d)
print("\n\n")
#User Defined Functions Docstrings
def function1():
    print("Hello You Are In function1")
function1()
print("\n\n")
def func2(a,b,c):
    print("Sum Of a,b,c:",a+b+c)
func2(10,20,30)
print("\n\n")
def func3(a,b):
       ###Docstring
    """This Function Will Give the average of two numbers"""
    average=(a+b)/2
    return average  #This Return Will Back The Value
v=func3(10,20)
print(v)##That wil print by variable v
###Print Docstring
print(func3.__doc__)
print("\n\n")
def func4(a,b,c):
    multiplication=(a*b*c)
    return multiplication
c=func4(12,13,14)
print(c)
print(func4.__doc__)##No Written Docstring So It Wil be Print None


