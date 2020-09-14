#7.8
sandwich_orders = ['barbecu', 'burger', 'bif', 'shes', 'flask']
finisjed_sandwichs = []

while sandwich_orders:
    currect_sandwich = sandwich_orders.pop()

    print(f"I made yuor tina sandwich: {currect_sandwich.title()}")
    finisjed_sandwichs.append(currect_sandwich)

print("\nThe finished sandwish :")
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

    print(f"I made yuor tina sandwich: {currect_sandwich.title()}")
    finisjed_sandwichs.append(currect_sandwich)

print("\nThe finished sandwish :")
for finisjed_sandwich in finisjed_sandwichs:
    print(finisjed_sandwich.title())

#7.10

rests = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    rest = input("Where would you like to relax this summer?")
    rests[name] = rest
    repeat = input("would you like to let another person respond? (yes/ no)" )
    if repeat == 'no':
        polling_active = False
print("\n--- Pool Results ---")
for name, rest in rests.items():
    print(f"{name} would like to climb {rest}.")