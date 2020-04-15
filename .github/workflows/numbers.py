number = []#cчет числе от 0 до 20
for number in range(1,21):
    print(number)

number = []#вывод миллиона
for number in range(1,1000001):
    print(number)

number = [1,2,3,4,5,6,7,8,9,0,1000000]#поиск минимального,максимального числа и суммы чисел в миллионе
min(number)
print(min(number))
max(number)
print(max(number))
sum(number)
print(sum(number))

number = [(i+1)+i for i in range(1,21)]#вывод нечетных чисел от 1 до 20
print(number)

number = list(range(3,33,3))#вывод чисел от 3 до 30. к каждому числу прибавляеться по 3
print(number)

cub = []#возведение чисел в куб от 1 до 10 
for value in range(1,10):
    cub.append(value**3)
print(cub)

cub = [value**3 for value in  range(1,10)]#генератор кубов от 1 до 10 
print(cub)