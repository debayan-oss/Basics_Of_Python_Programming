"""Printing Methods
print("My Name Is Debayan")
print('Chakraborty')
print("My Name Is Debayan",end=" ")
print("Chakraborty")
"""
#New Line Characteristics(Different Use Of \n and \\n and \t)
print("I AM AN ENGINEER\nOF ELECTRICAL BRANCH")
print("I AM AN ENGINEER\\nOF ELECTRICAL BRANCH")
print("I AM AN ENGINEER\tOF ELECTRICAL BRANCH")

#Different Type OF Datatype
var1="hello world"
var2=23
var3=45.89
print(type(var3),type(var2),type(var1))
print(var3+var2)
###Type Casting
var7="56"
var8="32"
print(var7+var8)##Normal String Addition
print(int(var7)+int(var8))###Typecasting(Convert String To Int)
###Special Typecasting
print(10*str(int(var7)+int(var8)))##It will print 88 ; 10 times


###Quiz1
x=int(input("Input 1st Number:--->"))
y=int(input("Input 2nd Number:--->"))
print("Sum Of Two Number",x+y)

##Quiz 2
x=float(input("Input 1st Number:--->"))
y=float(input("Input 2nd Number:--->"))
print("Sum Of Two Number",x+y)


##Quiz 3
x=str(input("Input 1st Number:--->"))
y=str(input("Input 2nd Number:--->"))
print("Sum Of Two Number",x+y)