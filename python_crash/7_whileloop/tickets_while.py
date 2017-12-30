# -*- coding: utf-8 -*-

prompt = "\nPlease enter your age (Enter quit to quit the program): "

while True:
	age = input(prompt)
	if age == 'quit':
		break
	else:
		age = int(age)
		if age >= 0 and age <= 3:
			print("The cost of the movie ticket is free.")
		elif age > 3 and age < 12:
			print("The cost of the movie ticket is $10.")
		elif age >= 12:
			print("The cost of the movie ticket is $15.")
		else:
			print("Please enter a valid age. ç")


# Active flag version

prompt = "\nPlease enter your age (Enter quit to quit the program) - flag version: "

active = True

while active:
	age = input(prompt)
	if age == 'quit':
		active = False
	else:
		age = int(age)
		if age >= 0 and age <= 3:
			print("The cost of the movie ticket is free.")
		elif age > 3 and age < 12:
			print("The cost of the movie ticket is $10.")
		elif age >= 12:
			print("The cost of the movie ticket is $15.")
		else:
			print("Please enter a valid age. ç")