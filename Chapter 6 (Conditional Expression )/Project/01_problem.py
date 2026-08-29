"""
Write a program to find the greatesst of four numbers entered by the user.
"""
i=0
a1=int(input(f"Enter number {i+1} : "))
a2=int(input(f"Enter number {i+2} : "))
a3=int(input(f"Enter number {i+3} : "))
a4=int(input(f"Enter number {i+4} : "))

if(a1>a2 and a1>a3 and a1>a4):
    print(f"{a1} is greater than other number {a2},{a3},{a4} : ")
    
elif(a2>a1 and a2>a3 and a2>a4):
  print(f"{a2} is greater than other number {a1},{a3},{a4} : ")
  
elif(a3>a1 and a3>a2 and a3>a4):
   print(f"{a3} is greater than other number {a1},{a2},{a4} : ")
   
else:
    print(f"{a4} is greater than other number {a1},{a2},{a3} : ")

print("\n")

#If without condition expression by using list 

numbers=[ ]
for i in range(4):
    number=int(input(f"Enter a number {i+1} : "))
    numbers.append(number)
print(f"The greatest number is {max(numbers)}")
