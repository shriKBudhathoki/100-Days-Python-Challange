#F srting

print("Traditional F-string method")

stor=("Hello my name is {}. I am from {}")
name="Shree!"
country="Nepal"
print(stor.format(name,country)) #.format play role one it
print(stor.format(country,name)) #wrong typo passing for testing

stor1=("Hello my name is {1}. I am from {0}")
print(stor.format(name,country)) #Using the indexing 0 is name and 1 for country
print()

#Using the modern f-string form which is supported by python 3.6 version
print("Using modern way")
stor2=(f"Hello My name is {name} and I am from {country}") #This is the modern way
print(stor2)

price=49.09 
txt=(f"Cost is {price:.2f} only") #using same as C-programming .2f for float
print(txt)

print(f"{3*5}")
print(type(stor2))

stor2=(f"Hello My name is {{name}}and I am from {{country}}")#when we need to have as it is string
print(stor2)