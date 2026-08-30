#Write a python function to remove a given word from a list and strip it at the same time

def remo(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l=["Harry","Subham","Samaya","Tanan","Rohan"]
user=input("Enter a remove word : ")
print(remo(l,user))







'''
for item in l:

This goes through the list one item at a time.

For:

l = ["Harry", "Subham", "Samaya"]

Python does:

item = "Harry"
item = "Subham"
item = "Samaya"
4. if not(item == word):

This is checking:

"Is this item NOT equal to the word the user wants to remove?"

Suppose:

word = "Samaya"

First:

item = "Harry"

item == word
"Harry" == "Samaya"
False

not False
True

So "Harry" gets added.

Next:

item = "Subham"

"Subham" == "Samaya"
False

not False
True

Add "Subham".

Next:

item = "Samaya"

"Samaya" == "Samaya"
True

not True
False

Don't add it.

So we're basically doing:

Harry   → keep ✅
Subham  → keep ✅
Samaya  → remove ❌
5. n.append(item.strip(word))

This part is actually not what you want.

append() means:

Add something to the list.

For example:

n.append("Harry")

gives:

["Harry"]

But then you have:

'''