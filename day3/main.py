
def move(x, y, slope, lanes, lane_length):
    if y >= lanes:
        return 0

    trees = move(x + 3, y + 1, slope, lanes, lane_length)

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

print('trees {}'.format(move(0, 0, slope, lanes, lane_length)))
