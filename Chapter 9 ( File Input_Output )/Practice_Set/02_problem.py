"""
The game() function is a program lets a user play a game and returns the score as an integer. 
You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. 
You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score


with open("file.txt") as f:
    print(f.read())
    

"""
# import random

# def game():
#     print("Let's play a game : ")
#     score = random.randint(1,62)
#     # Fetcg the hiscore
#     with open("Hi-score.txt","r") as f:
#         hiscore=f.read()
#         if(hiscore!=""):
#             hiscore=int(hiscore)
#         else:
#             hiscore=0
            
#     print(f"Your Score is : {score}")
#     if(score>hiscore):
#         with open("Hi-score.txt","w") as f:
#             f.write(str(score))
#     else:
#          print("Something went wrong")
        
#     return score
# game()
                    
import random

def game():

    print("Let's play a game:")

    score = random.randint(1, 62)

    # Fetch the hiscore
    with open("Hi-score.txt", "r") as f:
        hiscore = f.read()

        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your Score is : {score}")

    if score > hiscore:
        with open("Hi-score.txt", "w") as f:
            f.write(str(score))
        print(f"New high score!, {score}")
    else:
        print(f"You did not beat the high score, {hiscore}")

    return score

game()