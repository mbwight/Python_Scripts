__author__ = 'Mark'
print ("Welcome to the Calculator Program!")
one = 0
two = 0
choice = 0
restart = "y"
def addition(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def multiplication(x,y):
    return x * y
def division(x,y):
    return x / y
while restart == "y":
    one = float(input("Enter A Number: "))
    choice = input("Please Enter A Command: +,-,*,/")
    two = float(input("Enter Another Number: "))
    
    if choice == "+":
        print ("The numbers", one, "and", two,  "added to", addition(one,two))
        restart = input("Do you want to do it again? (y/n)")
    if choice == "-":
        print ("The difference of", one, "and", two, "is", subtraction(one,two))
        restart = input("Do you want to do it again? (y/n)")

    if choice == "*":
        print ("The product of", one, "and",  two, "is", multiplication(one,two))
        restart = input("Do you want to do it again? (y/n)")

    if choice == "/":
        print ("The quotient of", one, "and", two, "is", division(one,two))
        restart = input("Do you want to do it again? (y/n)")


else:
    print("Goodbye.")


