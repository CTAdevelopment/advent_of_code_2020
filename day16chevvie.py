params = open('ticket_params.txt', 'r').read().splitlines()
lines = open('tickets.txt', 'r').read().splitlines()
sum=0

kaassouffle = {
    i.split(':')[0] : [ range(int(i.split(':')[1].split(' or ')[0].split('-')[0]), int(i.split(':')[1].split(' or ')[0].split('-')[1]) + 0 ),
                        range(int(i.split(':')[1].split(' or ')[1].split('-')[0]), int(i.split(':')[1].split(' or ')[1].split('-')[1]) + 0 ) ]
                        for i in params
            }


for line in lines:
    for ticket in [int(i) for i in line.split(',')]:
        for ranges in kaassouffle.values():
            for range in ranges:
                if ticket not in range and range == ranges[-1]:
                    sum += ticket

print(sum)
