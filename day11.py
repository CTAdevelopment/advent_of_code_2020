import pandas as pd
import sys, os
changed_seats, occupied_seats = 0, 0

def data_framing():
    if not os.path.exists('day11.xlsx'):
        data = open('day11.txt', 'r').read().splitlines()
        col_nums = list(range(0, len([i for i in data[0]])))
        frame = pd.DataFrame(columns=col_nums)
        for row in data:
            row_data = []
            for letter in row:
                row_data.append(letter)

            frame.loc[(len(frame))] = row_data
    else:
        frame = pd.read_excel('day11.xlsx', index=False)

    if os.path.exists('day11.xlsx'):
        None
    else:
        frame.to_excel('day11.xlsx', index=False)

    return frame

def search_for_all_seats(some_frame, z):
    global changed_seats
    global occupied_seats
    c = 0

    for i, j in enumerate(some_frame[z]):
        new_state_seat = human_behavior(some_frame, j, i, z)
        some_frame.at[i, z] = new_state_seat

        if new_state_seat != j:
            changed_seats += 1
            if new_state_seat == '#':
                occupied_seats += 1

        if c + 1 == len(some_frame[z]):
            if z + 1 == len(some_frame.columns) - 1:
                print('total numbers of changed seats: ', changed_seats, 'total occupied seats', occupied_seats)
                new_frame = some_frame.copy()
                search_for_all_seats(new_frame, 0)
            else:
                z += 1
                search_for_all_seats(some_frame, z)

        c += 1

def human_behavior(frame, occupation, seat_row, seat_col):
    def count_taken_chairs(frame):
        count_taken = 0
        surrounding_chairs_occupation = []

        try: surrounding_chairs_occupation.append(frame.at[seat_row-1, seat_col-1])
        except: None
        try: surrounding_chairs_occupation.append(frame.at[seat_row-1, seat_col])
        except: None
        try: surrounding_chairs_occupation.append(frame.at[seat_row-1, seat_col+1])
        except: None
        try: surrounding_chairs_occupation.append(frame.at[seat_row, seat_col-1])
        except: None
        try: surrounding_chairs_occupation.append(frame.at[seat_row, seat_col+1])
        except: None
        try: surrounding_chairs_occupation.append(frame.at[seat_row+1, seat_col-1])
        except: None
        try: surrounding_chairs_occupation.append(frame.at[seat_row+1, seat_col])
        except: None
        try: surrounding_chairs_occupation.append(frame.at[seat_row+1, seat_col+1])
        except: None

        count_taken = surrounding_chairs_occupation.count('#')

        return count_taken

    if occupation == '.':
        return '.'

    if occupation == '#':
        taken_chairs = count_taken_chairs(frame)
        if taken_chairs >= 4:
            return 'L'
        else:
            return '#'

    if occupation == 'L':
        taken_chairs = count_taken_chairs(frame)
        if taken_chairs == 0:
            return '#'
        else:
            return 'L'

frame = data_framing()
search_for_all_seats(frame, 0)
