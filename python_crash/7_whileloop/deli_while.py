# -*- coding: utf-8 -*-

sandwich_orders = ['bacon', 'pastrami', 'bagel toast', 'bauru', 'pastrami', 
 'cheese steak', 'pastrami']

print("The deli has run out of pastrami...")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

finished_sandwich = []

while sandwich_orders:
	cook_order = sandwich_orders.pop()

	print("I have made your " + cook_order + ' sandwich')

	finished_sandwich.append(cook_order)


print("Sandwich I have made: ")

for sandwich in finished_sandwich:
	if sandwich != 'pastrami': 
	    print(sandwich)



