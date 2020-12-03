import numpy as np


def isprime(n):
    if n in primes:
        return True
    if n == 7:
        return True
    
    if (n == 2):
        return True
    
    if (n % 2  == 0 and n != 2):
        return False

    j=3
    while (j <= np.sqrt(n)):
        if ( n % j == 0 ):
            return False
        j += 2
    return True

def revPrime(number):
    for i in range(number, 3, -1):
        if isprime(i):
            primes.append(i)
            return i

if __name__ == "__main__":
    primes = []
    
    pakker = 5433000
    sendt = 0

    i = 0
    while (i <= pakker):
        if "7" in str(i):
            kastes = revPrime(i)
            i += kastes + 1
        else:
            sendt += 1
            i += 1


    print(sendt)