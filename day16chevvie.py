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

def tickets_with_unique_values(id):

    unsorted_tickets = [int(i) for i in id.split(',')]
    temp = dict.fromkeys(unsorted_tickets)

    if len(unsorted_tickets) == len(list(temp.keys())):
        return unsorted_tickets
    else:
        return None

def ticket_indexation_possibilities(valid_ids):
    kroket = {i : [] for i in kaassouffle.keys()}

    for id in valid_ids:
        ticket_row = tickets_with_unique_values(id)
        if not ticket_row:
            continue

        for ticket in ticket_row:

            ticket_ind = ticket_row.index(ticket)

            for id, values in kaassouffle.items():
                if ticket in values[0] or ticket in values[1]:
                    if ticket_ind not in kroket[id]:
                        kroket[id].append(ticket_ind)
                        continue
                elif ticket_ind in kroket[id]:
                    kroket[id].remove(ticket_ind)

    return kroket


valid_ids = part_One(params, lines)
ticket_mogelijkheden = ticket_indexation_possibilities(valid_ids[0:3])

for i, j in ticket_mogelijkheden.items():
    print(len(j), i)

print(ticket_mogelijkheden)
