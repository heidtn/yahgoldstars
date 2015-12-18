import copy

def lookandsay(lst):
	said = list()
	curCount = 1
	curNum = int(lst[0])
	index = 1
	while index < len(lst):
		if int(lst[index]) == curNum:
			curCount += 1
		else:
			said.append(int(curCount))
			said.append(int(curNum))
			curCount = 1
			curNum = int(lst[index])
		index += 1

	said.append(curCount)
	said.append(curNum)
	return said		


file = open('inputs.txt', 'r')
currentNums = list(file.readline().strip())
for i in xrange(50):
	currentNums = lookandsay(currentNums)	
	print "final: ", len(currentNums), " iter: ", i

print "length: ", len(currentNums)
