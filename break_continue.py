##Break Statements
##This Program will Print 0-43
i=0
while(True):
    if (i == 44):
        break  ###Stop the loop
    print(i, end=" ")
    i=i+1
print("\n")

##This Program will Print 0-44
i=0
while(True):
    print(i, end=" ")
    if (i == 44):
        break  ###Stop the loop
    i=i+1


###Continue Statement
i=0
while(True):
    if (i<5):
        i=i+1
        continue ###Continue
    print(i, end=" ")
    if(i==45):
        break
    i=i+1

print("\n")




#Quiz
while(True):
    x=int(input("Enter Number"));
    if(x<100):
        continue
    if(x==100):
        print("You Have Entered 100")
        continue
    else:
        print("Congats You have entered more than 100")
        break
