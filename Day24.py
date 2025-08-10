#Tuple

'''
Point to be noted
1. Tuple are ordered collectio of data items
2. It store multiple items in a single variable
3.It seperated by commas and enclosed with round bracket()
4. It is unchangable meaning we can not after them after creation.

'''

print("Tuple is same as list but tuple cannot change the variable")
print()

tup=(1,2,3,4,5,6,7,8,"shree",True) #it can also store string,boolean,string same as list
print("Printing the tupple",type(tup),tup)
print("Length of tup",len(tup))

'''  It throw the exception we cannot change the truple
print("Tupple Changing Try1")
tup[0] =500 
print(tup)
'''

#slicing
print("1:4 Slicing")
print(tup[1:4]) #it goes 1 to 4 
print(":0:5 indexing")
print(tup[:5]) #python automatically add 0 on it so 0:5
print("Negative indexing")
print(tup[1:-1]) #trying negative indexing which is 1 to len(tup) - 1 is that  shree

#Trying if-else in tuple

if 8 in tup:
    print("yes it is exit")
else:
    print("No it is not")

#Trying the jump list (start:stop:step to jump) slicing 

print(tup[1:8:2])

