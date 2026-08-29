"""
Write a program to print message when the age enter by the user is greater than or equal to 18 for enter to a club if bellow show message why
"""

message="Please be honest with the program."
while True:
    age=int(input("Enter your age :"))

    if age == -1:
        print(f"Program ended.{message}.")
        break
    elif(age<0):
        print(f"Invalid age {age}.")
    elif(age==0):
        print(f"{age} is not valid age.")
    elif(age>=18):
        print(f"You are eligible to enter because your age is {age}.")
    else:
        print("You are below the age of consent")
    print("Thankyou")