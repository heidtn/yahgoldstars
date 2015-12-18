
f = open('input.txt', 'r')
fullLines = 0
parseLines = 0
for line in f:
	line = line.strip()
	fullLines += len(line)
	print line
	parseLines += len(line.decode('string_escape')) - 2
	print line.decode('string_escape') 

print fullLines - parseLines
