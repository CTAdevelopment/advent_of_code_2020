import re
data = open('day4.txt', 'r').read().splitlines()
str_to_check, valid  = '', 0

def conditions(val):
    cond = val.split(':')[0]
    info = val.split(':')[1]

    if cond == 'byr':
        if len(info) == 4 and int(info) >= 1920 and int(info) <= 2002:
            return 1
    elif cond == 'iyr':
        if len(info) == 4 and int(info) >= 2010 and int(info) <= 2020:
            return 1
    elif cond == 'eyr':
        if len(info) == 4 and int(info) >= 2020 and int(info) <= 2030:
            return 1
    elif cond == 'hgt':
        if info[-2:] == 'cm':
            check_ = int(info[0:len(info) - 2])
            if check_ >= 150 and check_ <= 193:
                return 1
        if info[-2:] == 'in':
            check_ = int(info[0:len(info) - 2])
            if check_ >= 59 and check_ <= 76:
                return 1
    elif cond == 'hcl':
        if re.match('#{1}[0-9|a-z]{6}$', info):
            return 1
    elif cond == 'ecl':
        if info in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return 1
    elif cond == 'pid':
        if re.match('[0-9]{8}[0-9]{1}$', info):
            return 1
    elif cond == 'cid':
        return 1

    return 0

def func(check):
    x = [i for i in check.split(' ')]
    all_valid = 0

    if len(x) < 7:
        return 0

    if len(x) == 8:
        for b in x:
            all_valid = all_valid + conditions(b)

        if all_valid == 8:
            return 1
        else:
            return 0

    if len(x) == 7:
        for a in x:
            if 'cid' in a.split(':')[0]:
                return 0

            all_valid = all_valid + conditions(a)

        if all_valid == 7:
            return 1
        else:
            return 0

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
