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
