data = open('day12.txt', 'r').read().splitlines()
c_direction = 'E'
positions_coordinates_1 = {
    'N' : 0,
    'E' : 0,
    'S' : 0,
    'W' : 0}

positions_coordinates_2 = {
    'N' : 0,
    'E' : 0,
    'S' : 0,
    'W' : 0}

wavepoint = {
    'N' : 1,
    'E' : 10,
    'S' : 0,
    'W' : 0}

wave_point_spot = ['N', 'E']

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

def move_ment_two(move, steps):
    global wave_point_spot
    global wavepoint

    if move in ['N', 'E', 'S', 'W']:
        wavepoint[move] += int(steps)

    if move == 'F':
        for i in wave_point_spot:
            positions_coordinates_2[i] += (int(steps) * wavepoint[i])

    if move in ['L', 'R']:
        n_spots = []
        n_wave_point  = {}
        for j in wave_point_spot:
            n_spot = rotation(move, steps, j)
            n_spots.append(n_spot)
            n_wave_point[n_spot] = wavepoint[j]

        ''' KC last note: create a new dict and del old one '''
        for k in wavepoint.keys():
            if k not in n_wave_point:
                n_wave_point[k] = wavepoint[k]

        wavepoint = n_wave_point
        wave_point_spot = n_spots

for line in data:
    move = line[0]
    steps = line[1:len(line)]
    move_ment_one(move, steps)
    move_ment_two(move, steps)

print('final cords day 12A:',positions_coordinates_1)
manhatten = (positions_coordinates_1['E'] - positions_coordinates_1['W']) + (positions_coordinates_1['S'] - positions_coordinates_1['N'])
print('manhatten distance day 12A:', manhatten)

print('final cords day 12B:',positions_coordinates_2, wavepoint)
manhatten2 = (positions_coordinates_2['E'] - positions_coordinates_2['W']) + (positions_coordinates_2['S'] - positions_coordinates_2['N'])
print('manhatten distance day 12B:', manhatten2)
