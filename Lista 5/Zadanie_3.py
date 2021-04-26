import robot as r


def quicksort(array):

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for elem in array:
            if elem < pivot:
                less.append(elem)
            elif elem == pivot:
                equal.append(elem)
            elif elem > pivot:
                greater.append(elem)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return array


def r_list(robot_vector):
    identity = []
    type_r = []
    mass = []
    range_r = []
    resolution = []
    for robot in robot_vector:
        identity.append(robot.identity)
        type_r.append(robot.type)
        mass.append(robot.mass)
        range_r.append(robot.range)
        resolution.append(robot.resolution)
    return identity, type_r, mass, range_r, resolution


if __name__ == "__main__":
    r_vector = r.generate_M_robots(10)
    r.print_generated_robots(r_vector)

    print(quicksort(r_list(r_vector)[2]))
