"""Write a program to wipe out the content of a file using python"""

with open("this.txt","r") as file:
    file.read()
with open("this.txt","w")as file:
    file.write("")