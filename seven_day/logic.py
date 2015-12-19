import struct

f = open('inputs.txt', 'r')

vals = dict()

lines = []
for line in f:
	lines.append(line)

while len(lines) > 0:
	for i, line in enumerate(lines):
		line = line.strip()
		left = line.split("->")[0]
		val = line.split("->")[1]
		leftparts = left.split()
		try:
			if len(leftparts) == 1:
				vals[val.strip()] = int(left.strip())	
			elif leftparts[0] == "NOT":
				number = int(vals[leftparts[1]])
				vals[val] = struct.unpack('H', struct.pack('h', ~number))[0]
			elif leftparts[1] == "AND":
				number1 = int(vals[leftparts[0]])
				number2 = int(vals[leftparts[2]])
				output = struct.unpack('H', struct.pack('h', number1&number2))[0]
				vals[val] = int(output)	
			elif leftparts[1] == "OR":
				number1 = int(vals[leftparts[0]])
				number2 = int(vals[leftparts[2]])
				output = struct.unpack('H', struct.pack('h', number1|number2))[0]
				vals[val] = int(output)	
			elif leftparts[1] == "LSHIFT":
				number1 = int(vals[leftparts[0]])
				number2 = int(leftparts[2])
				output = struct.unpack('H', struct.pack('h', number1<<number2))[0]
				vals[val] = int(output)	
			elif leftparts[1] == "RSHIFT":
				number1 = int(vals[leftparts[0]])
				number2 = int(leftparts[2])
				output = struct.unpack('H', struct.pack('h', number1>>number2))[0]
				vals[val] = int(output)	
			
			del lines[i]
			print vals
		except (KeyError, ValueError):
			pass
		
print vals['a']
		
