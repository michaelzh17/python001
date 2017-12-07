# -*- coding: utf-8 -*-

squares = []

for i in range(1, 12):
	squares.append(i**2)
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

#list comprehensions examples
count_20 = [x for x in range(1, 21)]
print(count_20)

count_1m = [x for x in range(1, 1000001)]
print(min(count_1m))
print(max(count_1m))
print(sum(count_1m))


odd_list = [x for x in range(1, 21, 2)]
for row in odd_list:
	print(row)



three_list = [x for x in range(3, 31, 3)]
for row in three_list:
	print(row)


cube_list = [x**3 for x in range(1, 11)]
for row in cube_list:
	print(row)

