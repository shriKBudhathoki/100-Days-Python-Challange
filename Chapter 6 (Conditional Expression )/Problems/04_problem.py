"""
Write a program to find whether a given username contains less than 10 characters or not.
"""
username =input("Enter a username : ")

if(len(username)<10):
    print(f"Make sure your username contains atleast 10 characters, {username}")
else:
    print(f"Your username contain 10 character so is, {username} ")