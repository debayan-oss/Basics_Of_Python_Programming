x=str(input("Enter Your Choice(True/False):\n"))
rows = int(input("Enter the number of rows: "))
i=0
j=0
if(True):
    for i in range(0,rows):
        # inner loop to handle number of columns
        # values is changing according to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")

            # ending line after each row
        print()

elif(False):
    # the outer loop is executing in reversed order
    for i in range(rows + 1, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print(" ")
        


