# -*- coding: utf-8 -*-

def city_country(city, country):
	"""Return a dictionary of information about the city"""
	city = {'city': city, 'country': country}
	return city 

city01 = city_country('boston', 'america')
print('"' + city01['city'].title() + ', ' + city01['country'].title() + '"')

city02 = city_country('beijing', 'china')
print('"' + city02['city'].title() + ', ' + city02['country'].title() + '"')

city03 = city_country('tokyo', 'japan')
print('"' + city03['city'].title() + ', ' + city03['country'].title() + '"')

