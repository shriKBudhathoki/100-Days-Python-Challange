"""
A spam comment is defined as a text containing following keywords:
"Make a lot of money", "buy now", "subscribe this", "click this".
Write a program to detect these spams.

"""

# GPT Version if we want to detect specific word
"""
FOR every keyword
       ↓
   Is it spam?
       ↓
      YES
       ↓
   Show keyword
       ↓
      BREAK
       ↓
  Stop searching
"""
print("Version 1")
spam_comment=["make a lot of money", "Buy now", "subscribe this", "click this"]
comment=input("Enter a comment : ").lower()
for word in spam_comment:
    if word.lower() in comment: 
     print(f"Alert Spam detected :'{word}'")
     break
else:
    print(comment)

print("\n")


# GPT Version if we don't want to detect specific word
print("Version 2")
spam_comment=["make a lot of money", "buy now", "subscribe this", "click this"]
comment=input("Enter a comment : ").lower()
for word in spam_comment:
    if word.lower() in comment: 
        print(f"Alert Spam detected : {comment}")
        break
    else:
        print(comment)
print("\n")

#Harry bhai
print("Version 3")
p1="make a lot of money"
p2="buy now"
p3="subscribe this" 
p4="click this"
message=input("Enter a comment :")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print(f"This Comment is spam : {message}")
else:
    print("This comment is not a spam")
    
print("\n")