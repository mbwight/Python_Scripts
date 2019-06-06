__author__ = 'Mark'
print("Welcome to the Healthy Food Shop!")

#all of the values for the food items multiplied by amount user inputs
potato = int(input("Please enter how many potatoes you would like to buy ($0.75 per potato):")) * .75
tomato = int(input("Please enter how many tomatoes you would like to buy ($1.25 per tomato):")) * 1.25
apple = int(input("Please enter how many apples you would like to buy ($0.5 per apple):")) * .5
mango = int(input("Please enter how many mangoes you would like to buy ($1.75 per mango):")) * 1.75

#######the total value of the items
total = potato + tomato + apple + mango
print("Your total is $", '%.2f' % (total))

#######all of the values for pay amount and change
pay = input("Please enter the amount you are paying")
pay = float(pay)
ten = 0
five = 0
one = 0
quarter = 0
penny = 0
dime = 0
nickel = 0
change = 0

#####this portion asks for more money if user doesnt supply sufficient funds in input/pay
while pay < total:
    print("You still owe me money! Please add more money")
    pay = pay + float(input())
#########this section of code calculates the denominations of change dispursed to the user
if pay > total:
    change = (pay - total) + .001

    if change >= 10:
        ten = change // 10
        change = change % 10
        print(int(ten),"ten dollar bill(s)", end=",")

    if change >= 5:
        five = change // 5
        change = change % 5
        print(int(five), "five dollar bill(s)", end=",")

    if change >= 1:
        one = change // 1
        change = change % 1
        print (int(one), "one dollar bill(s)", end=",")
    if change >= .25:
        quarter = change // .25
        change = change % .25
        print (int(quarter), "quarter(s)", end=",")
    if change >= .10:
        dime = change / .10
        change = change % .10
        print (int(dime), "dime(s)", end=",")
    if change >= .05 and change < .10:
        nickel = change // .05
        change = change % .05
        print (int(nickel), "nickel(s)" , end=",")
    if change > 0:
        penny = change / .01
        change = change % .01
    if penny > 1:
        print (int(penny), "penny(ies)", end=", ")

    print ("is your change. Have a nice day!")
#######if change is exact, program ends
if pay == total:
    print("Thank You, Have A Nice Day!")
