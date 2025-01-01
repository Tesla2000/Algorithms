from collections.abc import Iterable
from collections.abc import MutableSequence
from collections.abc import Sequence

import robot as r

from protocols.protocols import RobotvectorSubscript


def minmax_f(tab: Sequence):
    min_n = tab[0]
    max_n = tab[0]
    for el in tab:
        if el > max_n:
            max_n = el
        if el < min_n:
            min_n = el

    return min_n, max_n


def count_sort(tab: MutableSequence, lenght):
    minmax = minmax_f(tab)
    min_n = minmax[0]
    max_n = minmax[1]
    print(f'\nMin: {min_n}, Max: {max_n}')
    counters_size = max_n - min_n + 1
    counters = [0] * counters_size
    for x in range(lenght):
        counters[tab[x] - min_n] += 1
    last_index = 0
    for x in range(counters_size):
        y = last_index
        while y < counters[x] + last_index:
            tab[y] = x + min_n
            y += 1
        last_index = y

    sorted_res = []
    start_val = min_n
    for elem in counters:
        print(f'Value {start_val} Count: {elem}')
        for i in range(elem):
            sorted_res.append(start_val)
        start_val += 1

    return sorted_res


def ro_list(robot_vector: Iterable[RobotvectorSubscript]):
    resolution = []
    for robot in robot_vector:
        resolution.append(robot.resolution)
    return resolution


if __name__ == "__main__":
    r_vector = r.generate_M_robots(10)
    r.print_generated_robots(r_vector)

    res_list = ro_list(r_vector)
    n = len(res_list)

    print(f'Sorted resolution: {count_sort(res_list, n)}')
