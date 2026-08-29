"""
Write a program to print message when the age enter by the user is greater than or equal to 18 for enter to a club if bellow show message why both if statement
"""

message="Please be honest with the program."
while True:
    age=int(input("Enter your age :"))
    
    #IF statement no : 1
    if(age%2==0):
        print("Age is even")
    # else:
    #     print("Age is odd")
    
    #END of IF statement no : 1
    
    #IF statement no : 2
    
    if age == -1:
        print(f"Program ended.{message}.")
        break
    elif(age<0):
        print(f"Invalid Age {age}.")
    elif(age==0):
        print(f"{age} is not valid Age.")
    elif(age>=18):
        print(f"You are eligible to enter because your age is {age}.")
    else:
        print("You are below the age of consent")
    
    #END of IF statement no : 2
    
    print("Thankyou")