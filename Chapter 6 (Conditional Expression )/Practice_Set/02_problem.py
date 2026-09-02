"""
Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass.
Assume 3 subjects and take marks as an input from the user.


| Situation               | Formula                             |
| ----------------------- | ----------------------------------- |
| Average of 3 values     | `(a + b + c) / 3`                   |
| Marks out of 300        | `(obtained / 300) * 100`            |
| Different maximum marks | `(obtained / total_possible) * 100` |

total_percentage = ((marks1 + marks2 + marks3) / 300) * 100

"""
#/ 3 gives the average of three percentage values
#/ 300 gives a decimal fraction of the total marks To turn that fraction into a percentage, multiply by 100.

marks1=int(input("Enter a Subject marks 1 : "))
marks2=int(input("Enter a Subject marks 2 : "))
marks3=int(input("Enter a Subject marks 3 : "))

total_percentage=((marks1 + marks2 + marks3) / 300) * 100

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 ): #Because question say at least 33% in each subject to pass.
    print("You are pass :",total_percentage)
else:
    print("You are Failed,try again next year! :",total_percentage)