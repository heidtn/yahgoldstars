import re, itertools

f = open('inputs.txt')

ingreds = []
names = []

for line in f:
	line = line.strip()
	name = line.split()[0]
	names.append(name)
	items = re.findall(r'-?[0-9]+', line)[:-1]
	ingreds.append([int(x) for x in items])

print ingreds

def sumweights(wts):
	total = 1 #we're going to multiply anyways
	#print "weights to test: ", wts
	for i in range(len(ingreds[0])):
		curSum = 0
		for j in range(len(ingreds)):
			if wts[j] != 0:
				curSum += wts[j]*ingreds[j][i]
		#print curSum
		if curSum < 0: curSum = 0
		total *= curSum

	#print total
	return total


weights = [20, 20, 30, 30]
best = list(weights)

optimal = 0

"""
while True:
	for i in range(len(weights)):
		test = list(weights)
		test[i] += 1
		if sumweights(test) > optimal:
			optimal = sumweights(test)
			best = list(test)
	if weights == best:
		print "solved!"
		print weights
		break
	weights = list(best)
"""

"""
while True:
	betterThisTime = False
	for i in range(len(weights)):
		test = list(weights)
		test[i] += 1
		if test[i] == 100: next
		for j in range(len(weights)):
			if j != i:
				test[j] -= 1
				if test[j] < 0: next
				if sumweights(test) > optimal:
					optimal = sumweights(test)
					best = list(test)
					betterThisTime = True
					print "new best: ", optimal
	if not betterThisTime:
		print "solved!"
		print weights, sumweights(weights)
		break
	weights = list(best)
"""

for i in xrange(100):
	for j in xrange(100 - i):
		for k in xrange(100 - i - j):
			val = sumweights([i, j, k, 100 - i - j - k])
			if val > optimal:
				optimal = val
				best = [i, j, k, 100 - i - j - k]
				print "new best: ", optimal

print "done"




















