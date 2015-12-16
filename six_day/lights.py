SIZE = 1000

lights = [[False]*SIZE for i in xrange(SIZE)]

f = open('input.txt', 'r')


def count():
	count = 0
	for y in range(SIZE):
		for x in range(SIZE):
			if lights[x][y] == True:
				count += 1
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
				lights[x][y] = not lights[x][y]
			elif els[1] == 'on':
				lights[x][y] = True
			else:
				lights[x][y] = False

print count()	
