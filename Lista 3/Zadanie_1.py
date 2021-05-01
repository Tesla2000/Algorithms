from math import sqrt

def fun(n, l):
    if x%n==0:
        if check_prime(n):
            l.append(n)
    if n==1:
         return None
    fun(n-1, l)

def check_prime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

def since_till(since, till):
    zw = []
    while since != till + 1:
        zw.append(since)
        since += 1
    return zw

def net(till):
    sq = int(sqrt(till))
    current = 1
    tab = since_till(1, till)
    while True:
        if current > sq:
            return tab

        for i in tab:
            if (not (i % current) and not (current == i)) and current != 1:
                tab.remove(i)

        i = tab.index(current) + 1
        current = tab[i]

x=24
l=[]
fun(x, l)
print(l)

prime_numbers = net(100)
print(prime_numbers)
