#IF-elif-else

num=int(input("Enter a number: "))
print("The age is",num)

print()

#Vote Eligible 

if(num>18):
    print("You can vote")

#'Indentation'
else:
    print("You cannot vote") 

print()

#Input a number and check if it is even or odd.
if(num%2==0):
    print("This is even number",num)

else:
    print("This is odd number",num)

print()

#Input a number and check if it is positive, negative or zero.

num1=int(input("Enter a PNZ Number: "))
if(num1<0):
    print("This is the negative number")

elif(num1==0):
    print("This is the zero number")
else:   
    print("This is the positive number")

    print()

#Check Voting Eligibility of person who can vote or not

vote=int(input("Enter your age: "))

if(vote<=17):
    print("You cannot give the vote")

else:
    print("You can give the vote")

print()

#Password checker which is give by user


import getpass #it simpily dont show the string give by user and it is useful

check_password="Hunter_sung"
password=getpass.getpass("Enter your password")

if(password==check_password):
    print("Accessed Granted")

else:
    print("Accessed Denied")

print()

#Check Divisibility by 5 or not

dive=int(input("Enter a number: "))

if dive%5==0:
    print("Provide No division by 5")

else:
    print("Provide No is not division by 5")

print()

#Number Comparison greatest among o & p also check zero & equal

o=int(input("Enter a number o: "))
p=int(input("Enter a number p: "))

if (o==0 or p==0):
    print("Please put above 0")

elif o>p:
    print(f"{o} is the greatest number")

elif p>o:
    print(f"{p} is the greatest number")

else:
    print("Both no is equal")

print()

#Login System

print("Simple Login System Ask for username and password. If both are correct, allow login.")

print()

import getpass

correct_pas="Password"
correct_use="Srikrishna"

username=input("Enter a Username: ")
password=getpass.getpass("Enter a password: ")

if(username==correct_use):
    if(password==correct_pas):
        print("Accessed Approved")
    else:
        print("Accessed Denied Password Wrong")    

else:
    print("username wrong")

print("Something went wrong!!")


