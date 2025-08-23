#Recursion
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial (n-1)
print(factorial(5))
print()

# WAP to print the Fibonacci sequence

'''
f(0)=0
f(2)=1
f(2)= f(1) +f(0)
f(n)= f(n-a)+f(n-2)

'''

def fibonacci(num):
    if(num==0):
        return 0
    elif(num==1):
        return 1
    else:
         return fibonacci(num-1) + fibonacci(num-2)

for i in range(10):
 print(fibonacci(i))

 '''
 Implementation

 f(0) = 0
f(1) = 1
f(2) = f(1) + f(0) = 1 + 0 = 1
f(3) = f(2) + f(1) = 1 + 1 = 2
f(4) = f(3) + f(2) = 2 + 1 = 3
f(5) = f(4) + f(3) = 3 + 2 = 5
f(6) = f(5) + f(4) = 5 + 3 = 8
f(7) = f(6) + f(5) = 8 + 5 = 13
f(8) = f(7) + f(6) = 13 + 8 = 21
f(9) = f(8) + f(7) = 21 + 13 = 34
f(10) = f(9) + f(8) = 34 + 21 = 55
 '''