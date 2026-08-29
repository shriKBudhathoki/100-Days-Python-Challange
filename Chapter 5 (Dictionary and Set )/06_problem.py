"""
Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names.
Assume that the names are unique.

"""
attempt=1
library={}
wrong_name=[]
Friends=["shreekrishna","anasansari","unishsthapit","gauravthapa"]
# for i in range(4):
while len(library)<4:
    temp=input(f"Enter your name {attempt} : ").lower()
    if temp in Friends:
        language=input("Enter your Favorite language: ")
        library[temp]=language
    else:
        print(f"Sorry name is not here {temp}. ")
        wrong_name.append((attempt,temp))
    attempt+=1
        
print("\n Fraviroate Language")
print(library)

print("\n Wrong names entered")    
for attemp_no,name in wrong_name:
    print(f"Attempt {attemp_no} = wrongname:{name}")

"""
tuple unpacking 
wrong_name.append((attempt, temp))
wrong_name = [
    (2, "ram"),
    (5, "hari"),
    (6, "sita")
]

(2, "ram")
 ↑    ↑
attempt  name

for attempt_no, name in wrong_name: ((2, "ram")) ==> attempt_no = 2
name = "ram"

wrong_name
    ↓
(2, "ram")   → attempt_no = 2, name = "ram"
(5, "hari")  → attempt_no = 5, name = "hari"
(6, "sita")  → attempt_no = 6, name = "sita"



for item in wrong_name:
    attempt_no = item[0]
    name = item[1]




"""

