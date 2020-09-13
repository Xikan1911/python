#7.4
toping = "\nPlease select toping for you pizza"
toping += "\n(Enter 'quit' when yuo are finished.)"

message = ""
while message != 'quit':
    message = input(toping)

    if message != 'quit':
        print(message)



#7.5
mes = "Введите возраст посетителя кинотеатра: "
mesage = ""
while mes != 'quit':
    message = input(mes)
    if message <= str(3):
        print("Билет бесплатный")
    if message <= str(12):
        print("Билет стоит 10 долларов")
    if message > str(12):
        print("Билет стоит 15 долларов")

#7.6

toping = "\nPlease select toping"
toping += "\n(Write 'quit' in exit)"

active =True
while active:
    message = input(toping)

    if message == 'quit' :
        active = False
    else:
        print(message)

#7.7

x = 1
while x <= 5:
    print(x)