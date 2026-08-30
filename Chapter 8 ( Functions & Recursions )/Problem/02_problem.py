#Write a python program using function to convert Celsius to Fahrenheit


def celsius_to_fahrenheit(c):
    Fahrenheit=(c*9/5)+32
    return Fahrenheit

def fahrenheit_to_celsius(f):
    Celcius=(f-32)*5/9
    return Celcius

choice=int(input("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nChoose: "))

if choice==1:
    print("Choice no 1 : Convert fahrenheit to celsius")
    Celsius =int(input("Enter Celsius : "))
    print(f"Fahrenheit of Celsius {Celsius} is :  {celsius_to_fahrenheit(Celsius):.2f} °F")

elif choice==2:
    print("Choice no 2 : Convert celsius to fahrenheit")
    Fahrenheit =int(input("Enter Fehrenheit : "))
    print(f"Celcius of Fahrenheit {Fahrenheit} is : {fahrenheit_to_celsius(Fahrenheit):.2f} °C" )
else:
    print("invalid Choice")


'''
 store2=fahrenheit_to_celsius(Fahrenheit)
    print(f"Celcius of Fahrenheit {Fahrenheit} is : {round(store2,2)} °C" )
    
store1=celsius_to_fahrenheit(Celsius)
    print(f"Fahrenheit of Celsius {Celsius} is : {round(store1,2)} °F")

'''
