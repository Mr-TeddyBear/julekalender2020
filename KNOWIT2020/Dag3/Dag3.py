import numpy as np

def isin(word, matrix):
    wlen = len(word)
    mlen = len(matrix)

    wsqrt = int(np.sqrt(wlen))


    for i in range(mlen):
        for j in range(mlen):
            #Normal horisontal forward and rev search
            if matrix[i,j] == word[0] or matrix[i,j] == word[-1]:
                if not (j > mlen-wlen):
                    if ''.join(matrix[i][j:j+wlen]) == word:
                        print("Normal, ", end='')
                        return True
                if not (j-wlen < 0):
                    if ''.join(matrix[i][j-wlen+1:j+1])[::-1] == word:
                        print("Reverse ,", end='')
                        return True

                # Vertical search
                if  not (i - wlen < 0):
                    #print(''.join(matrix[i-wlen+1:i+1,j]), word)
                    if ''.join(matrix[i-wlen+1:i+1,j])[::-1] == word:                        
                        print("Vert up, ", end='')
                        return True
                if not (wlen + i > mlen):
                    if ''.join(matrix[i:i+wlen,j]) == word:
                        print("Vert down, ", end='')
                        return True

                # Diagonal search
                #Digonal NorthEast and NorthWest

                def NorthEast(i,j,a):
                    return matrix[i-a,j-a]
                
                def NorthWest(i,j,a):
                    return matrix[i-a,j+a]

                def SouthEast(i,j,a):
                    return matrix[i+a,j-a]

                def SouthWest(i,j,a):
                    return matrix[i+a,j+a]


                directions = []

                if not ((i - wlen) < 0):
                    if not (j - wlen < 0):
                        directions.append(NorthEast)
                    else:
                        directions.append(None)
                    if not (j + wlen >= mlen):
                        directions.append(NorthWest)
                    else:
                        directions.append(None)
                else:
                    directions.append(None)
                    directions.append(None)
                if not (i + wlen >= mlen):
                    if not (j + wlen >= wlen):
                        directions.append(SotuhWest)
                    else:
                        directions.append(None)
                    if not (j - wlen < 0):
                        directions.append(SouthEast)
                    else:
                        directions.append(None)
                else:
                    directions.append(None)
                    directions.append(None)
                tmpstr = ["", "", "", ""]
                
                for a in range(wlen):
                    for b in range(4):
                        if directions[b] != None:
                            tmpstr[b] += (directions[b](i,j,a))

#                print(tmpstr, word)
#                print([len(i) for i in tmpstr], len(word))
                for c in tmpstr:
                    if c == word:
                        print("Diag, ", end='')
                        
                        return True








if __name__ == "__main__":
    matrix = np.empty((1000,1000), dtype=str)
    wordlist = []

    with open("matrix.txt", "r") as file:
        for line,i in zip(file,range(1000)):
            for j in range(len(line[:-1])):
                matrix[i,j] = line[j]

    with open("wordlist.txt", "r") as file:
        for line in file:
            wordlist.append(line[:-1])
    

    print(matrix[0:5,0], matrix[5:0,0])

    print(wordlist)
    found = 0
    for word in wordlist:
        if isin(word, matrix):
            print(word)
            found += 1
            wordlist.remove(word)
    
    print(wordlist)
    print(found)

