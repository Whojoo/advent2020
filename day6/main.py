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

total_count_2 = 0

temp_dict = {}
temp_user_count = 0

for line in input_list:
    if line == '':
        for key in temp_dict:
            count = 1 if temp_dict[key] == temp_user_count else 0
            total_count_2 += count

        temp_dict = {}
        temp_user_count = 0
        continue

    temp_user_count += 1
    for char in line:
        if char in temp_dict:
            temp_dict[char] += 1
        else:
            temp_dict[char] = 1

for key in temp_dict:
    count = 1 if temp_dict[key] == temp_user_count else 0
    total_count_2 += count

print('total_count_2({})'.format(total_count_2))
