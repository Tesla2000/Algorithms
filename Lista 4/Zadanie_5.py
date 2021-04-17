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


def binary_search_identity(A, x):
    (left, right) = (0, len(A) - 1)
    result = None

    while left <= right:
        mid = (left + right) // 2
        if x == A[mid].identity:
            result = mid
            right = mid - 1

        elif x < A[mid].identity:
            right = mid - 1
        else:
            left = mid + 1

    return result

def binary_search_type(A, x):

    (left, right) = (0, len(A) - 1)
    result = None

    while left <= right:
        mid = (left + right) // 2
        if x == A[mid].type:
            result = mid
            right = mid - 1

        elif x < A[mid].type:
            right = mid - 1
        else:
            left = mid + 1

    return result

def binary_search_range(A, x):

    (left, right) = (0, len(A) - 1)
    result = None

    while left <= right:
        mid = (left + right) // 2
        if x == A[mid].range:
            result = mid
            right = mid - 1

        elif x < A[mid].range:
            right = mid - 1
        else:
            left = mid + 1

    return result

def binary_search_mass(A, x):

    (left, right) = (0, len(A) - 1)
    result = None

    while left <= right:
        mid = (left + right) // 2
        if x == A[mid].mass:
            result = mid
            right = mid - 1

        elif x < A[mid].mass:
            right = mid - 1
        else:
            left = mid + 1

    return result

def binary_search_resolution(A, x):

    (left, right) = (0, len(A) - 1)
    result = None

    while left <= right:
        mid = (left + right) // 2
        if x == A[mid].resolution:
            result = mid
            right = mid - 1

        elif x < A[mid].resolution:
            right = mid - 1
        else:
            left = mid + 1

    return result

def binary_search_main(sorted_robots, search_vector, sorted_indexes):
    identity_indexes = []
    if search_vector[0] != None:
        result = binary_search_type(sorted_robots[0], search_vector[0])
        identity_indexes.append(result)
        if result != None:
            for i in range(result+1,len(sorted_robots[0])):
                if sorted_robots[0][i].type == search_vector[0]:
                    identity_indexes.append(i)
                else:
                    break
    if identity_indexes:
        if identity_indexes[0] != None:
            identity_indexes = sorted_indexes[0][identity_indexes[0]:identity_indexes[-1]+1]
    
    type_indexes = []
    if search_vector[1] != None:
        result = binary_search_type(sorted_robots[1], search_vector[1])
        type_indexes.append(result)
        if result != None:
            for i in range(result+1,len(sorted_robots[1])):
                if sorted_robots[1][i].type == search_vector[1]:
                    type_indexes.append(i)
                else:
                    break
    if type_indexes:
        if type_indexes[0] != None:
            type_indexes = sorted_indexes[1][type_indexes[0]:type_indexes[-1]+1]
                
    mass_indexes = []
    if search_vector[2] != None:
        result = binary_search_mass(sorted_robots[2], search_vector[2])
        mass_indexes.append(result)
        if result != None:
            for i in range(result+1, len(sorted_robots[2])):
                if sorted_robots[2][i].mass == search_vector[2]:
                    mass_indexes.append(i)
                else:
                    break
    if mass_indexes:
        if mass_indexes[0] != None:
            mass_indexes = sorted_indexes[2][mass_indexes[0]:mass_indexes[-1] + 1]
                
    range_indexes = []
    if search_vector[3] != None:
        result = binary_search_range(sorted_robots[3], search_vector[3])
        range_indexes.append(result)
        if result != None:
            for i in range(result+1,len(sorted_robots[3])):
                if sorted_robots[3][i].range == search_vector[3]:
                    range_indexes.append(i)
                else:
                    break
    if range_indexes:
        if range_indexes[0] != None:
            range_indexes = sorted_indexes[3][type_indexes[0]:type_indexes[-1] + 1]
    
    resolution_indexes = []
    if search_vector[4] != None:
        result = binary_search_resolution(sorted_robots[4], search_vector[4])
        resolution_indexes.append(result)
        if result != None:
            for i in range(result+1,len(sorted_robots[4])):
                if sorted_robots[4][i].resolution == search_vector[4]:
                    resolution_indexes.append(i)
                else:
                    break
    if resolution_indexes:
        if resolution_indexes[0] != None:
            resolution_indexes = sorted_indexes[4][resolution_indexes[0]:resolution_indexes[-1] + 1]

    return [identity_indexes, type_indexes, mass_indexes, range_indexes, resolution_indexes]

def find_common(result, robots):
    result_without_empty = []
    wanted_robots = []

    for elem in result:
        if elem:
            result_without_empty.append(elem)
    result_without_empty = set.intersection(*map(set,result_without_empty))

    if result_without_empty and None not in result_without_empty:
        for elem in list(result_without_empty):
            wanted_robots.append(robots[elem])
        return wanted_robots
    else:
        return None


if __name__ == '__main__':
    robots = r.generate_M_robots(1000)
    r.print_generated_robots(robots)

    sorted_indexes = sorted_index_vector(robots)
    s_robots = sorted_robots(robots, sorted_indexes)

    result = binary_search_main(s_robots, [None, None, 600, None, None], sorted_indexes)

    wanted_robots = find_common(result, robots)
    print('\nDetected robots with given parameters:')
    r.print_generated_robots(wanted_robots)

