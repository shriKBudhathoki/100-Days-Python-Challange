'''
We all have played snake, water gun game in our childhood. If you haven't, google the rules of this game and write a python program capable of playing this garne with the user.

'''
import random
# Game Legend:
# 1 for snake
# -1 for water
# 0 for gun
computer=random.choice([1,0,-1])
# youStr=input("Enter a number [ snake:1 , water : -1 , Gun : 0] : ")
youStr = input("Enter [s = Snake, w = Water, g = Gun]: ")
youDist = {"s":1,"w":-1,"g":0}
reverseDist={1:"Snake",-1:"Water",0:"Gun"}
message="Please input s,w,g"
if youStr not in youDist:
    print(f"invalid input ! ,{message}")
else:
   you = youDist[youStr]
   print(f"Your Choice : {reverseDist[you]}\n Computer Choice : {reverseDist[computer]}")
   
   if computer==you:
       print("Draw...!")
       
   elif you==1 and computer==-1:
       print("You Win..!")
   elif you==-1 and computer==-0:
       print("You Win..!")
   elif you==0 and computer==1:
       print("You Win..!")
   elif you==-1 and computer==1:
       print("You Lose..!")
   elif you==0 and computer==-1:
       print("You Lose..!")
   elif you==1 and computer==0:
       print("You Lose..!")