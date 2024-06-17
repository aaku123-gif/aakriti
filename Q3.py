#program that calculates the factorial of a given number.

n=int(input("enter the number: "))
factorial=1
if n<0:
    print("factorial doesnot exist for negative numbers")
elif n==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,n+1):
        factorial = factorial*i
    print("the factorial of",n,"is",factorial)
    