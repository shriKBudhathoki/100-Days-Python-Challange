#If the names of 2 friends are same; what will happen to the program in problem no 6?
d={}
i=1
for i in range(1,5):
    
    name=input(f"Enter a name {i} :")
    lan=input(f"Enter a language {i} :")
    d.update({name:lan})
print(d)

#The Vlaues enter later will be updated