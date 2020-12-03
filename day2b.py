import pandas as pd
import numpy as np
import sys

path = 'day2.txt'
file = open(path, 'r+')
data = file.read().splitlines()
condition_met_counter = 0

def condition_met(item):
    qualification = False
    condition = item.split(':')[0].strip()
    input = item.split(':')[1].strip()
    qualification = check_condition(condition, input)
    #print(qualification, condition, input)

    return qualification

def check_condition(condition, input):
    first_split = condition.split(' ')[0]
    cond_1 = int(first_split.split('-')[0])
    cond_2 = int(first_split.split('-')[1])
    letter = condition.split(' ')[1]
    counter = 0
    end = len(input)

    for i in input:

        counter += 1

        if counter == cond_1:
            if i == letter:
                a = True
            else:
                a = False
        if counter == cond_2:
            if i == letter:
                b = True
            else:
                b = False

            end = 0
        
        if a and b:
            return False

        if end == 0:
            if a and not b:
                return True
            elif b and not a:
                return True
            elif b and a:
                return False
            elif not b and not a:
                return False
            else:
                print('error pos undefined')
                return None

for item in data:
    if condition_met(item):
        condition_met_counter += 1


print(condition_met_counter)
