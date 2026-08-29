def mathe():
    import math

    result=math.sqrt(9)
    print(result)
    print(dir(math))
    print(math.pi,type(math.pi))
# mathe()

def sqrt():
    
    from math import sqrt as a
    result=a(9)
    print(result)

# sqrt()

def sqrt1():
    # from import math *   it is not a good practice so avoid it
    from math import sqrt,pi
    result=sqrt(9) * pi
    print(result)

# sqrt1()

def trial():
    from imp import welecom,shree
    welecom() # Cuz it is the function
    print(shree) #cuz it is the variable

trial()