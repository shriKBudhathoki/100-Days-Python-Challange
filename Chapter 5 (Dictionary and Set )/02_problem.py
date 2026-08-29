"""
Write a program to input eight numbers from the user and display all the unique numbers (once).
"""
# combination = set()

# for i in range(8):
#     user=input(f"Enter a Integer {i} : ")
#     combination.add(int(user))
# print(combination)

combination = set()

collection=int(input("Enter the set you want to loop : "))
for i in range(collection):
    user=input(f"Enter a Word or Integer {i} in range of {collection} : ")
    combination.add(int(user))
print(combination)