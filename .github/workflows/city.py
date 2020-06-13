cities = {
	'Murom':{
		'country': 'Russian',
		'population': 100000,
		'fact': 'ilua muromesh',
	},
	'Kolomna':{
		'country': 'Moscow',
		'population': 400000,
		'fact': 'over old'
	},
	'Cupertino':{
		'country': 'USA',
		'population': 1000000,
		'fact': 'comp.Apple',
	},
}
for city, user_info in cities.items():
	print("\nCity: " + city)
	country = user_info['country']
	population = user_info['population']
	fact = user_info['fact']
	print("\tCountry" + " " + country.title())
	print("\tPopulation" + " " + str(population))
	print("\tFact" + " " + fact.title())
