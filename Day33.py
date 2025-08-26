#Dictionaries

#accesing single values

dic={
    12: "Shree Krishna",
    13 :"Krishna",
    14 :"Ramesh",
}
num=int(input("enter a id :"))
print(dic[num])

#accesing multiple values

info={'name': 'Karan', 'age':19, 'eligible': True}
print(info)
print(info['name']) #It is used for access the coresponding element of name
print(info.get('name')) #It is used for access the coresponding element of name

#what if
# print(info['name2']) #This throw the error and interrut the process

print(info.get('name2')) #This throw error and give NONE in the statement

print(info.keys())
print(info.values())

#Using iteration
for key in info.keys():
    print(info[key])
    print(f"The value corresponding to the key {key} is{info[key]}")
# for i in info.values():
#     print(info[i])

def new_func():
    info={'name':'Ram',"age":19,"address":"Newroad"} # Key:value
    print(info.items()) 
    for key,value in info.items():
        print(f"The corresponding value of {key} is {value}")
        
new_func()
