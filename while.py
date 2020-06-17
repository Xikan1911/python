car = "Let me see if I can find you a: "
car += "\nWhat car ? "

name = input(car)
print("\nYor car is " + name + "!")


restoran = input("Hello, how much does a person need a table?")
restoran = int(restoran)

if restoran >= 8:
    print("\nTable not yet cats need to wait!")
else:
    print("\nYour table is ready!")


number = input("You number is : ")
number = int(number)

if number % 10 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")