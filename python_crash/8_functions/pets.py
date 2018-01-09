# -*- coding: utf-8 -*-

def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet('harry', 'hamster')
describe_pet(pet_name = 'harry', animal_type = 'hamster')


def describe_pet_dog(pet_name, animal_type = 'dog'):
	"""Display information about a pet."""
	print("\nI have a " + animal_type +".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet_dog('Willie')
describe_pet_dog('willie', 'cat')
describe_pet_dog('cat')

# A dog named Willie
describe_pet_dog('willie')
describe_pet_dog(pet_name = 'willie')

# A hamster named Harry.
describe_pet_dog('harry', 'hamster')
describe_pet_dog(pet_name = 'harry', animal_type = 'hamster')
describe_pet_dog(animal_type = 'hamster', pet_name = 'harry')

describe_pet_dog()







