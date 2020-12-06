file_input = open("input")

input_list = file_input.read().splitlines()

temp_list = list()

counts = []

for line in input_list:
    if line == '':
        counts.append(len(set(temp_list)))
        temp_list = list()
        continue

    temp_list = temp_list + list(line)

counts.append(len(set(temp_list)))

total_count = 0
for count in counts:
    total_count += count

print('total_count({})'.format(total_count))
