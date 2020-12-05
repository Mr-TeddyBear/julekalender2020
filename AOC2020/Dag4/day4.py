

passports = []

with open("input", "r") as file:
    tmpdict = {}
    for line in file:
        if line != "\n":
            line = line[:-1]
            if len(line) == 3: print(line)
            if " " in line:
                line = line.split()
            if isinstance(line, list):
                line = [i.split(":") for i in line]
            else:
                line = line.split(":")
            if isinstance(line[0], str):
                tmpdict[line[0]] = line[1]
            elif isinstance(line[0], list):
                for i in line:
                    tmpdict[i[0]] = i[1]
        else:
            passports.append(tmpdict.copy())
            tmpdict.clear()
    passports.append(tmpdict.copy())
    tmpdict.clear()


mando = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']

not_valid = 0
print(f"Number of passports {len(passports)}")
#for i in passports:
#    print(i)

missing = []
nrmiss = []
antpass = len(passports)

for i,u in enumerate(passports):
    for field in mando:
        if not field in u:
            not_valid += 1
            #print(field,u)
            missing.append(u)
            foundmiss = True
            nrmiss.append(i)
            break

for i in sorted(nrmiss, reverse=True):
    del passports[i]


print(f"\nNumber of incomplete passports {not_valid}")
print(f"Number of passports with all fields {antpass-not_valid}")

"""
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
"""


valid = {'byr': [1920, 2002],
         'iyr': [2010,2020],
         'eyr': [2020, 2030], 
         'hgt': {'cm': [150,193], 'in': [59,76]}, 
         'ecl': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'], 
         'pid': 9}


for u in passports:
    for key in u:
        if key in ['byr','iyr','eyr','hgt']:
            if key == 'hgt':
                if not u[key][-2:] in ['cm', 'in']:
                    not_valid += 1
                    break

                valhgt = valid[key][u[key][-2:]]

                if not (valhgt[0] <= int(u[key][:-2]) <= valhgt[1]):
                    not_valid += 1
                    break
            else:
                if len(u[key]) != 4:
                    not_valid += 1
                    break
                val = valid[key]
                if not (val[0] <= int(u[key]) <= val[1]):
                    not_valid += 1
                    break

        elif key == 'ecl':
            if not u[key] in valid[key]:
                not_valid += 1
                break

        elif key == 'pid':
            if len(u[key]) != valid[key]:
                not_valid += 1
                break
            else:
                try:
                    int(u[key])
                except:
                    not_valid += 1
                    break

        elif key == 'hcl':
            if u[key][0] != '#' or len(u[key][1:]) != 6:
                not_valid += 1
                break
            else:
                try:
                    int(u[key][1:], 16)
                except:
                    not_valid += 1
                    break


print(f"Number of valid passports, with valid data, is {antpass-not_valid}. \nNumber of not valid passports {not_valid}")
