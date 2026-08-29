#Function Argeuments
'''
1. Default argument 
2. Required argument
3. variable length argument
4. keyword argument
'''
#Default Argument
print("Default argument")

def defaul(a=10,b=5): #one run other still 

    print("The calculation is =",(a+b)/2)

defaul(5) # it override the a=10 and a is now 5 and program take 5
defaul(b=20) # it override the b=5 and a is now 20 and program take 20 but a=10 now 

print()

#another example

def names(fname,mname="krishna",lname="Budhathoki"):
    print("Hello,",fname,mname,lname)

names("Mr","Sri krishna","Budhathoki")
print()

#keyword argument
print("Keyword Argument")
def defaul(a=10,b=5): #one run other still 

    print("The calculation is =",(a+b)/2)

defaul(a=500,b=1000) #the value by keyword argument override the default

#required argument
def num(a,b,c=1):
    print("The summation of 3 is",a+b+c)

num(1,5)#this is required argument weher a,b must be have value and c is optional also must to add value otherwise program not run

print()
#variable length number
print("variabe length")
def numbers(*charac):
    print(type(charac))
    sum=0
    for i in charac:
        sum = sum + i #calulation of sum
    print("The average is", sum / len(charac) )

numbers(5,6,20,30) #it sum and divide by the length of no 

print()
print("Alternative,")

print("variabe length Example 2 return type")
def numbers(*charac):
    
    sum=0
    for i in charac:
        sum = sum + i #calulation of sum
    #return 7 #it take first return get more value

    return sum / len(charac) #return=wapch leke jao value ko

c=numbers(5,6,20,30) #it sum and divide by the length of no 
print(c)

print()

#Example 2 of variable length for dictionary

def dicto(**name):
    print(type(name))
    print("Hello",name["fname"],name["mname"],name["lname"])

dicto(fname="amy",mname="ton",lname="Christopher")