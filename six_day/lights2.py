SIZE = 1000

lights = [[0]*SIZE for i in xrange(SIZE)]

f = open('input.txt', 'r')


def count():
	count = 0
	for y in range(SIZE):
		for x in range(SIZE):
			count += lights[x][y]
	return count

def printLights():
	for el in lights:
		print el

for line in f:
	line = line.strip()
	els = line.split()
	if els[0] == 'toggle':
		x1 = int(els[1].split(',')[0])
		y1 = int(els[1].split(',')[1])
		x2 = int(els[3].split(',')[0])
		y2 = int(els[3].split(',')[1])
	else:	
		x1 = int(els[2].split(',')[0])
		y1 = int(els[2].split(',')[1])
		x2 = int(els[4].split(',')[0])
		y2 = int(els[4].split(',')[1])
	for x in xrange(x1, x2 + 1):
		for y in xrange(y1, y2 + 1):
			if els[0] == 'toggle':
				lights[x][y] += 2
			elif els[1] == 'on':
				lights[x][y] += 1
			else:
				lights[x][y] -= 1
				if lights[x][y] < 0: lights[x][y] = 0

print count()	
