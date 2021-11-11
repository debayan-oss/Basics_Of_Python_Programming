#join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))  ##Seperate join list
# # As we are on the subject, let us discuss another limitation associated with the join method. In situations where the iterable consists of a multi-data type, such as a list or tuple consisting of all integer variables and one single, double variable, the join function will not work. Instead, it will display an error. For join to function properly, all the variables should have the same sort of data type, either it is an integer, string, or any oth
# inputlist = ["Test1",13,"Test2",24,"Test3",100,"Test4"]
# sep = '_'
# out = sep.join(inputlist)
# print(out)

lis = ["John", "cena", "Randy", "orton",
       "Sheamus", "khali", "jinder mahal"]

# for item in lis:
#     print(item, "and", end=" ")

a = ", ".join(lis)
print(a, "other wwe superstars")
