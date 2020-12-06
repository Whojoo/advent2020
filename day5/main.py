def get_number(false_binary, zero_identifier):
    binary = ''
    for char in false_binary:
        corrected = '0' if char == zero_identifier else '1'
        binary = '{}{}'.format(binary, corrected)
    return int(binary, base=2)

file_input = open("input")

input_list = file_input.read().splitlines()

max_seat_id = 0

for seat in input_list:
    row = get_number(seat[:7], 'F')
    column = get_number(seat[7:], 'L')
    seat_id = row * 8 + column
    max_seat_id = max(max_seat_id, seat_id)

print('max seat_id({})'.format(max_seat_id))

seat_ids = []

for seat in input_list:
    row = get_number(seat[:7], 'F')
    column = get_number(seat[7:], 'L')
    seat_id = row * 8 + column
    seat_ids.append(seat_id)

seat_ids.sort()

target_seat_id = 0

for idx in [x for x in range(1, len(seat_ids) - 1) if x % 2 == 1]:
    first = seat_ids[idx - 1]
    second = seat_ids[idx]
    third = seat_ids[idx + 1]

    print(first, second, third)

    if third - second + first == second:
        continue
    elif third - second == 2:
        target_seat_id = second + 1
        break
    else:
        target_seat_id = first + 1
        break

print('my seat_id({})'.format(target_seat_id))