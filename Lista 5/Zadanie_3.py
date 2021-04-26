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

if __name__ == "__main__":
    r_vector = r.generate_M_robots(10)
    r.print_generated_robots(r_vector)

    print(quicksort([23, 4, 45, -34, 4, 6, 7]))