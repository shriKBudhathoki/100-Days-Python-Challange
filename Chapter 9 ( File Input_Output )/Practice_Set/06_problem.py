'''
Write a program to mine a log file and find out whether it contains'python'
'''

word="python"
with open("log.txt","r") as file:
    found=file.read()
    if word in found:
        print(f"{word} is found..")
    else:
        print(f"{word} is not found")