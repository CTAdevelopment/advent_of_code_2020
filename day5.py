data = open('day5.txt', 'r').read().splitlines()
c_id_value, highest_id = 0, 0

def func(val):
    data_slice, col_slice = range(0, 128), range(0, 8)

    for letter in val:
        if letter == 'F':
            data_slice = data_slice[slice(0, int(len(data_slice) / 2))]
        elif letter == 'B':
            data_slice = data_slice[slice(int(len(data_slice) / 2 + 0.5), data_slice[-1])]

        if letter == 'L':
            col_slice = col_slice[slice(0, int(len(col_slice) / 2))]
        elif letter == 'R':
            col_slice = col_slice[slice(int(len(col_slice) / 2), col_slice[-1])]

        if len(data_slice) == 1:
            row_ = int(list(data_slice)[0])
        if len(col_slice) == 2 or len(col_slice) == 1:
            col_ = int(list(col_slice)[0])
            break

    return row_ * 8 + col_

for line in data:
    c_id_value = func(line)
    if c_id_value > highest_id:
        highest_id = c_id_value
