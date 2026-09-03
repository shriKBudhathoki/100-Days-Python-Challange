"""
A file contains a word "Donkey" multiple ties.You need to write a program which replace this word with ### by updating the same file/

"""
#My Version
user=input("Enter a updating name : ")
with open ("written.txt","w") as f:
    f.write (user)
f.close()
#Harry Version

rword=input("Enter a word you want replace : ")
user=input("Enter a replace word you want to replace : ")
with open("written.txt","r") as file:
    content=file.read()
contentNew=content.replace(rword,user) 
with open("written.txt","w") as file:
    file.write(contentNew)
file.close()
