




def convertTrueFalse(liste):
    case = {'#': True, '.': False}
    return [[case[i] for i in j] for j in liste]



def traverse(liste, Dstep, Rstep):
    Ypos = 0+Dstep
    Xpos = 0+Rstep

    Ydim = len(liste)
    Xdim = len(liste[0])

    Trees = 0

    End = False

    while not End:
        if (Ypos >= Ydim):
            break

        if liste[Ypos][Xpos%Xdim]:
            Trees += 1

        Xpos += Rstep
        Ypos += Dstep

    return Trees




if __name__ == "__main__":
    slope = []

    with open("input", "r") as file:
        for line in file:
            slope.append(list(line[:-1]))

    tfslope = convertTrueFalse(slope)

    print(traverse(tfslope, 1, 3))

    for i in slope:
        for j in i:
            print(j, end='')
        print("")

    paths = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    pordTree = 1


    for i in paths:
        pordTree *= traverse(tfslope, i[1], i[0])

    print(pordTree)