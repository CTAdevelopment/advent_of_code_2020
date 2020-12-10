import sys
data = [int(i) for i in open('day9.txt', 'r').read().splitlines()]
global_pos = 0

def initiate_protocol(data, pos):
    injection, unpack = data[pos:pos+25], data[pos+25]
    while not find_weakness(injection, unpack, pos):
        pos += 1
        initiate_protocol(data, pos)

    if break_encryption(data, unpack, pos):
        sys.exit()

def find_weakness(injection, search_val, pos):
    r_injection = injection.copy()
    for number in injection:
        if int(search_val) - int(number) in r_injection: return False

    print('weakness found:', search_val, 'at pos:', pos)
    return True

def break_encryption(data, optelling, found_pos):
    search_data = data[0:found_pos].copy()
    start_pos = 0
    end_pos = 1
    total_sum = 0
    while total_sum != optelling:
        total_sum = sum(search_data[start_pos:end_pos])
        if total_sum < optelling:
            end_pos += 1
        elif total_sum > optelling:
            start_pos += 1
            end_pos = start_pos + 1
        else:
            print('found', min(search_data[start_pos:end_pos]) + max(search_data[start_pos:end_pos]))
            return True


initiate_protocol(data, global_pos)
