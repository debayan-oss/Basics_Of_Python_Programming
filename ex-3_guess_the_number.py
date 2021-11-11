number=20
attempt=1
while(True):
    if(attempt<=9):
        attempt += 1
        x=int(input("Guess The Number:"))
        if(x<=19):
            print("Increase Your Assumption")
        elif(x==20):
            print("Correct Guess!You Win")
            break
        elif(x>=20):
            print("Decrease Your Assumption")
        print(10-attempt,"attempt are remaining")
    else:
        print("No More Attempts Are Here!")
        break
print("Thanks For Playing")
