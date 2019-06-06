__author__ = 'Mark'

import random
import time

########## variables for starting balance and each slot as a random number 1-7
########## asks the user if they want to play. If "y" the game starts
balance = 20
slot1 = random.randrange(1,8)
slot2 = random.randrange(1,8)
slot3 = random.randrange(1,8)
print("Welcome To The Slot Machine! Your starting balance is $20.")
choice = input("Do you want to take a spin? (y/n)")

#############The minimum balance required to keep the game going is 5 dollars.
############ Anything under 5 dollars and the game exits automatically
while balance > 5 and choice == "y" or choice == "Y":
    slot1 = random.randrange(1,8)
    slot2 = random.randrange(1,8)
    slot3 = random.randrange(1,8)
    print ("The slot machine is rolling!")
    time.sleep(1)
    print ("You rolled", slot1, slot2, slot3)

    ############ I have 3 scenarios here: If none of the slots match, if two of them match, and
    ############ if all of them match. You get payed depending on if they match or not
    if slot1 == slot2 and slot2 == slot3 and slot1 == slot3:
        balance = balance - 2
        print ("You won the jackpot! +$20")
        balance = balance + 20
        print ("Your balance is", balance)
        choice = input("Do you want to spin again? (y/n)")

    if slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
        print("You won a partial jackpot! + $2")
        print("Your balance is", balance)
        choice = input("Do you want to spin again? (y/n)")

    if slot1 != slot2 and slot2!= slot3 and slot1 != slot3:
        balance = balance - 2
        print("You lose 2 dollars!")
        print("Your balance is", balance)
        choice = input("Do you want to spin again? (y/n)")


#############if the user chooses n or something else, the program quits
if choice != "y" or choice != "Y":
    print("Thanks for playing! Come again.")

#########if the total balance is not enough to continue, the program kicks you out
if balance < 5:
    print("You don't have enough money! Goodbye.")







