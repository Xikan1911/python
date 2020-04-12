name = ['mam', 'dad', 'grandma']
for i in name:
    print("Пригласительный билет для " + i)
    
no_exit = 'mam'
name.remove(no_exit)
print(name)
print("Она " + no_exit.title() + " заболела")

name.append('grandpa')
print(name)

for i in name:
    print("Пригласительный билет для 4 " + i)

name.insert(0, 'cat')
print(name)

name.insert(2, 'dog')
name.append('fox')
print(name)

for i in name: #
    print("Приглашение на обед " + i)

for i in name:
    print("На обед можно пригласить только двух " + i)

no_com = name.pop(0)
print('Стол не смог придти ' + no_com.title() + '.')

no_com = name.pop(2)
print('Стол не смог придти ' + no_com.title() + '.')

no_com = name.pop(3)
print('Стол не смог придти ' + no_com.title() + '.')

no_com = name.pop(1)
print('Стол не смог придти ' + no_com.title() + '.')

for i in name:
	print('Приглашение на обед еще в силе ' + i + '.')

del name[0]
print(name)

del name[0]
print(name)

print(name)
