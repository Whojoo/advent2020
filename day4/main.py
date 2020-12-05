import re

def map_to_passport_group(matches):
    passport_group = {}
    for match in matches:
        if match[0] == 'cid':
            continue
        passport_group[match[0]] = match[1]
    return passport_group


def valid_check_1(passport_group):
    # byr (Birth Year)
    # iyr (Issue Year)
    # eyr (Expiration Year)
    # hgt (Height)
    # hcl (Hair Color)
    # ecl (Eye Color)
    # pid (Passport ID)
    # cid (Country ID)
    byr_present = 'byr' in passport_group
    iyr_present = 'iyr' in passport_group
    eyr_present = 'eyr' in passport_group
    hgt_present = 'hgt' in passport_group
    hcl_present = 'hcl' in passport_group
    ecl_present = 'ecl' in passport_group
    pid_present = 'pid' in passport_group
    return byr_present and iyr_present and eyr_present and hgt_present and \
           hcl_present and ecl_present and pid_present

def valid_check_2(passport_group):
    if not valid_check_1(passport_group):
        return False

    if re.match(r'^(19[2-9]\d|200[0-2])$', passport_group['byr']) is None:
        return False

    if re.match(r'^20(1\d|20)$', passport_group['iyr']) is None:
        return False

    if re.match(r'^20(2\d|30)$', passport_group['eyr']) is None:
        return False

    hgt_pattern = r'^(1[5-8]\dcm|19[0-3]cm|59in|6\din|7[0-6]in)$'
    if re.match(hgt_pattern, passport_group['hgt']) is None:
        return False

    if re.match(r'^#[\da-f]{6}$', passport_group['hcl']) is None:
        return False

    if re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', passport_group['ecl']) is None:
        return False

    if re.match(r'^\d{9}$', passport_group['pid']) is None:
        return False

    return True

file_input = open("input")

input_list = file_input.read().splitlines()

passport_lines = []

curr_str = ''

for line in input_list:
    if line == '':
        passport_lines.append(curr_str)
        curr_str = ''
        continue

    if curr_str == '':
        curr_str = line
    else:
        curr_str = '{} {}'.format(curr_str, line)

passport_lines.append(curr_str)

pattern = re.compile(r'\s?(\w{3}):([\d#a-z]*)\s?')
passport_groups = []

for passport in passport_lines:
    find_all = pattern.findall(passport)
    passport_groups.append(map_to_passport_group(find_all))

valid_1 = 0

for passport_group in passport_groups:
    if valid_check_1(passport_group):
        valid_1 += 1

print('1: passports({}) valid({})'.format(len(passport_lines), valid_1))

valid_2 = 0

foo = []
for passport_group in passport_groups:
    if valid_check_2(passport_group):
        foo.append(passport_group)
        valid_2 += 1

for bar in foo:
    print(bar['ecl'])
print('2: passports({}) valid({})'.format(len(passport_lines), valid_2))
