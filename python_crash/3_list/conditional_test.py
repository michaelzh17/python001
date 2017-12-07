# -*- coding: utf-8 -*-

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'toyota'? I predict False")
print(car == 'toyota')

city = 'queens'
print("Is city == 'queens'? I predict True.")
print(city == 'queens')

print("\nIs city = 'brooklyn'? I predict False.")
print(city == 'brooklyn')

country = 'cuba'
print("Is country == 'cuba'? I predict True.")
print(country == 'cuba')

print("\nIs country == 'mexico'? I predict False.")
print(country == 'mexico')

food = 'sandwich'
print("Is food == 'sandwich'? I predict True.")
print(food == 'sandwich')

print("\nIs food == 'burger'? I predict False.")
print(food == 'burger')

sport = 'pingpang'
print("Is sport == 'pingpang'? I predict True.")
print(sport == 'pingpang')

print("Is sport == 'badminton'? I predict False.")
print(sport == 'badminton')
	
currency = 'US dollar'
print("currency is US dollar")
print("currency == 'US dollar' is " + str(currency == 'US dollar'))
print("currency == 'Rupee' is " + str(currency == 'Rupee'))

#testing using lower() function
district = 'Bayside'
print('district is Bayside.')
print("district.lower() == 'bayside' is  " + str(district.lower() == 'bayside'))

#test numerical equality and inequality
age = 89 
print('age = 89 is ' + str(age == 89))
print('age = 80 is ' + str(age == 80))

#testing using keyword and and or
if age > 80 and age < 100: 
	print('the person is too old!')

if age < 18 or age > 81: 
	print('the person is not in working age!')

#test whether an item is in a list or not in a list
fruit = ['apple', 'tomato', 'pear', 'fig', 'pipeapple']
print('apple in the list is ' + str('apple' in fruit))
print('peach not in the list is ' + str('peach' not in fruit))

