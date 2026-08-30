#Write a program to print multiplication table of n using loops in reversed order

Multiplication=int(input("Enter a multiplication number : "))
for i in range (1,11):
    print(f"{Multiplication} X {11-i} = {Multiplication*(11-i)}")
    