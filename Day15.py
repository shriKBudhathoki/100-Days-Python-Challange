#Exercise By time say good morning,afternoon,goodnight
import time

timestamp=time.strftime('%H:%M:%S')
print(timestamp)

hour=int(time.strftime('%H'))

Minute=int(time.strftime('%M'))

second=int(time.strftime('%S'))


print()

if hour<12:
    print("Good Morning,Srikrishna")
    
elif hour<17:
    print("Good Afternoon,Srikrishna")

else:
    print("Good Night,Srikrishna")

print()

if Minute==30:
    print(f"It is{hour} Half Hour:",Minute)

elif Minute==45:
    print=(f"It is three-quarters of an hour {hour}:",Minute)

else:
    print(f"Minute is {hour}:",Minute)