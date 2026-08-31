'''
We all have played snake, water gun game in our childhood. If you haven't, google the rules of this game and write a python program capable of playing this garne with the user.

'''
import random

# Game Legend:
# 1 for snake
# -1 for water
# 0 for gun

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
        if computer == -1 and you == 1:
            print("You win!")
        elif computer == -1 and you == 0:
            print("You lose!")
        elif computer == 1 and you == -1:
            print("You lose!")
        elif computer == 1 and you == 0:
            print("You win!")
        elif computer == 0 and you == -1:
            print("You win!")
        elif computer == 0 and you == 1:
            print("You lose!")
        else:
            print("Something went wrong!")
