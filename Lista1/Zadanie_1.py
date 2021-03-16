def sequence_1(n):
    if n ==0:
        return 0
    else:
        return 3**n +sequence_1(n-1)

def sequence_2(n):
    if n ==-1 or n==0:
        return 0
    else:
        return n+sequence_2(n-2)

def sequence_3(n):
    if n==0:
        return 0
    elif n ==1:
        return 1
    else:
        return sequence_3(n-1)+sequence_3(n-2)

