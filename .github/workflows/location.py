favorit_places ={
    'Andrey': ['America', 'Cupertino'],
    'Jura': ['Europa', 'Canada'],
    'Sveta': ['Aliska', 'Paris'],
}
for name, fp in favorit_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for p in fp:
        print("\t" + p.title())    
