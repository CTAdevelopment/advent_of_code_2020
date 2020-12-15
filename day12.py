data = open('day12.txt', 'r').read().splitlines()
c_direction = 'E'
import matplotlib
from matplotlib import pyplot as plt

positions_coordinates_1 = {
    'N' : 0,
    'E' : 0,
    'S' : 0,
    'W' : 0}


translations = {"N": [0, 1], "E": [1, 0], "S": [0, -1], "W": [-1, 0]}

def rotation(left_right, degrees, c_direction):
    if left_right == 'L':
        if c_direction == 'N':
            if degrees == '90':
                new_direction = 'W'
            elif degrees == '180':
                new_direction = 'S'
            elif degrees == '270':
                new_direction = 'E'
        elif c_direction == 'E':
            if degrees == '90':
                new_direction = 'N'
            elif degrees == '180':
                new_direction = 'W'
            elif degrees == '270':
                new_direction = 'S'
        elif c_direction == 'S':
            if degrees == '90':
                new_direction = 'E'
            elif degrees == '180':
                new_direction = 'N'
            elif degrees == '270':
                new_direction = 'W'
        elif c_direction == 'W':
            if degrees == '90':
                new_direction = 'S'
            elif degrees == '180':
                new_direction = 'E'
            elif degrees == '270':
                new_direction = 'N'
    if left_right == 'R':
        if c_direction == 'N':
            if degrees == '90':
                new_direction = 'E'
            elif degrees == '180':
                new_direction = 'S'
            elif degrees == '270':
                new_direction = 'W'
        elif c_direction == 'E':
            if degrees == '90':
                new_direction = 'S'
            elif degrees == '180':
                new_direction = 'W'
            elif degrees == '270':
                new_direction = 'N'
        elif c_direction == 'S':
            if degrees == '90':
                new_direction = 'W'
            elif degrees == '180':
                new_direction = 'N'
            elif degrees == '270':
                new_direction = 'E'
        elif c_direction == 'W':
            if degrees == '90':
                new_direction = 'N'
            elif degrees == '180':
                new_direction = 'E'
            elif degrees == '270':
                new_direction = 'S'

    return new_direction

def move_ment_one(move, steps):
    global c_direction
    if move in ['N', 'E', 'S', 'W']:
        positions_coordinates_1[move] += int(steps)
    if move == 'F':
        positions_coordinates_1[c_direction] += int(steps)
    if move in ['L', 'R']:
        c_direction = rotation(move, steps, c_direction)

def move_ment_two():
    x, y, wayX, wayY = 0, 0, 10, 1

    for line in data:
        move = line[0]
        steps = line[1:len(line)]

        if move in ['N', 'E', 'S', 'W']:
            wayX += translations[move][0] * int(steps)
            wayY += translations[move][1] * int(steps)

        if move == 'F':
            x += (int(steps) * wayX)
            y += (int(steps) * wayY)

        if move in ['L', 'R']:
            if move == 'L':
                for i in range(0, int(int(steps) / 90)):
                    newX, newY = -wayY, wayX
                    wayX, wayY = newX, newY
            elif move == 'R':
                for i in range(0, int(int(steps) / 90)):
                    newX, newY = wayY, -wayX
                    wayX, wayY = newX, newY

    print(abs(x) + abs(y))

for line in data:
    move = line[0]
    steps = line[1:len(line)]
    move_ment_one(move, steps)


print('final cords day 12A:',positions_coordinates_1)
manhatten = (positions_coordinates_1['E'] - positions_coordinates_1['W']) + (positions_coordinates_1['S'] - positions_coordinates_1['N'])
print('manhatten distance day 12A:', manhatten)

move_ment_two()
