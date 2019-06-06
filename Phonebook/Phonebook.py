__author__ = 'Mark'

menu = ["1. Add New Entry", "2. Change the phone number for a person", "3. Delete an entry"
        , "4. Display entire list", "5. Exit"]
phonebook = {}


choice = ""
for i in menu:
        print(i)
while choice != '5':

    choice = input("Hello! Welcome to the number store. Please choose an option")

    if choice == '1':
        newname = input("Please enter the name of your new entry: ")
        newnumber = input("Enter his/her number: ")
        newentry = phonebook[newname] = newnumber
        print("Here is the updated phonebook: ", phonebook)
        for i in menu:
            print (i)
        choice = input("Choose another option")
    if choice == '2':
        namechange = input("Whose number do you want to change?")
        numberchange = input("What do you want their new number to be?")

        for i in phonebook:
            if i == namechange:
                phonebook[i] = numberchange

        print("Here is the updated list: ", phonebook)
        for i in menu:
            print(i)
        choice = input("Choose another option")

    if choice == '3':
        deleteentry = input("Which entry do you want to delete?")
        if deleteentry not in phonebook:
            print("This isn't in the phonebook!")
            for i in menu:
                print (i)
                choice = input("Choose another option")
        for i in phonebook:
            if i == deleteentry:
                phonebook.pop(deleteentry)
            print("Here is the updated phonebook: ", phonebook)

            for i in menu:
                print (i)
            choice = input("Choose another option")
    if choice == '4':
        print(phonebook)
        for i in menu:
            print (i)
        choice = input("Choose another option")
if choice == '5':
    print("Goodbye!")






