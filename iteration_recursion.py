# Find Recursion Using IterativeMethod
# n=int(input("Enter A Number"))
# fac=1
# i=0
# for i in range(n):
#     fac=fac*(i+1)
# print(fac)

# Find Recursion Using Recursive Method
# def factorial_recursive(n):
#     if n==1:
#         return 1
#     else:
#          return n*factorial_recursive(n-1)
# num=int(input("Enter a number:"))
# print("Result of the factorial_recursive is",factorial_recursive(num))


# Quiz
#fibonacci series
def fibonacci_recursive(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)
num=int(input("Enter the last index: "))
print("Result of the fibonacci_recursive is",fibonacci_recursive(num))



