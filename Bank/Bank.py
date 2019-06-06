__author__ = 'Mark'
balance = 0
choice = 1
print("To make a deposit press 1")
print("To make a withdrawal press 2")
print("To show balance press 3")
print("To quit press 4")
choice=int(input())

while choice != 4:

   if choice == 1:

        deposit = float(input("How much money do you want to deposit? "))
        balance = deposit + balance
        print("Your new balance is: ", balance)
        choice = int(input("Please make another choice"))
   if choice == 2:
       withdrawal = float(input("How much money do you want to withdraw?"))
       balance=balance-withdrawal
       print("Your new balance is: ", balance)
       choice=int(input("Please make another choice"))
   if choice == 3:
       print("Your balance is", balance)
       choice=int(input("Please make another choice"))



