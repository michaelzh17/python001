# -*- coding: utf-8 -*-

# People dictionary
user_0 = {
	'fname': 'larry',
	'lname': 'page',
	'city': 'dallas',
	'age': 37,
	}
user_1 = {
	'fname': 'debby',
	'lname': 'woods',
	'city': 'new york',
	'age': 45,
	}
user_2 = {
	'fname': 'bob',
	'lname': 'adams',
	'city': 'boston',
	'age': '23', 
	}
user_list = [user_0, user_1, user_2]
print('User information: ')
for user in user_list:
	print('First Name: ' + user['fname'])
	print('Last Name: ' + user['lname'])
	print('City: ' + user['city'])
	print('Age of User: ' + str(user['age']))


# Pets dictionary

papy = {
	'kind': 'dog',
	'owner': 'ricky',
	'color': 'black',
	'age': 3,
	}

lulu = {
	'kind': 'cat',
	'owner': 'larra', 
	'color': 'brown',
	'age': 4,
	}

magie = {
	'kind': 'dog',
	'owner': 'mary',
	'color': 'white',
	'age': 5,
	}

pets = [papy, lulu, magie]
print('\n')
print('Pets information: ')
for pet in pets: 
	print('Kind of the pet: ' + pet['kind'])
	print('Owner of the pet: ' + pet['owner'])
	print('Color of the pet: ' + pet['color'])
	print('Age of the pet: ' + str(pet['age']))

# Favorite places dictionary and list
favorite_places = {
	'bob': ['philadelphia', 'king of prussia', 'atlantic city'],
	'michael': ['dallas', 'boston', 'seattle', 'san fransisco'],
	'judy': ['guangzhou', 'wuhan', 'hongkong'],
	}

# Print out people's name and their favorite places
for person, places in favorite_places.items():
	print(person.title() + "'s favorite places are: ")
	for place in places:
		print(place.title())

# Cities list and dictionary

cities = {
	'dallas': {
	    'country': 'us',
	    'population': 2000,
	    'fact': 'assassination of kennedy',
	    },
	'sydney': {
	    'country':'austrilia',
	    'population': 5000,
	    'fact': 'famous sydney opera house',
	    },
	'boston': {
	    'country': 'us',
	    'population': 3000,
	    'fact': 'havard university',
	    },
	}

for city, city_info in cities.items():
	print('\nCity name: ' + city.title())
	print('The city is in country ' + city_info['country'].title() + '.')
	print('The city has a population of ' + str(city_info['population']) + '.')
	print('One fact about the city is ' + city_info['fact'] + '.')









