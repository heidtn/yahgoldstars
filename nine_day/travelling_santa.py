import itertools
f = open('input.txt', 'r')
cities = []
paths = dict()
for line in f:
	city1 = line.strip().split()[0]
	city2 = line.strip().split()[2]
	paths[(city1, city2)] = int(line.strip().split()[4])
	if city1 not in cities: cities.append(city1)
	if city2 not in cities: cities.append(city2)	

best = []
bestDistance = MAX_INT
distance = 0
print cities
for permute in itertools.permutations(cities):
	
	for i in range(len(permute) - 1):
		if	
