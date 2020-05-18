car = 'dmw'
print("car == 'dmw' ? True")
print(car == 'dmw')

name = 'Andrey'
if name != 'Jura' :
    print("Name is Jura!")

car = 'audio'
print("car.lower() == 'Audio ? False")
print(car.lower() == 'Audio')

car = 'Audio'
print("car.lower() == 'audio' ? True")
print(car.lower() == 'audio')
#Use "<,>,=,<=,>=,==" for check
age = 32
if age != 20:
    print("No age corect!")

age = 19
print("age < 21 ? True")
print(age < 21)
age = 21
print(age <= 17)
age = 21
print(age >= 27)
age = 21
print(age == 21)
#Use "AND" for check
age_0 = 21
age_1 = 31
print(age_0 <= 20 and age_1 >=21)#False 
age_0 = 21
age_1 = 30
print((age_0 >= 19) and (age_1 >= 29))#True
#Use "OR" for check
age_0 = 17
age_1 = 20
print((age_0 <= 10) or (age_1 <= 24))#True
age_0 = 20
age_1 = 27
print((age_0 >= 30) or (age_1 <= 25))#False

games = ['warcraft', 'sky', 'diablo', 'doom']#check in spisok
print('warcraft' in games )#True
print('heartstone' in games)#False

love_games = ['warcraft', 'heartstone', 'diablo']
game = 'skyrim'#check in not spisok

if game not  in love_games:
    print(game.title() + ",my not love game")