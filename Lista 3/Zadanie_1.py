def prime(n):
    primes = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            primes.append(k)
        k += 1

    return primes

print(prime(30))