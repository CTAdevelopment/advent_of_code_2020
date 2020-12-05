data = open('day4.txt', 'r').read().splitlines()
str_to_check, valid  = '', 0


def func(check):
    x = [i for i in check.split(' ')]
    print(x)

    if len(x) < 7:
        return 0
    if len(x) > 7:
        return 1
    if len(x) == 7:
        boo = True
        for a in x:
            if 'cid' in a.split(':')[0]:
                return 0
        if boo:
            return 1


c = 0
for line in data:
    c += 1
    if line == '':
        valid = valid + func(str_to_check[1:len(str_to_check)])
        str_to_check = ''
    elif c == len(data):
        str_to_check = str_to_check + ' ' + line.strip()
        valid = valid + func(str_to_check[1:len(str_to_check)])
    else:
        str_to_check = str_to_check + ' ' + line.strip()



print(valid)
