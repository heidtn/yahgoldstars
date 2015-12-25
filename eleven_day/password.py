import re


def increment(lst):
	for i in range(len(lst) - 1, 0, -1):
		lst[i] = chr(ord(lst[i]) + 1)
		if ord(lst[i]) % 123 == 1:
			lst[i] = 'a'
		else:
			return

def checklist(lst):
	if checkinc(lst) and checkbad(lst) and checkpairs(lst):
		return True
	return False

def checkinc(lst):
	for i in range(len(lst) - 3):
		if chr(ord(lst[i]) + 1) == lst[i + 1] and chr(ord(lst[i + 1]) + 1) == lst[i + 2]:
			return True
	return False

def checkbad(lst):
	if 'i' in lst or 'o' in lst or 'l' in lst:
		return False
	return True

def checkpairs(lst):
	check = ''.join(lst)
	if len(re.findall(r'(\w)\1+', check)) > 1:
		return True
	return False

f = open('inputs.txt', 'r')

password = f.readline().strip()

pw = list(password)

count = 0
if __name__ == "__main__":
	while True:
		increment(pw)
		count += 1
		if checklist(pw):
			print pw
			break
		if count % 1000 == 0:
			print count

