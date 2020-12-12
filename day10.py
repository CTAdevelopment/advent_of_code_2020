data, used_voltages = [int(i) for i in open('day10text.txt', 'r').read().splitlines()], [0, 3]
data.sort()
from itertools import groupby

def determine_voltage(data, used_voltages):
    next_voltage = 0
    for input_voltage in data:
        next_voltage += 1
        dynamic_voltage = 1
        while int(data[next_voltage]) - input_voltage != dynamic_voltage and dynamic_voltage < 4:
            dynamic_voltage += 1
        else:
            used_voltages.append(dynamic_voltage)
            if next_voltage + 1 == len(data):
                print(int(used_voltages.count(1)) * int(used_voltages.count(3)))
                return

determine_voltage(data, used_voltages)

inputString = [int(i) for i in open("day10text.txt", "r").read().splitlines()]
inputString.sort()
inputString.insert(0, 0)
inputString.append(inputString[len(inputString)-1] + 3)

delta = [inputString[n]-inputString[n-1] for n in range(1, len(inputString))]
print(delta.count(1) * delta.count(3))
print(delta)
import sys

def term(n):
    if n == 1:
        return 3
    elif n == 2:
        return 4
    elif n == 3:
        return 7

x = [term(len(list(g))) for k, g in groupby(delta) if k == 1]
