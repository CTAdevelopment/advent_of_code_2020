import numpy as np

data = open('day8.txt', 'r').read().splitlines()
row_actioned = {}

def iteration_rules(data):
    row_number = 0
    accumalation_value = 0

    for i in range(len(data)):

        if row_number != i:
            row = data[row_number]
        else:
            row = data[i]

        temp_dict = {}

        if row in row_actioned.keys() and row_number == row_actioned[row]:
            print('looping on:', accumalation_value)
            break

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

def calc_acc_value__action(att, val, count):

    print(att, val, count)

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

iteration_rules(data)
