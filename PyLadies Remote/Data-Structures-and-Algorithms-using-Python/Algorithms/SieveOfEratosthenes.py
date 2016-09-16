def sieve(n):
    not_prime = []
    primes = []
    for i in xrange(2, n + 1):
        if i not in not_prime:
            primes.append(i)
            for j in xrange(i * i, n + 1, i):
                not_prime.append(j)
    return primes

print sieve(100)
