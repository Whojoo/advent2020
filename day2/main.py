import re

pattern = re.compile(r'(?P<Min>\d+)-(?P<Max>\d+) (?P<Letter>\w): (?P<Password>\w*)')

file_input = open("input")

input_list = file_input.read().splitlines()

valid = 0
total = len(input_list)

for line in input_list:
    search = pattern.search(line)
    groupdict = search.groupdict()

    min_req = int(groupdict['Min'])
    max_req = int(groupdict['Max'])
    letter = groupdict['Letter']
    password = groupdict['Password']

    occurrences = password.count(letter)

    if occurrences >= min_req and occurrences <= max_req:
        valid += 1

print('total({}) valid({})'.format(total, valid))

valid2 = 0

for line in input_list:
    search = pattern.search(line)
    groupdict = search.groupdict()

    first_pos = int(groupdict['Min'])
    second_pos = int(groupdict['Max'])
    letter = groupdict['Letter']
    password = groupdict['Password']

    first_letter = line[first_pos + 1]
    second_letter = line[second_pos + 1]

    first_valid = first_letter == letter
    second_valid = second_letter == letter

    if first_valid or second_valid:
        print(line)
        if not (first_valid and second_valid):
            valid2 += 1

print('total({}) valid({})'.format(total, valid2))
