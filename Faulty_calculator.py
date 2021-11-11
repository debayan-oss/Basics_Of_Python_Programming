print("Enter 1st number:",end=" ")
Number1 = int(input())
print("Enter 2nd number:",end=" ")
Number2 = int(input())
print("Enter operator +,-,*,/ on numbers:",end=" ")
Operator = input()
if (Number1 == 45 and Number2 == 3 or Number1 == 3 and Number2 == 45) and Operator == '*':
    print(Number1, Operator, Number2, " = ", 7777)
elif (Number1 == 56 and Number2 == 9 or Number1 == 9 and Number2 == 56) and Operator == '+':
    print(Number1, Operator, Number2, " = ", 77)
elif (Number1 == 56 and Number2 == 6 or Number1 == 6 and Number2 == 56) and Operator == '/':
    print(Number1, Operator, Number2, " = ", 4)
else:
    if Operator == '*':
        print(Number1, Operator, Number2, " = ",Number1*Number2)
    elif Operator == '+':
        print(Number1, Operator, Number2, " = ",Number1 + Number2)
    elif Operator == '-':
        print(Number1, Operator, Number2, " = ",Number1 - Number2)
    elif Operator == '/':
        print(Number1, Operator, Number2, " = ",Number1 / Number2)
    else:
        print("Unable to calculate, wrong operator")