import itertools

f = open('inputs.txt', 'r')

bottles = []

for line in f:
	bottles.append(int(line.strip()))

bottles.sort()

mincons = len(bottles)
count = 0

for i in xrange(len(bottles)):
	for comb in itertools.combinations(bottles, i):
		if sum(comb) == 150: 
			if len(comb) < mincons:
				count = 1
				mincons = len(comb)
			elif len(comb) == mincons:
				count += 1

print mincons, count



