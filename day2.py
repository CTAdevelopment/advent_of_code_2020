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
    count_start = int(first_split.split('-')[0])
    count_end = int(first_split.split('-')[1])
    letter = condition.split(' ')[1]
    counter = 0
    end = len(input)

    for i in input:
        end -= 1

        if str(letter) == str(i):
            counter += 1

        if counter > count_end:
            return False

        if end == 0:
            if counter >= count_start and counter <= count_end:
                return True
            else:
                return False

for item in data:
    if condition_met(item):
        condition_met_counter += 1


print(condition_met_counter)
