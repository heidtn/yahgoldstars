import md5

secretkey = 'yzbqklnj'
hashout = ''
val = 0
while not hashout.startswith('00000'):
	string = "" + secretkey + str(val)
	print string
	hashout = md5.new(secretkey + str(val)).hexdigest()
	val += 1

print (secretkey + str(val - 1))
print hashout
print val	
