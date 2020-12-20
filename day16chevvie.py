params = open('ticket_params.txt', 'r').read().splitlines()
lines = open('tickets.txt', 'r').read().splitlines()

sum=0

kaassouffle = {i.split(':')[0] : list(range(int(i.split(':')[1].split(' or ')[0].split('-')[0]), int(i.split(':')[1].split(' or ')[0].split('-')[1]))) + list(range(int(i.split(':')[1].split(' or ')[1].split('-')[0]), int(i.split(':')[1].split(' or ')[1].split('-')[1]))) for i in params }
for line in lines:
    for ticket in [int(i) for i in line.split(',')]:
        if ticket in kaassouffle.values():
            print(ticket)
            sum += ticket


print(kaassouffle.values())
print(sum)
