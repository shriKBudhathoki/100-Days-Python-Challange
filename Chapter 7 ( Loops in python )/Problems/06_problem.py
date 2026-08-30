#Write a program to calculate the factorial of a given number using for loop

# 5!=1 X 2 X 3 X 4 X 5

number=int(input("Enter a Number :"))
Product=1
for i in range(1,number+1): # Because we need to 2,3,4,5 not 2,3,4
    Product=Product*i
    # Multiply the previous product by i
print(f"Factorial Number {number} :  {Product}")

'''
| Loop     | `i` | Calculation | `Product` |
| -------- | --: | ----------- | --------: |
| Starting |   — | —           |         1 |
| 1st      |   1 | `1 X 1`     |         1 |
| 2nd      |   2 | `1 X 2`     |         2 |
| 3rd      |   3 | `2 X 3`     |         6 |
| 4th      |   4 | `6 X 4`     |        24 |
| 5th      |   5 | `24 X 5`    |       120 |


'''
