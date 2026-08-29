#Write a program to find the sum of first natural number using while loop

number=int(input("Enter a number :"))
i=1
sum=0
while (i<=number):
    sum+=i
    i+=1
print(sum)

'''
Sure. This program calculates the sum of all natural numbers from 1 up to the number entered by the user.

For example, if you enter 5, it calculates:

1 + 2 + 3 + 4 + 5 = 15



| Loop | `i` | `sum` before | `sum += i` | `sum` after |
| ---: | --: | -----------: | ---------: | ----------: |
|    1 |   1 |            0 |      0 + 1 |           1 |
|    2 |   2 |            1 |      1 + 2 |           3 |
|    3 |   3 |            3 |      3 + 3 |           6 |
|    4 |   4 |            6 |      6 + 4 |          10 |
|    5 |   5 |           10 |     10 + 5 |          15 |


After the fifth loop:

i = 6
number = 5

Python checks:

6 <= 5

That's: False
'''
