import sys
data = open('day9.txt', 'r').read().splitlines()
global_pos = 0

def initiate_protocol(data, pos):
    injection, unpack = data[pos:pos+25], data[pos+25]
    while not find_weakness(injection, unpack, pos):
        pos += 1
        initiate_protocol(data, pos)

    break_encryption(data, unpack, pos)

def find_weakness(injection, search_val, pos):
    r_injection = injection.copy()
    for number in injection:
        if str(int(search_val) - int(number)) in r_injection: return False

    print('weakness found:', search_val, 'at pos:', pos)
    return True

def break_encryption(data, search_val, found_pos):
    search_data = data[0:found_pos].copy()
    c_val = 0
    dyn_search_val = int(search_data[c_val])
    used_codes_to_decrypt = [int(search_data[c_val])]
    hacked = False

    while not hacked:

        for i in range(len(search_data) - 1):

            if (c_val + 1 + i) > (len(search_data) - 1):
                break
            elif int(dyn_search_val) + int(search_data[c_val + i]) != search_val:
                used_codes_to_decrypt.append(int(search_data[c_val + i]))
                dyn_search_val += int(search_data[c_val + i])
                continue
            else:
                print('hack_found')
                hacked = True
                print(min(used_codes_to_decrypt) + max(used_codes_to_decrypt))
                sys.exit()

        c_val += 1

        try:
            dyn_search_val = int(search_data[c_val])
        except:
            print(c_val, 'error')
            sys.exit()

        used_codes_to_decrypt = [dyn_search_val]


    print('stop')
    sys.exit()

initiate_protocol(data, global_pos)
