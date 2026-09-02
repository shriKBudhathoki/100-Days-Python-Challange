# Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'

user=input("Enter a word : ").lower()
f=open("poems.txt")
checker=f.read().lower()
if user in checker:
    print("Found",user)
else:
    print("Not found",user)
f.close()   
    
