'''
if computer == -1 and you == 1:     0 
            print("You win!") 
        elif computer == -1 and you == 0:  -1
            print("You lose!")
        elif computer == 1 and you == -1:   0
            print("You lose!")
        elif computer == 1 and you == 0:    1
            print("You win!")
        elif computer == 0 and you == -1:   -1
            print("You win!")
        elif computer == 0 and you == 1:    1
            print("You lose!")
        else:
            print("Something went wrong!")

sum = you + computer



if computer == -1 and you == 1:     -2
            print("You win!") 
        elif computer == -1 and you == 0:  -1
            print("You lose!")
        elif computer == 1 and you == -1:   2
            print("You lose!")
        elif computer == 1 and you == 0:    1
            print("You win!")
        elif computer == 0 and you == -1:   1
            print("You win!")
        elif computer == 0 and you == 1:    -1
            print("You lose!")
        else:
            print("Something went wrong!")

sub = computer - you

The below logic is written on the basis of the value of computer - you

'''

# if((computer -you) == -1 or (computer-you)== 2):
#     print("You lose")
# else:
#     print("You Win")

import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Validate user input to prevent KeyErrors
if youstr not in youDict:
    print("Invalid input! Please choose 's', 'w', or 'g'.")
else:
    you = youDict[youstr]

    print(f"You chose: {reverseDict[you]}\nComputer chose: {reverseDict[computer]}")

    if computer == you:
        print("It's a draw!")
    else:
         if((computer -you) == -1 or (computer-you)== 2):
            print("You lose")
         else:
            print("You Win")
         


"""

The Game rules

| You      | Computer | Result   |    
| -------- | -------- | -------- |
| Snake 🐍 | Water 💧 | You win  |   1      -1 
| Water 💧 | Gun 🔫   | You win  |  -1       0
| Gun 🔫   | Snake 🐍 | You win  |   0       1 
| Water 💧 | Snake 🐍 | You lose |  -1       1 
| Gun 🔫   | Water 💧 | You lose |   0       -1
| Snake 🐍 | Gun 🔫   | You lose |   1       0





"""
