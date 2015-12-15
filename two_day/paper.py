
f = open('input.txt', 'r')
total = 0
for line in f:
	nums = line.strip().split('x')
	side1 = int(nums[0])*int(nums[1])
	side2 = int(nums[1])*int(nums[2])
	side3 = int(nums[2])*int(nums[0])
	smallest = min(side1, side2, side3)
	area = side1*2 + side2*2 + side3*2
	area += smallest
	print area
	total += area

print "total: ", total
