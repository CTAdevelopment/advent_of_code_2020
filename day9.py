import sys
data = open('day9.txt', 'r').read().splitlines()
global_pos = 0

def initiate_protocol(data, pos):
    injection = data[pos:pos+25]
    unpack = data[pos+25]

    while not find_weakness(injection, unpack, pos):
        pos += 1
        initiate_protocol(data, pos)

def find_weakness(injection, search_val, pos):
    r_injection = injection.copy()

    print('....................................')
    print('finding new spot for measurement....', search_val, 'pos:', pos)
    print(r_injection)

    for number in injection:
        if str(int(search_val) - int(number)) in r_injection:
            print('program shows no weakness on', search_val)
            return False

    print('weakness found', search_val)
    sys.exit()

initiate_protocol(data, global_pos)
