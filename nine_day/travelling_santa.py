import itertools
import copy

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
bestDistance = 99999999999
distance = 0
print cities
for permute in itertools.permutations(cities):
	distance = 0
	for i in range(len(permute) - 1):
		if (permute[i], permute[i + 1]) in paths:
			pair = paths[(permute[i], permute[i + 1])]
		else:
			pair = paths[(permute[i + 1], permute[i])]
		distance += pair
	if distance < bestDistance:
		bestDistance = distance
		print permute, distance
