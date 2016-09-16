def sieve(n):
    not_prime = set()
    primes = []
    for i in xrange(2, n + 1):
        if i not in not_prime:
            prime.append(i)
            for j in xrange(i * i, n + 1, i):
                not_prime.append(j)
    return prime

print sieve(100)
