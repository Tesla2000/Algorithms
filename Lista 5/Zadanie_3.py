from prettytable import PrettyTable

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


def choose_trait():
    print('\nChoose trait to be sorted')
    t = PrettyTable(['CHOOSE:', ''])
    t.add_row(['1 - ', 'IDENTITY'])
    t.add_row(['2 - ', 'TYPE'])
    t.add_row(['3 - ', 'MASS'])
    t.add_row(['4 - ', 'RANGE'])
    t.add_row(['5 - ', 'RESOLUTION'])
    print(t)

    while True:
        try:
            number = int(input("Type number: "))
            if number in [1, 2, 3, 4, 5]:
                return number - 1
            else:
                print('\nInvalid number')
                print(t)
        except Exception as err:
            print(err)
            print(t)


if __name__ == "__main__":
    r_vector = r.generate_M_robots(10)
    r.print_generated_robots(r_vector)

    trait = choose_trait()
    print(f'Sorted in relation to given trait: {quicksort(r_list(r_vector)[trait])}')
