# -*- coding: utf-8 -*-

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print('Original x-position: ' + str(alien_0['x_position']))

# Move the alien to the right
# Determine how far to move the alien based on its current speed

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print('New x-position: ' + str(alien_0['x_position']))

favorite_language = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
    }

print(favorite_language['sarah'])


person_dict = {
	'first_name': 'Jessi', 
	'last_name': 'lemon', 
	'age': 28, 
	'city': 'richardson',
	}
print(person_dict['first_name'])
print(person_dict['last_name'])
print(person_dict['age'])
print(person_dict['city'])


favorite_numbers = {
	'gibben': 40,
	'jason': 28,
	'bob': 39,
	'lily': 19,
	'jess': 26,
	}

# Print out favorite number for each person
print('The favorite number for Gibben is ' + str(favorite_numbers['gibben']))
print('The favorite number for Jason is ' + str(favorite_numbers['jason']))
print('The favorite number for Bob is ' + str(favorite_numbers['bob']))
print('The favorite number for Lily is ' + str(favorite_numbers['lily']))


glossary = {
	'list': 'list of values mutable',
	'and': 'check both conditions',
	'true': 'boolean value as true',
	'for': 'loop through a list',
	'print': 'print your statement out',
	'str': 'convert int to str data type', 
}

# Print out information
for term, meaning in glossary.items():
	print("The meaning of python term " + "'" + term + "'" + " is " + meaning + '.')








