# -*- coding: utf-8 -*-

rental_car = input("What kind of car do you want? ")
print("Let me see if I can find you a " + rental_car + ".")


seat_num = input("How many people are in your dinner group? ")
seat_num = int(seat_num)

if seat_num > 8:
	print("Sorry. You will need to wait for a table.")
else:
	print("Your table is ready.")


number = input("Please input a number: ")
number = int(number)

if number % 10 == 0:
	print(str(number) + " is a multiple of 10.")
else:
	print(str(number) + " is not a multiple of 10.")