#Methdes or Function of py

#knowing the length

a="Computer"
print(len(a)) 
print()

#uppercase all
print(a.upper())
print()

#lowercase all
print(a.lower())
print()

#demonstrate of strip()
b=" Shree Krishna Budhathoki "
print(b.strip()) #It simpily remove the lead and tailing unwantd spaces in output
print()

#demonstrate of rstrip()
c="!!! Welcome to my channel !!!"
print(c.rstrip("!!!")) #It only remove the specific symbol or character from tailing not leading point
print()

#demonstrate of replace()
print(a.replace("Computer","Personal Computer")) #It replace Computer to Personal Computer
print()

#demonstrate of split()
demo="shree Krishna Budhathoki"
print(demo.split(" ")) #It make the list after the space is comes in demo
print()

#demonstrate of capatillize() [It only support in py no it the js]
blog="welecome to my channel it is the represesntation OF the Our New Product"
print(blog.capitalize()) #Simply, It is used to make W in capital and OF & O,N,P make lower it prioty W than others
print()


#demonstrate of center()
blogs="Welecome to my channel" #object

print(blogs.center(50)) #length we create
print(len(blogs))       #actual length of sentences
print(len(blogs.center(50)))  #length of the blogs after we create
print()

#demonstrate of count()
print("Demonstrate of Count Using line no 26")
print(demo.count("s")) 
print()

#demonstrate of endswith()
print("demonstrate of endswith")
print(len(demo))
print(demo.endswith("sh",9,11)) #it include space and remove the one index at end string slicing 
print()

#demonstrate of find() and index()
print("Demonstration of find")
print(demo.find("o"))
print(demo.index("o")) #It give error when value not match if value match it simply run as it is
print()


#demonstration of isalnum() & isalpha
print("Demonstrate of isalnum() & isalpha")
str1="WelecomToMyChannel0"
str2="Welecom"
print(str1.isalnum()) #isalnum take A-Z,a-z,0-9
print(str2.isalpha())   #isalpha take A-Z,a-z
print()

#demonstrate islower & isupper()
print("Demonstrate of islower & isupper")

up="WELCOME"
do="welcome"
print(up.isupper())
print(do.islower())
print()

#demonstrate isprintable()==> It take all string characters 

print("Demonstrate of isprintable")
str="This is the representation of printable"
str4="This is the representation of printable\n"
print(str.isprintable())
print(str4.isprintable()) #It use \n which in not a printable format
print()


#demonstrate islower & isspace()

print("Demonstrate of isspace()")
trial="             " #using tab
trial1="            "#using spacebar
print(trial.isspace())
print(trial1.isspace())
print()

#demonstrate istile()

print("Demonstrate of istitle")
try2="It Was Big Big World"
try1="It was big big world"
print(try2.istitle())
print(try1.istitle()) #False because It order doesnot match the requirement
print()

#demonstrate startswith()

print("Demonstrate of startwith()")
i="Mohan is a good boy"
print(i.startswith("good")) #False cuz good is not start form the sentence
print(i.startswith("Mohan"))
print()

#demonstration of swapcase()


print("Demonstrate of swapcase")
l="kathmandu,prabhu"
u="BABARMAHAL,KATHMANDU,PRABHU"

print(l.swapcase())
print(u.swapcase())
print()

#demonstration of title()

print("Demonstraction of title")
p="shree krishna budhathoki"
print(p.title()) #It capatilize the space item


