data, used_voltages = [int(i) for i in open('day10.txt', 'r').read().splitlines()], [1, 3]
data.sort()

def determine_voltage_clean(data, used_voltages):
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

determine_voltage_clean(data, used_voltages)
