import itertools

f = open('inputs.txt', 'r')

bottles = []

for line in f:
	bottles.append(int(line.strip()))

bottles.sort()

total = 0
for i in xrange(len(bottles)):
	for comb in itertools.combinations(bottles, i):
		if sum(comb) == 150: total += 1

print total
