import random

def fermat_test(n: int, k):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(k):
        a = random.randint(1, n - 1)

        if pow(a, n - 1) % n != 1:
            return False
    return True

def miller_rabin(n: int, k):

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def test(number: int, number_of_iterations):
    print(f'Number to be testes: {number}')
    for i in range(number_of_iterations):
        print(f'\nIteration No. {i + 1}')
        print(f'Fermat test. Is primal? {fermat_test(number, number_of_iterations)}')
        print(f'Miller-Rabin test. Is primal? {miller_rabin(number, number_of_iterations)}')


number_of_iterations = 5
number = 16

test(number, number_of_iterations)
