# -*- coding: utf-8 -*-


def show_magicians(magician_list):
	"""Show the name of each magician in the list"""
	for magician in magician_list:
		print(magician.title())


def make_great(magician_list, great_magician):
	"""Make each magician great"""
	for i in range(len(magician_list)):
		magician_list[i] = "The Great " + magician_list[i]
		great_magician.append(magician_list[i])


magician_list = ['great gatesby', 'david kopola', 'phbee buffee']
great_magician = []
make_great(magician_list[:], great_magician)
show_magicians(magician_list)
show_magicians(great_magician)