import numpy as np

import robot as r
from Zadanie_1 import multi_full_vector_trait

def sorted_identity_vector(r_vector):
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

def sorted_robots(r_vector, sorted_indexes, trait_to_sort_by):
    return [r_vector[i] for i in sorted_indexes[trait_to_sort_by]]

if __name__ == '__main__':
    robots = r.generate_M_robots(10)
    r.print_generated_robots(robots)

    indexes = sorted_identity_vector(robots)

    r.print_generated_robots(sorted_robots(robots, indexes, 4))

    search_vec = multi_full_vector_trait()
