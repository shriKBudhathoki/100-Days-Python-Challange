#Write a program to print the following star pattern
'''
***
* *
***
for n=3
'''
number=int(input("Enter a number : "))
for i in range(1,number+1):
    if(i==1 or number==i):
        print("*"*number,end="")
    else:
        print("*",end="")
        print(" "*(number-2),end="")
        print("*",end="")
    print(" ")
    
"""
The important part
if i == 1 or number == i:

The loop gives:

i = 1
i = 2
i = 3

We want:

First row → ***
Middle row → * *
Last row → ***

So:

When i = 1
i == 1

is True.

Therefore:

print("*" * number, end="")

becomes:

print("*" * 3)

Output:

***
When i = 2
i == 1

is False.

But:

number == i

is also False because:

3 == 2 → False

So the else runs:

print("*", end="")
print(" " * (number - 2), end="")
print("*", end="")

Since:

number - 2
3 - 2
= 1

it becomes:

print("*", end="")
print(" ", end="")
print("*", end="")

Giving:

* *
When i = 3

Now:

number == i

means:

3 == 3

which is True.

So:

print("*" * number, end="")

again produces:

***
Think of the logic like this
i = 1  → first row → ***
i = 2  → middle    → * *
i = 3  → last row  → ***

And this:

" " * (number - 2)

creates the empty space between the two stars.


"""
