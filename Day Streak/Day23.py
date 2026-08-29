# List Methods
'''
append(x) → Adds a single element to the end of the list
sort() → Sorts the list in ascending order (small → big)
sort(reverse=True) → Sorts the list in descending order (big → small)
reverse() → Reverses the order of elements in the list (doesn't sort, just flips)
count(x) → Returns the number of times x appears in the list
index(x) → Returns the index of the first occurrence of x
insert(i, x) → Inserts x at index i
remove(x) → Removes the first occurrence of x
pop([i]) → Removes and returns the element at index i (last element if i not given)
clear() → Removes all elements from the list
copy() → Returns a shallow copy of the list
extend(iterable) → Adds multiple elements from another iterable to the end

'''

print("A. Demonstrate the Append Method")
list = [1, 2, 6, 5, 9, 8, 5,5,5,55]
list.append(10)  # Adds 10 at the end
print(list)      # [1, 2, 6, 5, 9, 8, 5, 10]
print()

#Demonstrate the reverse list method
print("B. Demonstrate reverse List")
list1 = ["A","B","C","D","E"] #It go to the reverse function like e d c b a
list1.reverse()
print(list1)
print()

#Demonstrate the sort method
print("C. Demonstrate the Sort Method")
sorting=[5,6,8,9,10,55,60,1,0] 
sorting.sort()# Usually it   sorting list like 1,2,3
print(sorting)
print()

print("D. Demonstrate reverse sorting")
sorting.sort(reverse=True) # Usually it reverse the sorting list like 9,8,7,6
print(sorting)
print()

#Demonstrate the index method
print("E. Demonstrate index list")
list2 =["A","B","C","D","E"]
print("The value is found on",list2.index("C")) #This define the array index of the char in the list where c is on the 2 index
print()

#Demonstrate the count method
print("F. Demonstrate count list")
print("The total no is after count",list.count(5)) #this function count to the 5 in the list method earrlier
print()

#Demonstrate the inset method
print("G. Demonstrate insert list")
list3=[10,20,30,40,50,60,70]
list3.insert(4,500) #This 4 define the index where we want ot add our 500 in the list
print(list3)
print()

#Demonstrate the extend method 
print("H. Demonstrate extend method list");print()
list4 =[500,600,700,800]
print("Before the extending",list4)
print()
m=[100,200,300,400]
print("Extending value",m);print()
list4.extend(m)     #now extending the list4 in the m
print("After the extending",list4);print() #it extend the value of the list with combining the list4 in the m 
list4.sort() #now sorting 
print("After the sorting",list4);print()

#Demonstrate the merge method
print("I. Demonstrate merge method list");print()
print("Taking the above list");print()
k=list4+m # k the new variable hold the summation of list4 and m and show 
print("This is the merging list of list4 and m",k)
print()