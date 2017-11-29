motocycles = ['honda', 'yamaha', 'suzuki']

print(motocycles)

motocycles[0] = 'toyota'

print(motocycles)

motocycles.append('honda')
print(motocycles)

motocycles.insert(0, 'ducati')
print(motocycles)

del motocycles[0]
print(motocycles)

popped_motocycle = motocycles.pop()
print(motocycles)
print(popped_motocycle)

first_owned = motocycles.pop(2)
print(motocycles)
print(first_owned)

motocycles.remove('toyota')
print(motocycles)


