import re

f = open('input.txt', 'r')

goodcount = 0
for line in f:
	isgood = True
	line = line.strip()
	if len(re.findall(r'[aeiou]', line)) < 3:
		isgood = False	
	if len(re.findall(r'(\w)\1+', line)) == 0:
		isgood = False
	if len(re.findall(r'ab|cd|pq|xy', line)) > 0:
		isgood = False
	if not isgood:
		print 'bad line, ', line
	else:
		goodcount += 1

print 'goodcount: ', goodcount
	
