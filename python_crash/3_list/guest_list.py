guests = ['Steve Jobs', 'Walter Isaacson', 'Groot', 'Albert Einstein', 'Peter Quill', 'Scarlett Johansson']

for guest in guests:
	print('Hey, ' + guest + ' I am holding a party on Saturday. Come and enjoy!')
	
guest_absence = 'Walter Isaacson'
guests.remove(guest_absence)
print(guests)
print(guest_absence + " won't be able to come")

guests.append('Steven King')

for guest in guests:
	print('Hey, ' + guest + '. Party is still on!')
	
for guest in guests:
	print('Hey, ' + guest + ' Good news, found a bigger table. Will invite more friends!')
	
guests.insert(0, 'Jon Snow')
guests.insert(3, 'Aye Stark')
guests.append('Mike Ross')


for guest in guests:
	print('Hey ' + guest + ' Bigger table and more people. Reserve your slot!')
	

print('Hey, Sorry, I can only have two guests for the party this time')

n = len(guests)

while n > 2:
	pop_guest = guests.pop()
	n = n-1
	print('Sorry, ' + pop_guest + ' can\'t invite you this time')

print(guests)

for guest in guests:
	print('Hey, ' + guest + ' you are still invited to the party')
	
del guests[0]
del guests[0]

print(guests)

print(str(len(guests)) + ' are invited to the party!!')
	
	
	
