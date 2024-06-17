#this generates the first n numbers in the Fibonacci sequence.

def fibonacci_sequence(number):
    if number==0:
        return 0
    elif number==1:
        return 1
    else:
        return fibonacci_sequence(number-2) + fibonacci_sequence(number-1)

n=7
for i in range(0,n):
    print(fibonacci_sequence(i),end=" ")