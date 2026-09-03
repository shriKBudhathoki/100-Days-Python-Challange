# Repeat Program 4 for a list of such words to be censored

Rough_words=["Makabhosada Aag","Bsdk","Gandi","Rand"]

with open("P5.txt","r") as file:
    content=file.read()
for word in Rough_words:
    content=content.replace(word,"#" * len(word))
with open("P5.txt","w") as file:
    file.write(content)

