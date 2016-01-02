numbertoreach = 29000000


lst = [11]*numbertoreach
print "alloc"

for i in xrange(2, len(lst) + 1):
	if i % 1000 == 0: print i
	for j in xrange(i, min(i*50 + 1, len(lst)) + 1, i):
		lst[j - 1] += i*11

print "done populating", lst[0], lst[1], lst[2]
for i in xrange(len(lst)):
	if lst[i] > numbertoreach:
		print i + 1
		break

