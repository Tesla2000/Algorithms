import math
from datetime import datetime

def factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def aczp(a, b):
    a_primes = factors(a)
    b_primes = factors(b)
    common = (set(a_primes) - (set(a_primes) - set(b_primes)))
    return max(common)

def aeuc(a, b):
    while b:
        a, b = b, a % b
    return a

def get_number():
    index1 = [2,4,3,8,1]
    index2 = [2,5,6,7,2]
    index = []
    for i in range(len(index1)):
        index.append(index1[i]*index2[i])

    return math.prod(index)

def get_time():
    return datetime.now()

t1 = get_time()
print(aczp(161280,161280))
t2 = get_time()
print(t2-t1)
t1 = get_time()
print(aeuc(161280,161280))
t2 = get_time()
print(t2-t1)
