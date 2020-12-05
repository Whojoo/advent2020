
def move(x, y, slope, lanes, lane_length, move_x, move_y):
    if y >= lanes:
        return 0

    trees = move(x + move_x, y + move_y, slope, lanes, lane_length, move_x, move_y)

    corrected_x = x % lane_length
    if slope[y][corrected_x] == '#':
        trees += 1
    return trees



file_input = open("input")

input_list = file_input.read().splitlines()

lanes = len(input_list)
lane_length = len(input_list[0])
slope = []

for idx in range(lanes):
    slope.append([])
    lane = input_list[idx]
    for character in lane:
        slope[idx].append(character)

move_1_1 = move(0, 0, slope, lanes, lane_length, 1, 1)
move_3_1 = move(0, 0, slope, lanes, lane_length, 3, 1)
move_5_1 = move(0, 0, slope, lanes, lane_length, 5, 1)
move_7_1 = move(0, 0, slope, lanes, lane_length, 7, 1)
move_1_2 = move(0, 0, slope, lanes, lane_length, 1, 2)

print('move_1_1({})'.format(move_1_1))
print('move_3_1({})'.format(move_3_1))
print('move_5_1({})'.format(move_5_1))
print('move_7_1({})'.format(move_7_1))
print('move_1_2({})'.format(move_1_2))
print('multiplied({})'.format(move_1_1 * move_3_1 * move_5_1 * move_7_1 * move_1_2))
