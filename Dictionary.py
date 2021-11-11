###Dictionary in Python
"""d1={}  ##It is a blank dictionary
print(d1)
print(type(d1))
d2={"Harry":"Code","Navin Reddy":"Python","CSDojo":"C++","Vijay":{"C":"Good","C++":"OOPs","Java":"Object Oriented","Python":"Best"}}####Dictionary Under in a dictionary
print(d2)
print(d2["Vijay"])##Printing the dictionary of only Vijay
#Adding Elements In Dictionary
#d1["Debayan"]="Electrical Engineering"
#print(d1)
#Removing Element From Dictionary
##del d2["Harry"]
##print(d2)
##del d2['Vijay']
##print(d2)
#Copying From One dict to another dictionary
"""
"""d3=d2.copy();
print(d2)
print(d3)
del d3["Harry"]
print(d3)##From Here Harry deleted
print(d2)##But here Harry Is Present
print(d2.get("CSDojo"))##It will give the vaue of CSDojo
"""
##Update any dictionary
d5={"A":"Apple","B":"Ball","C":"Cat"}
d5.update({"D":"Doll"})
print(d5)
d5.update({"E":"English"})
print(d5)
##Find The Keys.Items Of Dictionary
print(d5.keys())
print(d5.items())
