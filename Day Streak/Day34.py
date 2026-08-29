def update_clear():
    #Remember set is unordered and dictionary is ordered
    ep1={122:45,123:89,567:69,670:69}
    ep2={222:67,566:90}
    ep1.update(ep2) #It update the ep2 in the ep1
    #ep1.clear() #It clear the whole dictionary data and give {}
    print(ep1)

    #update_clear() #function calling.......


def pop_popitems():
    list={101:224,102:5001,103:500,104:100,105:5000,106:800,107:8001}
    # list.pop(106) #specific key value removed
    list.popitem() #last key value removed
    print(list)
#pop_popitems()

def delvar_delkey():
     list={101:224,102:5001,103:500,104:100,105:5000,106:800,107:8001}
     print("Before del key",list)
     #del list #delete all list and throw the error
     del list[101]
     print("After del key",list)
delvar_delkey()
