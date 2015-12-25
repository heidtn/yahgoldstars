import re

f = open('inputs.txt')

total = 0
for line in f:
	line = line.strip()
	nums = re.findall(r'-?[0-9]+', line)
	print nums
	for val in nums:
		total += int(val)

print total