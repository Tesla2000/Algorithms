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
    fig, axs = plt.subplots(2)
    fig.suptitle('Time in miliseconds')
    axs[0].set_title('Prime algorithm')
    axs[1].set_title('Euclides algorithm')
    plt.setp(axs[0], ylabel='Time')
    plt.setp(axs[1], ylabel='Time')
    x = np.linspace(1, len(aczp), len(aczp))
    axs[0].plot(x, aczp)
    axs[1].plot(x, euc)
    fig.tight_layout()
    plt.show()


def main():
    times_aczp = []
    times_euc = []
    for i in range(get_number()):
        t1 = get_time()
        t2 = get_time()
        delta1 = t2-t1
        delta1 = delta1.total_seconds()
        times_aczp.append(delta1)
        t1 = get_time()
        t2 = get_time()
        delta2 = t2 - t1
        delta2 = delta2.total_seconds()
        times_euc.append(delta2)
        if delta1 >=300 or delta2 >= 300:
            print('Too long')
            break

    graph(times_aczp, times_euc)

main()

