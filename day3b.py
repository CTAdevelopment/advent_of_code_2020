data = open('day3.txt', 'r').read().splitlines()
a = 1
z = [
		[1,1], [3, 1], [5, 1], [7, 1], [1, 2]
	]

def function(rechts, beneden):
	pos, trees = 0, 0
	for i in data[beneden::beneden]:
		i = i * (int((len(data) / len(i))) * 10 + 1)
		pos += rechts

		if i[pos] == '#':
			trees += 1

	return trees

for x, y in z:
	a = a * function(x, y)

print(a)
