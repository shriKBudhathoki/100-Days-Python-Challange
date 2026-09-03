'''
Write a program to find out whether a file is identical and matches the content of another file
'''

with open("this.txt") as file:
    content1=file.read()
    
with open("this_copy.txt") as file:
    content2=file.read()

if(content1==content2):
    print("Yes both content are Identical...!")
else:
    print("No both content are not Identical...!")