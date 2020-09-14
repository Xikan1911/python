message = input("Какая машина вам нужна ? ")
print(message)


rest = input("На сколько человек вам нужно забранировать стол? ")
rest = int(rest)

if rest >8:
	print("\nВам надо подождать когда освободиться нужный вам стол! ")
else:
	print("\nВаш стол готов прошу к столу!")
	
	
	
	
number = input("Напишите число и я вам сказу кратно оно или нет: ")
number = int(number)

if number % 10 == 0:
	print(f"\nТвое число {number} некратное")
else:
	print(f"\nТвое число {number} кратное ")
