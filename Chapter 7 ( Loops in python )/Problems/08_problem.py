# Write a program to print the following star pattern 
'''
*
**
***  for n=3

'''

number=int(input("Enter a number : "))
for i in range(1,number+1):
    print("*"*i,end="")
    print("")