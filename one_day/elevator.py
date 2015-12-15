f = open('input.txt', 'r')

line = f.readline()

leftBracket = line.count('(')
rightBracket = line.count(')')

print leftBracket - rightBracket
