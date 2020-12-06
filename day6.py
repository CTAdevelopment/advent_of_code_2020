data = open('day6.txt', 'r').read().splitlines()
group_data, c, sum = [], 0, 0

def uniqueList(x):
	return list(dict.fromkeys(x)) #Remove all duplicates from list[]

for line in data:

    if line == '':
        sum = sum + len(uniqueList(group_data))
        group_data = []
    if c + 1 == len(data):
        group_data.extend(line)
        sum = sum + len(uniqueList(group_data))
    else:
        group_data.extend(line)

    c += 1

print(sum)
