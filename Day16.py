#Demonstrate the Switch Case in python

'''Write a Python program that asks the user to enter a number from 1 to 7, and then uses match-case to print the corresponding day of the week.'''


days =int(input("Enter a days between 1-7: "))


match days: #must be in one lane and attached to each other

    case 1:
        print("Sunday")
    case 2:
         print("Monday")
    case 3:
         print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thrusday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
          print("Invalid")

   