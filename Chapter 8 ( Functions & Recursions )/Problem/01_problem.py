# Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if (a==b==c):
        return(f"Don't add same vlaue trice {a}")
        
    if(a>b and a>c):
        print(f"{a} is greater.")
    elif(b>a and b>c):
        print(f"{b} is greater")
    else:
        print(f"{c} is greater")

number_1 =int(input("Enter a number 1 : "))
number_2 =int(input("Enter a number 2 : "))
number_3 =int(input("Enter a number 3 : "))
print(" ")
print(greatest(number_1,number_2,number_3))