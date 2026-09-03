"""
Write a program to rename a file to "renamed_by_python.txt"
"""
# Gpt version

# import os
# old_name="Trial.txt"
# new_name="PRB11.txt"

# os.rename(old_name,new_name)
# print("File renamed sucessfully..!")

#Harry 

with open("old.txt") as f:
    content=f.read()
with open("rename_by_python.txt","w") as f:
    f.write(content)