from prettytable import PrettyTable

import robot as r
from Zadanie_2 import ro_list, count_sort

def quicksort(array):

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        print(f'\nPivot: {pivot}')
        for elem in array:
            if elem < pivot:
                print(f'{elem} < {pivot}: less appended')
                less.append(elem)
            elif elem == pivot:
                print(f'{elem} == {pivot}: equal appended')
                equal.append(elem)
            elif elem > pivot:
                print(f'{elem} > {pivot}: equal appended')
                greater.append(elem)
        print(f'Less: {less}\nEqual: {equal}\nGreater: {greater}')
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


    res_list = ro_list(r_vector)
    n = len(res_list)

    print(f'Sorted resolution: {count_sort(res_list, n)}')
