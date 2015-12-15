
f = open('input.txt', 'r')
line = f.readline().strip()
houses = []
x = 0
y = 0
houses.append((x, y))
for direction in line:
	if direction is '>':
		x += 1
	elif direction is '<':
		x -= 1
	elif direction is '^':
		y += 1
	elif direction is 'v':
		y -= 1
	if (x, y) not in houses:
		houses.append((x, y))

print 'num houses: ', len(houses)
	
