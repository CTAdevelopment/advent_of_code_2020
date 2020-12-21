inputString = [13,16,0,12,15,1]

def playMemory(target):
    memory = {i : inputString.index(i) for i in inputString[:-1]}
    lastNumber = inputString[-1]
    for turn in range(len(inputString)-1, target-1):
        currNumber = turn - memory[lastNumber] if lastNumber in memory.keys() else 0
        memory[lastNumber] = turn
        lastNumber = currNumber
    print(lastNumber)

playMemory(2020)
playMemory(30000000)
