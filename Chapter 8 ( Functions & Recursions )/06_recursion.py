'''
    factorial(0) = 1
    factorial(1) = 1
    factorial(2) = 2 X 1
    factorial(3) = 3 X 2 X 1
    factorial(4) = 4 X 3 X 2 X 1
    factorial(5) = 5 X 4 X 3 X 2 X 1
    factorial(n) = n X n-1 X......3 X 2 X 1
    factorial(n) = n * factorial(n-1)
'''
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n* factorial (n-1)

n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")


#Factorial Through While-Loop
n = int(input("Enter a number: "))

if n == 0 or n == 1:
    factorial = 1
else:
    factorial = 1

    for i in range(1, n + 1):
        factorial = factorial * i

print(f"The factorial of this number is: {factorial}")


'''
1. Why is factorial = 1?

Because we're doing multiplication.

We want: 5! = 1 x 2 x 3 x 4 x 5

factorial = 1 × 1  → 1      |           0 x 1 = 0
factorial = 1 × 2  → 2      |           0 x 2 = 0
factorial = 2 × 3  → 6      |           0 x 3 = 0
factorial = 6 × 4  → 24     |
factorial = 24 × 5 → 120    |

'''
