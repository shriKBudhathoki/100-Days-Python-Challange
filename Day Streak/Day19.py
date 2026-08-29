print("Normal While looping for Multiplication of 9")
print()

for i in range(12):
    if(i==10):
        break
    print("9 X", i+1, "=", 9 * (i+1))

print()
#The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.
print("Using the break statement")

for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
     print("Mississippi")
print("Thank you")

print()

#The continue statement skips the rest of the loop statements and causes the next iteration to occur.
print("Using Continue Key")

for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)

print()

#dowhile
print("Starting do-while")

i=0
while True:
    print(i) #it is because do while once print the value whether or not condition satisfied

    i=i+1

    if(i%100 ==0):
        break

'''
do{

execution statement

}condition or while loop

'''