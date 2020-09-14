#7.8
sandwich_orders = ['barbecu', 'burger', 'bif', 'shes', 'flask']
finisjed_sandwichs = []

while sandwich_orders:
    currect_sandwich = sandwich_orders.pop()

    print(f"Я могу приготовить вот такие сендвичи: {currect_sandwich.title()}")
    finisjed_sandwichs.append(currect_sandwich)

print("\nЭти седвичи готовы :")
for finisjed_sandwich in finisjed_sandwichs:
    print(finisjed_sandwich.title())
#7.9

sandwich_orders = ['barbecu', 'burger','pastrami', 'bif', 'shes', 'pastrami', 'flask', 'pastrami']
finisjed_sandwichs = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

while sandwich_orders:
    currect_sandwich = sandwich_orders.pop()

    print(f"Эти сендвичи я могу приготовить: {currect_sandwich.title()}")
    finisjed_sandwichs.append(currect_sandwich)

print("\nЭти сендвичи готовы :")
for finisjed_sandwich in finisjed_sandwichs:
    print(finisjed_sandwich.title())

#7.10

rests = {}
polling_active = True

while polling_active:
    name = input("\nКак тебя зовут? ")
    rest = input("В каком городе ты бы хотел отдохнуть этим летом? ")
    rests[name] = rest
    repeat = input("Ты бы хотле продолжить оброс или нет ? (да/ нет)" )
    if repeat == 'нет':
        polling_active = False
print("\n--- Pool Results ---")
for name, rest in rests.items():
    print(f"{name} ты хотел бы отдохнуть в городе: {rest}.")
