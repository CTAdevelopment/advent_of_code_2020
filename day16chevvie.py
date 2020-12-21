params = open('ticket_params.txt', 'r').read().splitlines()
lines = open('tickets.txt', 'r').read().splitlines()
sum=0

kaassouffle = {
    i.split(':')[0] : [ range(int(i.split(':')[1].split(' or ')[0].split('-')[0]), int(i.split(':')[1].split(' or ')[0].split('-')[1]) + 1 ),
                        range(int(i.split(':')[1].split(' or ')[1].split('-')[0]), int(i.split(':')[1].split(' or ')[1].split('-')[1]) + 1 ) ]
                        for i in params
            }

print(kaassouffle)

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
                sum += ticket

print(sum)
