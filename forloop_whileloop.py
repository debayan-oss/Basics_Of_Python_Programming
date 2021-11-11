"""
###For Loop In List
lis1=["Harry","Carry","Larry","Marry"]

for item in lis1:
    print(item)

Lis2=[["Harry","Coder"],["Carry","Gamer"],["Larry","Chef"],["Marry","Teacher"]]
###For Loop In The Case Of List In List
for item,profession in Lis2:
    print(item,"Is",profession)
###For Loop In The Case Of Dictionary Data
dict1=dict(Lis2)
print(dict1)
for item,profession in dict1.items():
    print(item,"Is",profession)


###Quiz In For Loop
list=["Debayan","Mayukhjit",453,7.5,8,431,78.345,"Sourodwip",12,"Tapas"]
for item in list:
        if str(item).isnumeric() and item>6:
            print(item)

"""



##For Loop
i=0
while(i<78):
    print(i)
    i=i+1
    print(i)