# -*- coding: utf-8 -*-

pizzas = ['neapolitan', 'california', 'deep dish', 'thin crust', 'pepperoni']

for pizza in pizzas:
	print(pizza)
	print('I love ' + pizza + ' pizza!')

print('Pizza is my favorite!\n I love the cheese on it and the tomato sauce\n Pizza is fast and cute!\n I really love Pizza!!')

friend_pizzas = pizzas[:]

pizzas.append('sausage')

friend_pizzas.append('upside-down')

print('My favorite pizza are: ')
for pizza in pizzas:
	print(pizza)

print('My friend favorite pizza are: ')
for pizza in friend_pizzas:
	print(pizza)

