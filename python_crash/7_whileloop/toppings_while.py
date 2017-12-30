# -*- coding: utf-8 -*-

prompt = "\nPlease enter a topping for your pizza: "
prompt += "\nEnter quit when you finish. "

while True:
	message = input(prompt)
	if message == 'quit':
		break
	else:
		print("We'll add " + message.title() + " to your pizza!")

