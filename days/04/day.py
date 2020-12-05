import re
import puzzle


def main():
    print('### day 04 ###')
    print('p1:', part1())
    print('p2:', part2())


def part1():
    passports = get_input()
    print('n_passports', len(passports))

    return len(
        list(
            filter(lambda key: valid(passports[key]), passports)
        )
    )


def valid(p):
    try:
        return p['byr'] != '' and p['iyr'] != '' and p['eyr'] != '' and  p['hgt'] != '' and p['hcl'] != '' and p['ecl'] != '' and p['pid'] != ''  # and
    except:
        return False



def part2():
    passports = get_input()

    n_valid = 0
    for key in passports:
        if valid_strict(passports[key]):
            n_valid += 1

    return n_valid


def valid_strict(p):
    try:
        birth_year = int(p['byr'])
        if birth_year < 1920 or birth_year > 2002:
            return False

        issue_year = int(p['iyr'])
        if issue_year < 2010 or issue_year > 2020:
            return False

        expiration_year = int(p['eyr'])
        if expiration_year < 2020 or expiration_year > 2030:
            return False

        height_unit = p['hgt'][-2:]
        if height_unit not in ['cm','in']:
            return False

        if height_unit == 'cm':
            height = int(p['hgt'][:-2])
            if height < 150 or height > 193:
                return False

        if height_unit == 'in':
            height = int(p['hgt'][:-2])
            if height < 59 or height > 76:
                return False

        hair_color = p['hcl']
        pattern = re.compile(r'^#[a-f0-9]{6}$')
        if not pattern.match(hair_color):
            return False

        eye_color = p['ecl']
        if not eye_color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False

        passport_id = p['pid']
        pattern = re.compile(r'^[0-9]{9}$')
        if not pattern.match(passport_id):
            return False

        return True
    except:
        return False


def get_input():
    lines = puzzle.input.split('\n')

    passport_nr = 0
    passports = {0: {}}
    for i in range(len(lines)):
        line = lines[i]
        if line == '':
            passport_nr += 1
            passports[passport_nr] = {}
            continue

        fields = line.split(' ')
        for f in fields:
            [key, value] = f.split(':')
            passports[passport_nr][key] = value

    return passports


def mod_input(match):
    w1, w2 = match
    return w2, w1


if __name__ == "__main__":
    main()
