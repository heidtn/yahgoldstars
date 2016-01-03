regs = {}
regs['a'] = 1
regs['b'] = 0

lines = []
f = open('inputs.txt', 'r')
for line in f:
	lines.append(line.strip())

pc = 0
while pc < len(lines):
	ln = lines[pc].split(' ')
	print ln, regs, pc
	ins = ln[0]
	vals = ln[1].strip(',')

	if ins == 'hlf':
		regs[vals] /= 2
	elif ins == 'tpl':
		regs[vals] *= 3
	elif ins == 'inc':
		regs[vals] += 1
	elif ins == 'jmp':
		pc += int(vals)
		continue
	elif ins == 'jie':
		reg = vals
		offset = int(ln[2])
		if regs[reg] % 2 == 0:
			pc += offset
			continue
	elif ins == 'jio':
		reg = vals
		offset = int(ln[2])
		if regs[reg] == 1:
			pc += offset
			continue

	pc += 1

print regs