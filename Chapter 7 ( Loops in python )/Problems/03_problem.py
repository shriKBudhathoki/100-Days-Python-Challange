#Write a program to print multiplication table of a given number using for loop.
Multiplication=int(input("Enter a number : "))
i=1
while(i<10):
    print(f"{Multiplication} X {i} = {Multiplication*i}")
    i+=1
