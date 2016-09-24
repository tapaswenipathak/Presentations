import math

def sieve(n):
    primes = [True] * n
    for i in range(2, int(math.sqrt(n+1))):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False
    return primes

primes = sieve(100)

print [i for i, x in enumerate(primes) if x and i > 1]
