# -*- coding: utf-8 -*-

river_dict = {
	'nile': 'egypt',
	'yangtze': 'china',
	'amazon': 'brazil',
	}

for river, country in river_dict.items():
	print('The ' + river.title() + ' runs through ' + country.title() + '.')

# Print river in dictionary
print('\nRivers: ')
for river in river_dict.keys():
	print(river)

# Print country in dictionary
print('\nCountry: ')
for country in river_dict.values():
	print(country.title())

for country in sorted(river_dict.values()):
	print(country.title())

# Polling problem
favorite_language = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
    }

print('\n')

people_list = ['jen', 'sarah', 'bob', 'john', 'lily']

for person in people_list:
	if person in favorite_language.keys():
		print(person.title() + ', thanks for taking the poll!')
	if person not in favorite_language.keys():
		print('Hey ' + person.title() + ', this is an invitation to taking the poll.')









