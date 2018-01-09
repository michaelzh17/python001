# -*- coding: utf-8 -*-

def make_shirt(size = 'large', message = 'I love Python!'):
	"""Display the size and message of the shirt"""
	print("The size of the shirt is " + size.title() + " and message on shirt is " + message + ".")


make_shirt('small', 'I love New York!')
make_shirt(size = 'medium', message = 'Happy New Year!')
make_shirt(message = 'What a snow day!', size = 'large')
make_shirt()
make_shirt('medium')
make_shirt('small', 'Python is great!')
make_shirt(message = 'Python is on the way!')
make_shirt(size = 'medium')


def describe_city(name, country = 'america'):
	"""Display city name and their country"""
	print(name.title() + " is in " + country.title())

describe_city('beijing', 'china')
describe_city('boston')
describe_city('seattle')


