data = open('day3.txt', 'r').read().splitlines()
step, pos, slope, intercept, end, treees = 1, 0, 3, 1, len(data[0]), 0

for i in data[1:]:
	i = i * (int((len(data) / len(i))) * 5 + 1)
	pos += 3	

	if i[pos] == '#':
		treees += 1	

	del i

print(treees)	
