#Function

def summation(a,b):
    sum=a+b
    print("The summation of",a,"+",b,"=",sum)
    print()

    diff=a-b
    print("The difference of",a,"-",b,"=",diff)
    print()

    divide=a/b
    print("The divide of",a,"/",b,"=",divide)
    print()

    multiplication=a*b
    print("The multiplication of",a,"*",b,"=",multiplication)
    print()
    
    Modolus = a % b
    print("The Reminder of",a,"*",b,"=",Modolus)
    print()

def isgreater(i,j): #defining the function

    if(i>j):
        print("Firse",i,"is greatest than",j)
        print()
    
    elif(i==j):
        print("First and second no is equal",j)
        print()

    else:
        print("Second",j,"is greatest than",i)
        print()

p=int(input("enter a first number :"))  #giving the input
p1=int(input("enter a second number :")) #giving the input 
print()

isgreater(p,p1) #call the function
summation(p,p1)