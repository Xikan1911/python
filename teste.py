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