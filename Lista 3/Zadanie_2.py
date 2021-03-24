from math import sqrt

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

prime_numbers = net(100)
for prime in prime_numbers:
    print(prime)


