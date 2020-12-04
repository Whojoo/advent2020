def check(checker, num_list, start_idx, end_idx):
    if start_idx > end_idx:
        return False

    idx_range = end_idx - start_idx
    target_idx = start_idx + int(idx_range / 2)

    if idx_range <= 1:
        target_idx = start_idx

    target = num_list[target_idx]
    total = checker + target
    # print('start_idx({}) end_idx({}) target_idx({}) total({})'.format(
    #     start_idx, end_idx, target_idx, total))

    if total == 2020:
        print('YAY, answer is {} x {} = {}'.format(checker, target, checker * target))
        return True
    elif total > 2020:
        return check(checker, num_list, start_idx, target_idx - 1)
    else:
        return check(checker, num_list, target_idx + 1, end_idx)



file_input = open("input")
items = 200

input_list = file_input.read().splitlines()
num_list = list(map(lambda str: int(str), input_list))
num_list.sort()
print(num_list)

for num in num_list:
    if check(num, num_list, 0, 199):
        print('Found it')
        break
