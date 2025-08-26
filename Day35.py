def looping_for():
    for i in range(5):
        print(i)
    else:
        print("no i is here") #It execute beause we dont use the break
# looping_for()

def looping_for2():
    for i in range(6):
        print(i)
        if i==3:
            break
    else:
        print("Not found") #It's not execute because we add the break and it work normally
# looping_for2()

def while_loop():
     i=0
     while i<7:
        print(i)
        i=i+1
        if i==3:
         break
     else:
      print("Not found") #It's not execute because we add the break and it work normally
# while_loop()

def algorithm():
   data=[10,20,30,40,50]
   for num in data:
      if(num==40):
       print("Found",num)
       break
      else:
       print("not found",num)
# algorithm()

def iteration():
    for x in range(5):
         print("iteration no {} in for loop".format(x + 1))
             
    else:
        print("else block in loop")
        print("Out of loop")
iteration()