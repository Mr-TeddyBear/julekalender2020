

def search2():
    for i in inpt:
        for j in inpt:
            if sum([i,j]) == 2020:
                return i*j
def search3():
    for i in inpt:
        for j in inpt:
            for k in inpt:
                if sum([i,j,k]) == 2020:
                   return i*j*k




if __name__ == "__main__":
    inpt = []

    with open('input', 'r') as file:
        for line in file:
            inpt.append(int(line))

    print(f"The product of 2 elemts is : {search2()}")
    print(f"The product of 3 elemnts is: {search3()}")

