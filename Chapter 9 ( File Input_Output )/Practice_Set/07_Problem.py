"""
Write a program to find out the line number where python is present from ques 6
"""
# Harry Version


word=input("Enter a word : ")
with open("log.txt","r") as f:
    lines=f.readlines()
lineno=1
for line in lines:
    if(word.lower() in line.lower()):
        print(f"Yes python is present. Line no : {lineno}")
        break
    lineno+=1
else:
    print("No,{word} is not present")
    

# GPT Version 
word=input("Enter a word : ")
with open("log.txt","r") as f:
    lines=f.readlines()
lineno=1
found=False
for line in lines:
    if(word.lower() in line.lower()):
        print(f"Yes python is present. Line no : {lineno}")
        found=True
    lineno+=1
else:
    if not found:
        print(f"No,{word} is not present")
    
    
'''
How this version works
found = False

Initially we assume:

"I haven't found the word."

When we find it:

found = True

Then the loop continues, because there is no break.

'''