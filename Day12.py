#Day 12 String Slicing
fruit="Mango"
fruitlen=len(fruit)
print(fruitlen)

print(fruit[0:4]) #it include 0 but not the 4 default feature (Mang)
print(fruit[0:5]) #Mango
print(fruit[1:4]) #ang
print(fruit[-3:-1]) #ng
print(fruit[-1:len(fruit)-3])  #4:2 it is impossible and ignore by the compiler

#Quick Quiz
nm="Harry"
print(nm[-4:-2])