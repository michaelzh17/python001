# -*- coding: utf-8 -*-

users = ['admin', 'user01', 'michael', 'bob', 'qa']

#users = []
if users:	
	for user in users:
		if user == 'admin':
			print('Hello ' + user + ', would you like to see a status report?')
		else:
			print('Hello ' + user + ', thank you for logging in again.')
else:
	print('We need to find some users!')


current_users = ['user01', 'user02', 'michael', 'bob', 'nancy', 'qa_test']
new_users = ['user03', 'user04', 'lily', 'john', 'qa_test']

if new_users:
	for user in new_users:
		if user.lower() in current_users:
			print('Please enter a new username.')
		else:
			print('OK. This username is available.')
else:
	print('There is no new user name.')


#Ordinal Numbers

num_lst = list(range(1, 10))
print(num_lst)
#loop through list to print out ordinal number
for number in num_lst:
	if number == 1:
		print('1st')
	if number == 2:
		print('2nd')
	if number == 3:
		print('3rd')
	elif number != 1 and number != 2: 
		print(str(number) + 'th')










