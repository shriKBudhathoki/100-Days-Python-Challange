#Write a program to print multiplication table of given number using for loop

Multiplication=int(input("Enter a multiplication number : "))
for i in range (1,11):
    print(f"{Multiplication} X {i} = {Multiplication*i}")
    