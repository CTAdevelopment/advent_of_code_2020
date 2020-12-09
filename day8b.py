import sys

data = open('day8.txt', 'r').read().splitlines()
row_actioned = {}
pos_list = []
original_data_set = data.copy()

def iteration_rules(data):
    row_number = 0
    accumalation_value = 0
    row_actioned = {}

    for i in range(len(data) + 1):

        if row_number != i:
            row = data[row_number]
        else:
            row = data[i]

        temp_dict = {}

        if row in row_actioned.keys() and row_number == row_actioned[row]:
            print('looping on:', accumalation_value)
            return False

        row_actioned[row] = row_number

        action_att = row.split(' ')[0]
        action_val = row.split(' ')[1][0]
        action_count = row.split(' ')[1][1:len(row.split(' ')[1])]

        temp_dict = calc_acc_value__action(action_att, action_val, action_count)

        if temp_dict['acc']:
            accumalation_value += temp_dict['val']

        if temp_dict['jump']:
            row_number += temp_dict['val']
        else:
            row_number += 1

        if row_number == len(data):
            print('set has been repaired with current dataset and accumalation_value of:', accumalation_value)
            return True

def calc_acc_value__action(att, val, count):

    #print(att, val, count)

    def pls_mn(x, y):
        if x == '-':
            return int(y) * -1
        elif val == '+':
            return int(y)

    if att == 'nop':
        return {'acc': False, 'val': 0, 'count' : 1, 'jump' : False}

    if att == 'acc':
        val = pls_mn(val, count)
        return {'acc': True, 'val': val, 'count' : 1, 'jump' : False}

    if att == 'jmp':
        val = pls_mn(val, count)
        return {'acc': False, 'val': val, 'count' : val, 'jump' : True}

def change_data_set(data):
    pos = 0
    global pos_list

    for i in data:
        attr = i.split(' ')[0]

        if attr == 'jmp' and pos not in pos_list:
            data[pos] = 'nop' + ' ' + i[len(attr) + 1:len(i)]
            print('changed:: ', i ,' to', data[pos], pos)
            pos_list.append(pos)
            return data

        if attr == 'nop' and pos not in pos_list:
            data[pos] = 'jmp' + ' ' + i[len(attr) + 1:len(i)]
            print('changed:: ', i ,' to', data[pos], pos)
            pos_list.append(pos)
            return data

        pos += 1

    print('lekker bezig man')
    sys.exit()

print('length of data: ', len(data))

while not iteration_rules(original_data_set):
    original_data_set = change_data_set(data.copy())
    print(original_data_set)
