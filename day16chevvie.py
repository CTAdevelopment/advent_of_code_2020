params = open('ticket_params.txt', 'r').read().splitlines()
lines = open('tickets.txt', 'r').read().splitlines()


def part_One(params, lines):
    sum=0
    global kaassouffle
    kaassouffle = {
        i.split(':')[0] : [ range(int(i.split(':')[1].split(' or ')[0].split('-')[0]), int(i.split(':')[1].split(' or ')[0].split('-')[1]) + 1 ),
                            range(int(i.split(':')[1].split(' or ')[1].split('-')[0]), int(i.split(':')[1].split(' or ')[1].split('-')[1]) + 1 ) ]
                            for i in params
                }

    valid_ids = lines[:]

    for line in lines:
        for ticket in [int(i) for i in line.split(',')]:
            max_ranges = len(kaassouffle.values())
            boo = False
            for ranges in kaassouffle.values():
                for r in ranges:
                    if ticket in r:
                        boo = True
                        break

                max_ranges -= 1
                if max_ranges == 0 and not boo:
                    valid_ids.remove(line)
                    sum += ticket


    print(sum)
    return valid_ids

valid_ids = part_One(params, lines)
print(len(lines))
print(len(valid_ids))

def define_order_params(valid_ids_1):

    kroket = {i : 0 for i in kaassouffle.keys()}
    print(kroket)

    for parameter in [int(i) for i in valid_ids_1.split(',')]:

        for idx, ranges in kaassouffle.items():
            if parameter in ranges[0] or parameter in ranges[1]:
                if kroket[idx] == 0 and valid_ids_1.index(str(parameter)) not in kroket.values():
                    kroket[idx] = valid_ids_1.index(str(parameter))



    print(kroket)


define_order_params(valid_ids[0])
