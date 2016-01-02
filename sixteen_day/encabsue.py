import re

sues = []

f = open('inputs.txt', 'r')

for line in f:
	thissue = dict()
	thissue['issue'] = 'yes'
	thissue['num'] = line[line.find(" "):line.find(":")]
	line = line[line.find(':') + 2:].strip()
	items = line.split(',')
	for i in items:
		thissue[i.split(': ')[0].strip(' ')]= int(i.split(': ')[1])
	sues.append(thissue)

g = open('knownfacts.txt', 'r')

knowns = dict()
for line in g:
	i = line.strip()
	knowns[i.split(': ')[0].strip(' ')] = int(i.split(': ')[1])

print knowns
count = 0

for i, sue in enumerate(sues):
	for fact in knowns:
		if fact in sue:
			count += 1
			if fact == 'cats' or fact == 'trees':
				if knowns[fact] >= sue[fact]:
					sues[i]['issue'] = 'no'
			elif fact == 'pomeranians' or fact == 'goldfish':
				if knowns[fact] <= sue[fact]:
					sues[i]['issue'] = 'no'
			elif knowns[fact] != sue[fact]:
				sues[i]['issue'] = 'no'
				break


for sue in sues:
	if sue['issue'] == 'yes':
		print sue