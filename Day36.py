#Exception Handling
import random
def Multiplication():
    #As input give the multiplication tabel
    a=input("Enter a number :")
    print(f"The Multiplication tabel user want is {a}")
    try:
     for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
    except Exception as e:        # or except:
       print("Invalid Input")
    print("Code sucessfully run")       
# Multiplication()

def Errors():
    try:
        num=int(input("Enter a number :"))
        a=[5,10,20,30,40,50,60,70,80,90,100]
        random.shuffle(a)
        print(a);print()
        print(f"Printed Index is {a[num]} and actual value is {num}")
    except ValueError:
        print("Numbers must be Integer")
    except IndexError:
        print("Number is not on Index")
    # finally:
    #    print(num)
Errors()

def Error():
   try:
      l = [10,15,20,25,30]
      i = int(input("enter a number"))
   except:
       print("nothing")