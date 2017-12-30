# -*- coding: utf-8 -*-

responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the user's name and response
	name = input("\nWhat is your name? ")
	response = input("\nIf you could visit one place in the world, where would you go? ")
	
	# Add the reponse to the dictionary
	responses[name] = response

	# Find out if anyone else is going to take the poll.
	repeat = input("Would you like another person to take to poll? (yes/ no)")
	if repeat == 'no':
		polling_active = False

print("\n--- Polling Results ---")
for name, response in responses.items():
	print(name + " would like to visit " + response.title() + " if possible.")


