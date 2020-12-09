import sys
data = open('day9.txt', 'r').read().splitlines()
global_pos = 0

def initiate_protocol(data, pos):
    injection, unpack = data[pos:pos+25], data[pos+25]
    while not find_weakness(injection, unpack, pos): pos += 1
        initiate_protocol(data, pos)

def find_weakness(injection, search_val, pos):
    r_injection = injection.copy()
    for number in injection:
        if str(int(search_val) - int(number)) in r_injection: return False

    print('weakness found', search_val)
    sys.exit()

initiate_protocol(data, global_pos)
