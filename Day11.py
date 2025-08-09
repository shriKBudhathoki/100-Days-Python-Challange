'''Day 11 where Studying of for loop/array/printing'''

name="Harry"
name2="Shree Krishna Budhathoki"
friend="donkey"


#Sause : you can't use double """" on same statement if u want use ' " "  '
apple=f'Hello World "welecome our master " {name2} 000\n' 


#The representaion of print all no of line like a paragrpah and show as you give]

apple2='''Hey newcommers
hi new Substraction
how was your Day
it is good 
\n
'''

print(apple)
print() #Making New Line Make Attractive
print(apple2)


#printing char of name also py is same as array but not exact array
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
#print(name[5]) it throw the program because harry have only 4 index but program go to 5 so program crash
print()


#looping 

for character in friend:
  print (character)