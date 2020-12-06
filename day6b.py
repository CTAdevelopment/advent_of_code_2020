data = open('day6.txt', 'r').read().splitlines()
c, sum, new_ =  0, 0, True

for line in data:

	if line == '':
		new_ = True
		sum = sum + len(list(a))

	if c + 1 == len(data):
		a.intersection_update(line)
		if a:
			sum = sum + len(list(a))

	if new_ == True:
		a = set(line)
		new = Falseii
	else:
		a.intersection_update(line)
		print(a)

	c += 1

print(sum)
