##Enumerate   Function
l1=["A","B","C","D","E","F"]
###It will print even index
for index,item in enumerate(l1):
    if index%2==0:
        print(f"Please Print {item}")
print("\n\n")
###It will print odd index
for index,item in enumerate(l1):
    if index%2!=0:
        print(f"Please Print {item}")