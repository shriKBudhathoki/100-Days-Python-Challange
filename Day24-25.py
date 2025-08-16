#Tuple

'''
Point to be noted
1. Tuple are ordered collectio of data items
2. It store multiple items in a single variable
3.It seperated by commas and enclosed with round bracket()
4. It is unchangable meaning we can not after them after creation.

'''

# print("Tuple is same as list but tuple cannot change the variable")
# print()

# tup=(1,2,3,4,5,6,7,8,"shree",True) #it can also store string,boolean,string same as list
# print("Printing the tupple",type(tup),tup)
# print("Length of tup",len(tup))

# '''  It throw the exception we cannot change the truple
# print("Tupple Changing Try1")
# tup[0] =500 
# print(tup)
# '''

# #slicing
# print("1:4 Slicing")
# print(tup[1:4]) #it goes 1 to 4 
# print(":0:5 indexing")
# print(tup[:5]) #python automatically add 0 on it so 0:5
# print("Negative indexing")
# print(tup[1:-1]) #trying negative indexing which is 1 to len(tup) - 1 is that  shree

# #Trying if-else in tuple

# if 8 in tup:
#     print("yes it is exit")
# else:
#     print("No it is not")

# #Trying the jump list (start:stop:step to jump) slicing 
# tup2 = tup[1:5]
# print(tup2)
# print(tup[1:8:2])

#Tupples method to manipulate the tupples using different variable stores

list2=(90,5,10,20,30,40,50)
list1 = sorted(list2)
print(list1)

countries =("spain","america","australia","Russia")
print("Before converting to list",countries)

temp=list(countries)          #list() is used to make the tuple editable.
temp.append("Nepal")        # adds Nepal at the end
print(temp)

#temp.pop(3)
a=temp.pop(3)                # removes item at index 3, and stores it

temp[2]="India"            # replaces "australia" with "India"

countries = tuple(temp)  # converting list back to tuple
print("After the pop,append,add element",countries)
print("Poped Item:",a)
print()


#Concatinare the two types
print("Concatinare the two types")
country =("spain","Itally","England")
country2=("korea","Japan","UK")
Countryalie =country+country2
print(Countryalie)

#Count
li =(5,10,50,20,15,25,35,30,20,30,20,30,20,320,20)
ten =li.count(20)
print("Tupple count is",ten)
ten1 =li.index(320)
print("Tupple given index no is in",ten1)
print("Length of li",len(li))

#indexing(element,start,end)
ten=li.index(35,1,15)
print("The element is found on",ten)
