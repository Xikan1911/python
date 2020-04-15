name = ['fox', 'wolf', 'murlok', 'bear', 'cat', 'dog']
print("The first three items in the list are:")
for name in name[0:3]:#срез из списка начало
    print(name.title())
#Срезы из списка 
print("Three items from the middle of rhe list are:")
name = ['fox', 'wolf', 'murlok', 'bear', 'cat', 'dog']
for name in name[2:4]:#срез из серидины списка
    print(name.title())
print("The last three items in the list are:")
name = ['fox', 'wolf', 'murlok', 'bear', 'cat', 'dog']
for name in name[3:6]:#срез из конца списка
    print(name.title())



    pizza = ['peperoni', 'four_shiz', 'meat']
for i in pizza:
    print("i like " + i + " pizza")    
print("l really love pizza!")
frends_pizza = pizza[:]
pizza.append('vim')
frends_pizza.append('sir')
print("My favorit pizzas are:")
for pizza in pizza:
    print(pizza)
print("My favorit frend pizza are")
for frends_pizza in frends_pizza:
    print(frends_pizza)