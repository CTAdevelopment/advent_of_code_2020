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

def map_ticket_to_params(tickets):

    kroket = {i : [] for i in kaassouffle.keys()}
    found_ticket_locations = []

    for ticket in tickets:
        ticket_ind = tickets.index(ticket)

        for id, values in kaassouffle.items():
            if ticket in values[0] or ticket in values[1]:
                kroket[id].append(ticket_ind)
                continue

    return kroket

def all_options(valid_ids):
    all_options = []
    for id in valid_ids:
        unique_ticket_row = tickets_with_unique_values(id)

        if unique_ticket_row:
            possibilities = map_ticket_to_params(unique_ticket_row)
            all_options.append(possibilities)

    return all_options

def determine_order_of_params(all_options):
    unfit_params = {k : [] for k in kaassouffle.keys()}

    for option in all_options:
        for key, val in option.items():
            for i in range(20):
                if i not in val and i not in unfit_params[key]:
                    unfit_params[key].append(i + 1)


    return unfit_params

def legit_options(unfit_params):
    legit_options = {k : [] for k in kaassouffle.keys()}

    for key, val in unfit_params.items():
        for i in range(1, 21):
            if i not in val and i not in legit_options[key]:
                legit_options[key].append(i)

    return legit_options

def final_options(possible_order, unfit_params):

    for key, val in possible_order.items():
        return


    pass
    return the_truth


valid_ids = part_One(params, lines)
all_options = all_options(valid_ids)
unfit_params = determine_order_of_params(all_options)
possible_order = legit_options(unfit_params)
print(possible_order)
print('..............')
print(unfit_params)
