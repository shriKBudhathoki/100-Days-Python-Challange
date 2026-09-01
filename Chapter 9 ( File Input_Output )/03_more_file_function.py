'''

#This Function is used to create a list of the output
#EG ['Trial 123\n', 'I am a second line\n', 'This is amazing\n', 'Twinkle Twinkle Little Star'] <class 'list'>
f = open("File.txt")
lines=f.readline()
print(lines,type(lines))
f.close()
'''

print("\n")
# One by one line print
f = open("File.txt")

# line1=f.readline()
# print(line1,type(line1))

# line2=f.readline()
# print(line2,type(line2))

# line3=f.readline()
# print(line3,type(line3))

# line3=f.readline()
# print(line3,type(line3))

# line4=f.readline()
# print(line4,type(line4))

# line5=f.readline()
# print(line5 == "")


# Using Loop

line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()

f.close()