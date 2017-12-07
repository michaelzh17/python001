# -*- coding: utf-8 -*-

age = 13

if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")

age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10

print("Your admission cost is $" + str(price) + '.')

#If you want only one block of code to run, use an if-elif-else chain
# if more than one block of code needs to run, use a series of independent if statements

