'''
Write a python function to print first n lines of the following pattern:
***
**
*
n = 3

'''

def pattern(n):
    if(n==0): #Stop condition
        return #Stop recursion
    print("*"*n)
    pattern(n-1)
    
number=int(input("Enter a number : "))
pattern(number)
    
    
'''
pattern(3)
    ↓
print("***")
    ↓
pattern(2)
    ↓
print("**")
    ↓
pattern(1)
    ↓
print("*")
    ↓
pattern(0)
    ↓
n == 0 → return


A recursive function keeps calling itself until its stopping condition (return) is reached.

'''
print("")
#For loop version

number = int(input("Enter a number: "))

for i in range(number, 0, -1):
    print("*" * i)
''''

Start = 5
Stop = 0 (but don't include 0)
Step = -1 (decrease by 1)

i = 5 → 4 → 3 → 2 → 1
    
'''