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

    kroket = {i : [0, 0] for i in kaassouffle.keys()}
    found_ticket_locations = []

    for ticket in [int(i) for i in valid_ids_1.split(',')]:
        ticket_ind = valid_ids_1.index(str(ticket))

        for id, values in kaassouffle.items():
            if ticket in values[0] or ticket in values[1]:
                if kroket[id][0] == ticket_ind:
                    continue
                else:
                    kroket[id] = ticket_ind, ticket
                    found_ticket_locations.append(ticket)
                    print(ticket)

        if ticket == valid_ids_1[-1]:
            temp_list = []

            while len(found_ticket_locations) != len(valid_ids_1.split(',')):
                for id in [int(i) for i in valid_ids_1.split(',')]:
                    id_index = valid_ids_1.index(str(id))
                    if id not in found_ticket_locations:
                        print('id not found in kroket:',id)
                        for idx, valuesx in kaassouffle.items():
                            if id in valuesx[0] or id in valuesx[1]:
                                found_ticket_locations.append(id)
                                temp_list.append(kroket[idx])
                                found_ticket_locations.remove(kroket[idx][1])
                                kroket[idx] = id_index, id
                                continue

                if len(temp_list) > 0:
                    for i in temp_list:
                        ticket_ind = i[0]
                        ticket_ = i[1]
                        for idx, valuesx in kaassouffle.items():
                            if ticket_ in valuesx[0] or ticket_ in valuesx[1] and kroket[idx][0] == 0:
                                kroket[idx] = ticket_ind, ticket_
                                continue

    print(kroket)





define_order_params(valid_ids[0])
