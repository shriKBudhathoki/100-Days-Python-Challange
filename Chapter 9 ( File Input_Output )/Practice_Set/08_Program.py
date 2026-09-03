'''
Write a program to make a copy of text file "this.txt"
'''
# import os
# path="d:\Coding\Python\Chapter 9 ( File Input_Output )\Practice_Set\07_Problem.py"

with open("this.txt","r") as file:
    content=file.read()

with open("this_copy.txt","w") as file:
    file.write(content)
    
    
#         file_path=os.path.join(table_path,f"table_{num}.txt")
#         table_path=os.path.join(path,"tables")
# os.makedirs(table_path,exist_ok=True)
# "d:\Coding\Python\Chapter 9 ( File Input_Output )\Practice_Set\07_Problem.py"