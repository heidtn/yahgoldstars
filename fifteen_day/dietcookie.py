import re, itertools

f = open('inputs.txt')

ingreds = []
names = []

for line in f:
	line = line.strip()
	name = line.split()[0]
	names.append(name)
	items = re.findall(r'-?[0-9]+', line)
	ingreds.append([int(x) for x in items])

print ingreds

def sumweights(wts):
	total = 1 #we're going to multiply anyways
	#print "weights to test: ", wts
	for i in range(len(ingreds[0]) - 1): # - 1 for calories
		curSum = 0
		for j in range(len(ingreds)):
			if wts[j] != 0:
				curSum += wts[j]*ingreds[j][i]
		if curSum < 0: curSum = 0
		total *= curSum

	return total

def sumcals(wts):
	cals = 0
	for i in xrange(len(ingreds)):
		cals += ingreds[i][len(ingreds[0]) - 1]*wts[i]
	return cals

weights = [20, 20, 30, 30]
best = list(weights)

optimal = 0

for i in xrange(100):
	for j in xrange(100 - i):
		for k in xrange(100 - i - j):
			val = sumweights([i, j, k, 100 - i - j - k])
			if val > optimal and sumcals([i, j, k, 100 - i - j - k]) == 500:
				optimal = val
				best = [i, j, k, 100 - i - j - k]
				print "new best: ", optimal

print "done"




















