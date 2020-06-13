people = {
    'andrey': {
        'first': 'andrey',
        'last': 'izmailov',
        'location': 'kolomna',
        'age': 20,
    },
    'jura': {
        'first': 'jura',
        'last': 'Timohin',
        'location': 'kolomna',
        'age': 33,
    },
    'sveta': {
        'first': 'Svetlana',
        'last': 'Izmailova',
        'location': 'murom',
        'age': 43,
    },
}
for username, user_info in people.items():
    print("\nusername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    age = user_info['age']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
    print("\tAge: " + str(age))