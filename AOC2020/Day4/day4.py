

passports = []

with open("input", "r") as file:
    tmpdict = {}
    for line in file:
        if line != "\n":
            line = line[:-1]
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
            passports.append(tmpdict)
            tmpdict = {}


mando = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']

not_valid = 0

for u in passports:
    for field in mando:
        if field in u:
            pass
        else:
            not_valid += 1
            print(u)
            break

print(not_valid)
