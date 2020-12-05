import numpy as np

controll = np.arange(1, 100001, dtype=int)

with open('numbers.txt', 'r') as file:
    line = file.readline().split(",")
    inpt = [int(i) for i in line]

inpt = np.sort(np.asarray(inpt))

print(sum(controll) - sum(inpt))
