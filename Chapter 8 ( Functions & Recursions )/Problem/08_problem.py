#Write a python function to print multiplication table of a given number
def Multiplication(a):
    i=1
    while(i<11):
        print(f"{a} X {i} = {a * i}")
        i+=1
    
Multiply=int(input("Enter a number:"))
Multiplication(Multiply)
