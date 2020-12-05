
seats = []

with open("input", "r") as file:
    for line in file:
        seats.append(line[:-1])

maxID = 0
rows = [i for i in range(128)]
col = [i for i in range(8)]
foundIDs = []
allIDs = []
for i in range(1,127):
    for j in range(8):
        allIDs.append((i*8)+j)



#Test input med gitte verdier
#seats = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]

for seat in seats:
    findrow = rows
    findcol = col
    for i in seat:
        if i == "F":
            findrow = findrow[:int(len(findrow)/2)]
        elif i == "B":
            findrow = findrow[int(len(findrow)/2):]
        elif i == "R":
            findcol = findcol[int(len(findcol)/2):]
        elif i == "L":
            findcol = findcol[:int(len(findcol)/2)]
    foundIDs.append((int(findrow[0])*8)+int(findcol[0]))

#Største ID i listen
print(max(foundIDs))

for i in foundIDs:
    allIDs.remove(i)

#Riktig id er tallet som er alene i denne listen som printes
print(allIDs)