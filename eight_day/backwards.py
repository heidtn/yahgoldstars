import re
f = open('input.txt', 'r')
fullLines = 0
parseLines = 0
for line in f:
	line = line.strip()
	fullLines += len(line)
	print line, len(line)
	parseLines += len(re.escape(line)) + 2
	print re.escape(line), len(re.escape(line))

print parseLines - fullLines
