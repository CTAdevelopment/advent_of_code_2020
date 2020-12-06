
inputString = open('day6.txt', 'r').read().splitlines()
totalCount, currentSet, start = 0, set(), True

for line in inputString:
    if line == "":
        totalCount += len(currentSet)
        currentSet, start = set(), True
    else:
        if start:
            currentSet, start = set(line), False
        else:
            currentSet.intersection_update(set(line))
totalCount += len(currentSet)
print(totalCount)
