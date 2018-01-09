# -*- coding: utf-8 -*-

def greet_users(names):
	"""Print a simple greeting to each user in the list"""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

usernames = ['hannah', 'ty', 'margerate']

greet_users(usernames)