def check(checker, num_list, start_idx, end_idx):
    if start_idx > end_idx:
        return -1

    idx_range = end_idx - start_idx
    target_idx = start_idx + int(idx_range / 2)

    if idx_range <= 1:
        target_idx = start_idx

    target = num_list[target_idx]
    total = checker + target

    if total == 2020:
        print('YAY, answer is {} x {} = {}'.format(checker, target, checker * target))
        return target
    elif total > 2020:
        return check(checker, num_list, start_idx, target_idx - 1)
    else:
        return check(checker, num_list, target_idx + 1, end_idx)

file_input = open("input")

input_list = file_input.read().splitlines()
num_list = list(map(lambda str: int(str), input_list))
num_list.sort()
print(num_list)

for num in num_list:
    if check(num, num_list, 0, len(num_list) - 1) > -1:
        print('Found it')
        break

for idx1 in range(len(num_list)):
    num1 = num_list[idx1]
    for idx2 in range(idx1 + 1, len(num_list)):
        num2 = num_list[idx2]
        if num1 + num2 >= 2020 - num2:
            break
        sliced_list = num_list[idx2:]
        num3 = check(num1 + num2, sliced_list, 0, len(sliced_list) - 1)
        if num3 > -1:
            print('Found it, {} x {} x {} = {}'.format(num1, num2, num3, num1 * num2 * num3))
