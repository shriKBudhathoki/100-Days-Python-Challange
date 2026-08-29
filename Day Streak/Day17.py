#Looping - For


print("Looping Name")
print()
name='Shree'
for i in name :
    print(i) # this print the no of name like 01234 shree (it print char no of 0-4 times)

for i in name:
    print(name) #this print same but it print name not the char

print()

print("looping list")
lists=["Red","Green","Orange","Yellow"]
for list in lists:
    print(list)     #Loop the red,yellow,yellow,orange (word)
    for i in list:
        print(i)    #Looping the Char not the word
print()

print("Looping range")

for j in range (0,5):
    #print(j) This loop go to 0 to 4 but not 5

    print(j+1) #This loop go to 0-7 but if  we add 1 in last
    #works 0+1=1 | 1+1=2 | 2+1=3 | 3+1=4  | 4+1=5 so it count 0-4



print("Looping the range only")

for k in range (0,5):
    print(k+1)

print()

print("Looping the ramge and step")

for o in range (1,21,1): # (Start,stop,steps(increment eg 1 or decrement -1))
    print(o)