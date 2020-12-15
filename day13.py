data = open('day13.txt', 'r').read().splitlines()
pref_departure_time = int(data[0])
bus_lines = [int(i) for i in data[1].split(',') if i != 'x']
all_departure_times = {}
import time

nu = time.time_ns()

for bus in bus_lines:
    bus_departure_times = [i for i in list(range(0, pref_departure_time + 60, bus)) if i > pref_departure_time]
    if bus_departure_times:
        all_departure_times[bus] = min(bus_departure_times)

print( min(all_departure_times, key=all_departure_times.get) * (min(all_departure_times.values()) - pref_departure_time) )
print( (time.time_ns() - nu) / 1000000 )

{int(x) - (int(inputString[0]) % int(x)): int(x) for x in inputString[1].split(",") if x != "x"}

def partOne():
    timeTable = {int(x) - (int(inputString[0]) % int(x)): int(x) for x in inputString[1].split(",") if x != "x"}
    print(min(timeTable.keys()) * timeTable[min(timeTable.keys())])
