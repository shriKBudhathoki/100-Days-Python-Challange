#Write a python function which converts inches to cms

#Remember: 1 inch = 2.54 cm.

def inches_to_cms(a):
    cm=a*2.54
    return cm

inches=int(input("Enter inches :"))
# inches_to_cms(inches)
print(f"Inches is {inches} converted to cm is : {inches_to_cms(inches)} cm")