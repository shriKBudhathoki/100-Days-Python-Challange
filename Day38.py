#Raise Custom error

def value():
    a=int(input("enter the value under 5-9: "))

    if(a<5 or a>9):
        raise ValueError("Not valid Input",a) #Raise Keyword Throw the value error if user give less than 5 or greather than 9
        
    print("Valid Input",a)
value()

def string():
#Task when user give quit string throw quit and dont take the other string

    a=input("Enter the string: ").upper()

    if a == "QUIT":
        print(a)
    else:   
        raise ValueError("not valid")
string()    