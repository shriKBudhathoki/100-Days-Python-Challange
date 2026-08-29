# Write a program to greet all the person names stored in a list 'l' and which starts with S.

list=["Harry","Sonam","Sachin","Rahul","Shree krishna","Sweta","Sasmita"]

for name in list:
    if(name.startswith("S")):
        print(f"Hello,{name}")
