# # Local Variable Can Acces Global Variable But Global Variable Can Not Acces Local Variable
# l=10  ##Global Variable
# def function1(n):
#     l=5
#     m=7   ##Local Variable
#     print(l,m)
#     print(n,"I have printed Successfully")
# function1("Debayan Chakraborty")
# print(l)  #It will print global variable
#
# def function2(j):
#     m=9
#     print(l,m)   ##Here is no function as l so in function it will take the value from golbal Variable
#     print(j,"I have printed Successfully")
# function2("Debayan Chakraborty")
# #print(m)   It will give error because in global variable there is no m variable

##Local Variable Change Global Variable
# s=34
# def function3(k):
#     m=8
#     global s   ###It will give access to change the value of global variable
#     s=s+10
#     print(s,m)
#     print(k,"Thanks")
# function3("Debayan Chakraborty")
# print(s)  ###This value of global varaiable will also change due to the function name("global")




