#List in the python

marks=[1,2,5,6,5,8,"shree","krishna"] #we can also pass string
# print(type(marks))
# print(marks[4])
# print(marks)

# #if negative indexing 
# print(marks[1:-1]) #normally -1 subtracting the no from total len of list 8-1 = [2, 5, 6, 5]

# print(marks[1:-3])
# print(marks[1:len(marks)-3])#normally -3 subtracting the no from total len but not include last cuz slicing

# if "shree" in marks:
#     print("Yes")
# else:
#     print("hell no")

# if "ree" in "krishna":
#     print("Yes")
# else:
#     print("No")    

# if "2" in marks:
#     print("Yes 6 is present")
# else:
#     print("no it is not,6")

# #same thing applies on the string as well!!

# if "her" in "shree":
#     print("Yes it is present")
# else:
#     print("no it is not,")

# print(marks)
# print(marks[1:-1])
# print(marks[1:5])
# print(marks[1:5:2])

#list comprehension

# lis=[10,11,12,13,14,15,16,17,18,19,20]

lis =[ i*i for i in range(4)] 
print(lis)

lis1=[i*i for i in range(10)]
print(lis1)

lis2=[i*i for i in range(10) if i%2==0]
print(lis2)

print()

names=["milo","Sarah","bruno","Assistant","Rosa"]
nameWith_o=[item for item in names if "o" in item]
print(nameWith_o)

names=["milo","Sarah","bruno","Assistant","Rosa"]
nameWith_o=[item for item in names if (len(item)>4)]
print(nameWith_o)