'''
Write a program to print the following star pattern
  *
 ***
***** for n=3
'''
number=int(input("Enter a number : "))
for i in range (1,number+1):
    print(" "* (number-i),end=" ") # This creates the spaces before the stars.
    print("*"* (2*i-1),end=" ") # 2 * i - 1 is just a formula to generate odd numbers: 1, 3, 5, 7, 9...
    print("")
    
    
'''
But WHY 2*i - 1?

Because we want the stars to increase like this:

1 → 3 → 5 → 7 → 9

Each row needs 2 more stars than the previous row.

2 * i gives:

2 → 4 → 6 → 8 → 10

But we want:

1 → 3 → 5 → 7 → 9

So subtract 1:

2 → 4 → 6 → 8 → 10
 ↓
-1
 ↓
1 → 3 → 5 → 7 → 9

Therefore:

"*" * (2 * i - 1)

means:

Print an odd number of stars, increasing by 2 on every row.

'''
