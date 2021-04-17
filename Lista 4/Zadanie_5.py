import numpy as np

import robot as r
from Zadanie_1 import multi_full_vector_trait

def sorted_index_vector(r_vector):
    identity = []
    type = []
    mass = []
    range = []
    resolution = []

    for robot in r_vector:
        identity.append(robot.identity)
        type.append(robot.type)
        mass.append(robot.mass)
        range.append(robot.range)
        resolution.append(robot.resolution)

    identity_index = list(np.argsort(identity))
    type_index = list(np.argsort(type))
    mass_index = list(np.argsort(mass))
    range_index = list(np.argsort(range))
    res_index = list(np.argsort(resolution))

    return [identity_index, type_index, mass_index, range_index, res_index]

def sorted_robots(r_vector, sorted_indexes):
    s_robots = []
    for trait in range(len(sorted_indexes)):
        s_robots.append([r_vector[i] for i in sorted_indexes[trait]])

    return s_robots

def binary_search(array, element, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if element == array[mid].mass:
        return mid

    if element < array[mid].mass:
        return binary_search(array, element, start, mid-1)
    else:
        return binary_search(array, element, mid+1, end)

if __name__ == '__main__':
    robots = r.generate_M_robots(10)
    r.print_generated_robots(robots)

    sorted_indexes = sorted_index_vector(robots)
    s_robots = sorted_robots(robots, sorted_indexes)
    for elem in s_robots:
        r.print_generated_robots(elem)

    print(binary_search(s_robots, 50, 0, len(s_robots[0])))

