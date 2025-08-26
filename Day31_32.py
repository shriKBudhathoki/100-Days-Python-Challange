#Sets

#Try to create an empty set. Check using the type() function whether the type of your 

shree=set()
print(type(shree))

#Alway's remember shree={} is dict type and we need to clarify set() to make type set

s={2,3,2,3,6}
print(s)

info={"ram",10,20,False,True,True,10.5}
print(info)

for value in info:
    print(value)

print("Set Methods 1. Union")

num1={5,10,20,40,35,30}
num2={15,5,25,35,30}
print("Before the Union",num1,num2) ;print()

tr=(num1.union(num2)) #This include the num2 part also and remove the duplicate entries

# print(sorted(tr)) #This sorted the items as the list like 5,10,15,20

print("After Making Union",tr);print()

num1.update(num2) #Updating the num1 like adding num2 properties in num1

print()

print("After the Update num2 properties",num1,num2)
print()

print("Set Method 2. Intersection & update")

cities={"Kathmandu","Bhakatapur","Kavre","Janakpur"}
cities2={"Nepalgung","Jhapa","Kathmandu","Kavre"}
cities3=cities.intersection(cities2)
print("Insertion",cities3)
cities.intersection_update(cities2)
print("Insertion-Update",cities3)

cities= {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 ={"Tokyo", "Seoul", "Kabul","Madrid"} 
cities3=cities.symmetric_difference(cities2)
print("Symetric Difference",cities3)


cities= {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 ={"Tokyo", "Seoul", "Kabul","Madrid"} 
cities.symmetric_difference_update(cities2)
print("Symetric Difference update",cities)


#💡 Key point: .difference() removes only exact matches (case- and spelling-sensitive).
# Original sets
set1 = {"apple", "banana", "cherry", "date"}
set2 = {"banana", "date", "fig", "grape"}

# Using difference()
result = set1.difference(set2)
print("Using difference():", result)
print("set1 after difference():", set1)  # original remains unchanged

# Using difference_update()
set1.difference_update(set2)
print("Using difference_update():", set1)  # original set1 is now changed


print("Method for isdisjoint operation")

cities= {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 ={"Tokyo", "Seoul", "Kabul","Madrid"} 
print("Disjoint",cities.isdisjoint(cities2)) #Disjoint is false because there is the common in the set


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"} #It returns True if all the items are present, else it returns False.
print(cities.issuperset (cities2))
cities3 = {"Tokyo", "Madrid", "Delhi"}
print(cities. issuperset (cities3)) # It returns True if all the items are present
print(cities3.issubset(cities)) #if all the items of the original set are present in the particular set. 

print("Add Method")
Asia={"Nepal","India","Jhapan","Korea","Austrilia"}
# Asia.add("Bhutan","Bangaladesh")  wrong Method

Asia.add("Bhutan")
Asia.add("Bangaladesh") #Using add function it support only one value
print(Asia)

Asia.update(["Korea","Tokyo"]) #Using Update Function to push multiple value 
print(Asia)

print("Remove/discard Methods")

name={"Shree","Krishna","MD","Anas","Ansari"}
name.remove("Shree")
print("before",name)
name.remove('MD')
#name.remove("Unish") This is not in the list so it throw error and not give propr run the program
name.discard("unish") #This dont throw the error in the system 
print(name)

print()

print("POP Method")
cities ={"Tokyo","Mardid","Berlin","Delhi"}
item = cities.pop() # Nobody assumed that which value gonna be poped 
print(cities)
print(item)

print("Del Method")
cities ={"Tokyo","Mardid","Berlin","Delhi"}
#del cities #Throw error if print
cities.clear() #It clear the whole set and give empty set
print(cities)


print("Check if items exits")
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
 print("Carla is present.")
else:
 print("Carla is absent.")







'''
Theory...

symmetric_difference() → returns a new set (original unchanged)
symmetric_difference_update() → updates the original set

IV. difference() and difference_update():

The difference() and difference update() methods prints only items that are only present in the original set and not in both the sets.
The difference mathod returns a new set whereas difference_update method updates into the existing set from another set.


Using difference(): {'cherry', 'apple'}
set1 after difference(): {'apple', 'banana', 'cherry', 'date'}

Using difference_update(): {'cherry', 'apple'}


difference()        = "Show me what's different, but don't touch my stuff"
difference_update() = "Remove the common stuff from me directly"


| Method            | Use For                   |
| ----------------- | ------------------------- |
|  .add(x)          | Adding **1 item only**    |
|  .update([x, y])  | Adding **multiple items** |


'''