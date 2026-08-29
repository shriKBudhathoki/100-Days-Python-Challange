# Write a progrma to find whether a given number is prime or not

''' No is divisible by itself or one'''

number=int(input("Enter a number : "))
for i in range(2,number):
    if (number%i)==0 :
        print(f"This is not a prime number {number}")
        break
else:
    print(f"This is a prime numnber {number}")
    
    
    '''
2 = where we start checking

number = where we stop checking (not included)

i = the current possible divisor being tested.

'''
    