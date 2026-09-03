"""
Write a program to generate multiplication tables from 2 to 20 and
write it to the different files.place these files in a folder for 13-years old 
"""

""" Multiplication normal 

def multiplication():
    for i in range(2,21):
        for j in range(1,11):
            print(f"{i} X {j} = {i*j}")
multiplication()

"""


""" Code with harry 

def Tablegenerator(ret):
        table=" "
        for i in range (1,11):
         table+=f"{i} X {ret} = {ret*i}\n"
        with open(f"tables/table_{ret}.txt","w") as f:
            f.write(table)
for j in range(2,21):
    Tablegenerator(j)
    
    """
    
# Better Version of Chatgpt with using OS

import os

#This is the main folder where we want to create our "tables" folder
path = r"D:\Coding\Python\Chapter 9 ( File Input_Output )\Practice_Set"

#Create a "Tables" folder insidet the given path

table_path=os.path.join(path,"tables")
os.makedirs(table_path,exist_ok=True)

#Fucntion to generate a multiplication table 

def tablegenerator(num):
    
    #Empty String to store the complete table
    table=" "
    
    #Loop to 1 to 10
    for i in range(1,11):
        
        #Add each multiplication line to the table
        table+=f"{num} X {i} = {i * num}\n"
        
        #Create the complete path for the text file 
        #Example : ....\tables\table_5.txt
    file_path=os.path.join(table_path,f"table_{num}.txt")
    
    
    #open the file in write mode    
    with open(file_path,"w") as file:
        file.write(table)

#Generate Tables from 2 to 20
for j in range(2,21):
    
    #Call the function and pass the current number
    tablegenerator(j)