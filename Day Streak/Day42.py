#Emmuerate
def Enmurate():
    list=[10,30,20,40,50,60]

    for index,i in enumerate(list,start=1):
     print(i)
    if(index==5):
        print("Jha2")
    # else:
    #     print("hello world")
# Enmurate()

def Enmurate2():
    list=[10,20,40,50,60]
    print("Before 1",list)

    index=0
    for i in list:
        print("Before 2",i)
        if (index==3):
         print("hello world")
        index+=1
Enmurate2()