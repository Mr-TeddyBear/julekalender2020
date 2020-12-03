
if __name__ == "__main__":

    limits = []
    chars = []
    passwd = []

    with open('input', 'r') as file:
        for line in file:
            line = line.split(" ")
            limits.append([int(i) for i in line[0].split("-")])
            chars.append(line[1][0])
            passwd.append(line[-1])

    correct_passwd = 0

    for i in range(len(passwd)):
        if limits[i][0] <= passwd[i].count(chars[i]) <= limits[i][1]:
            correct_passwd += 1

    print(correct_passwd)


# Del 2


def isinplace(pos, char, passwd):
    if char == passwd[pos-1]:
        return True
    return False
if __name__ == "__main__":
    correct_passwd2 = 0

    for i in range(len(passwd)):
        if isinplace(limits[i][0], chars[i], passwd[i]) != isinplace(limits[i][1], chars[i], passwd[i]):
            correct_passwd2 += 1

    print(correct_passwd2)