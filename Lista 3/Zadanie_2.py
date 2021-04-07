import math
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

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

def graph(aczp, euc):
    x_aczp = np.linspace(1,len(aczp),len(aczp))
    plt.plot(x_aczp,aczp)
    plt.title('Times of algorithms')
    plt.ylabel('Miliseconds')
    plt.show()
    x_euc = np.linspace(1,100,len(euc))
    plt.plot(x_euc, euc)
    plt.ylabel('Miliseconds')
    plt.show()

def main():
    times_aczp = []
    times_euc = []
    for i in range(100):
        t1 = get_time()
        t2 = get_time()
        delta = t2-t1
        delta = delta.total_seconds()
        times_aczp.append(delta)
        t1 = get_time()
        t2 = get_time()
        delta = t2 - t1
        delta = delta.total_seconds()
        times_euc.append(delta)

    graph(times_aczp, times_euc)
    return times_aczp, times_euc

x = main()
print(x)

