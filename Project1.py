#while looping

#Taking the user input
acc_num=9847394866
pin=300689
balance=1000
user=int(input("Enter your Account number: "))
if(user==acc_num):
    apin=int(input("Enter Transaction pin: "))

    if(apin==pin):
     while True:
         c =int(input("Enter no 1 deposit,2 withdrawn,3 Balance check 4 exit:"))
   
         match c:
            case 1:
             bala=int(input("Enter your deposit amount: "))
             balance=balance+bala
             print("Net Balance: ",balance)
            case 2:
             bala1=int(input("Enter your Withdrawl Money: "))
             uapin=int(input("Enter your Transaction Pin: "))
             if(uapin==pin):
                 if balance-bala1<200:
                    print("sorry rs.200 is hold") 
                      

                 else:
                    balance=balance-bala1
                    print("Sucessfully Withdrawn", bala1)
        
             else:
                    print("Transaction number is incorrect")

            case 3:
                 print("The net Balance is",balance)

            case 4:
                 print("Thankyou for using our service")
                 break
            case _:
                 print("invalid input")

    else:
        print("Transaction number is incorrect")

    
else:
    print("Please Enter Valid A/C Number")














