#Write a program which finds out whether a given name is present in a list or not.

list=["john","michael","satyam","ragav"]

name=input("Enter a name : ").lower()
if name in list:
    print("Yes the name is present in list")
else:
    print("No the name is not present in list")