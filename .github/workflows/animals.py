pets = {
    'monster': {
        'vid': 'dog',
        'name': 'monster',
        'name master': 'Andrey',
    },
    'lisa': {
        'vid': 'cat',
        'name': 'lisa',
        'name master': 'Sveta',
    },
}
for pet, user_info in pets.items():
    print("\nPet: " + pet)
    vid = user_info['vid']
    name = user_info['name']
    name_master = user_info['name master']
    print("\tVid: " + vid.title())
    print("\tName: " + name.title())
    print("\tName master: " + name_master.title())