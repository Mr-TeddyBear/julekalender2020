

with open("input", "r") as file:
    tmp_group = []
    tot_answer = 0
    for line in file:
        if line == "\n":
            print(tmp_group)
            tot_answer += len(tmp_group)
            tmp_group = []
        else:
            line = line[:-1]
            for letter in line:
                if not letter in tmp_group:
                    tmp_group.append(letter)
    print(tmp_group)
    tot_answer += len(tmp_group)

print(f"Number of unique yes in the groups {tot_answer}")

# Part two
with open("input", "r") as file:
    tmp_group = {}
    tot_answer = 0
    ngroup = 0
    for line in file:
        if line == "\n":
            print(tmp_group)
            for key in tmp_group:
                if tmp_group[key] == ngroup:
                    tot_answer += 1
            tmp_group = {}
            ngroup = 0
        else:
            line = line[:-1]
            ngroup += 1
            for letter in line:
                if letter in tmp_group:
                    tmp_group[letter] += 1
                else:
                    tmp_group[letter] = 1
    for key in tmp_group:
        if tmp_group[key] == ngroup:
            tot_answer += 1

print(f"Number of answer where the whole group answerd the same {tot_answer}.")
