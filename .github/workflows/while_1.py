#7.4
toping = "\nПожалуйста, выбирети топинг для совей пиццы"
toping += "\n(Напишите 'quit'когда ваш выбор будет свделан чтобы закончить .)"

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

toping = "\nВыбирети топинг для пиццы"
toping += "\n(Напишите 'quit'чтобы занкочить )"

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
