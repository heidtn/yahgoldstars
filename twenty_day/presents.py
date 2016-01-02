numbertoreach = 29000000

seed = 289000
cursum = 0
best = 0

"""
while cursum < numbertoreach:
	cursum = 0
	cursum += seed*10	
	for i in xrange(1, seed/2 + 1):
		if seed % i == 0:
			cursum += i*10
	seed += 1
	if cursum > best:
		best = cursum
		print best
	if seed % 1000 == 0:
		print seed, cursum

print seed - 1
"""

lst = [10]*numbertoreach
print "alloc"

for i in xrange(2, len(lst) + 1):
	if i % 1000 == 0: print i
	for j in xrange(i, len(lst) + 1, i):
		lst[j - 1] += i*10

print "done populating"
for i in xrange(len(lst)):
	if lst[i] > numbertoreach:
		print i + 1, lst[i]
		break

