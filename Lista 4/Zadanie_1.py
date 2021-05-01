from prettytable import PrettyTable
import time

import robot as r


def choose_trait():
    print('\nChoose trait to be searched')
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
                return number
            else:
                print('\nInvalid number')
                print(t)
        except Exception as err:
            print(err)
            print(t)


def choose_char_chain():
    print('\nType identity to be searched')
    while True:
        try:
            string = input("Type chain of char: ")
            if len(string) > r.Robot().lenght_of_identity:
                print(f'Too long. Max char is {r.Robot().lenght_of_identity}')
            else:
                return string.upper()
        except Exception as err:
            print(err)


def choose_type():
    print(f'\nType one of the following types to be searched: "AGV", "AFV", "AUV"')

    t = PrettyTable(['CHOOSE:', ''])
    t.add_row(['1 - ', 'AGV'])
    t.add_row(['2 - ', 'AFV'])
    t.add_row(['3 - ', 'AUV'])
    print(t)

    while True:
        try:
            number = int(input("Type number: "))
            if number in [1, 2, 3]:
                if number == 1:
                    return 'AGV'
                elif number == 2:
                    return 'AFV'
                else:
                    return 'AUV'
            else:
                print('\nInvalid number')
                print(t)
        except Exception as err:
            print(err)
            print(t)


def choose_mass():
    print('\nType the mass of robot to be searched')
    while True:
        try:
            int_mass = int(input("Type mass: "))
            if int_mass < 50 or int_mass > 2000:
                print('All robots mass is between 50 and 2000')
            else:
                return int_mass

        except Exception as err:
            print(err)


def choose_range():
    print('\nType the range of robot to be searched')
    while True:
        try:
            int_range = int(input("Type range: "))
            if int_range < 0 or int_range > 1000:
                print('All robots range is between 0 and 1000')
            else:
                return int_range

        except Exception as err:
            print(err)


def choose_resolution():
    print('\nType the resolution of robot to be searched')
    while True:
        try:
            int_res = int(input("Type resolution: "))
            if int_res < 1 or int_res > 30:
                print('All robots resolution is between 1 and 30')
            else:
                return int_res

        except Exception as err:
            print(err)


def single_trait_search(r_vector):
    trait = choose_trait()
    wanted_robots = []

    if trait == 1:
        identity = choose_char_chain()
        print(f"\nSearching IDENTITY: '{identity}' ")
        for elem in r_vector:
            print(f"\nIDENTITY of {elem} is {elem.identity}")
            if identity in elem.identity:
                print(f"Found in {elem}")
                wanted_robots.append(elem)
            else:
                print(f"Not found in {elem}")
            time.sleep(0.2)
        if len(wanted_robots) == 0:
            return None
        else:
            return wanted_robots
    elif trait == 2:
        type = choose_type()
        print(f"\nSearching TYPE: '{type}' ")
        for elem in r_vector:
            print(f"\nTYPE of {elem} is {elem.type}")
            if type == elem.type:
                print(f"Found in {elem}")
                wanted_robots.append(elem)
            else:
                print(f"Not found in {elem}")
            time.sleep(0.2)
        if len(wanted_robots) == 0:
            return None
        else:
            return wanted_robots
    elif trait == 3:
        mass = choose_mass()
        print(f"\nSearching MASS: '{mass}' ")
        for elem in r_vector:
            print(f"\nMASS of {elem} is {elem.mass}")
            if mass == elem.mass:
                print(f"Found in {elem}")
                wanted_robots.append(elem)
            else:
                print(f"Not found in {elem}")
            time.sleep(0.2)
        if len(wanted_robots) == 0:
            return None
        else:
            return wanted_robots
    elif trait == 4:
        range = choose_range()
        print(f"\nSearching RANGE: '{range}' ")
        for elem in r_vector:
            print(f"\nRANGE of {elem} is {elem.range}")
            if range == elem.range:
                print(f"Found in {elem}")
                wanted_robots.append(elem)
            else:
                print(f"Not found in {elem}")
            time.sleep(0.2)
        if len(wanted_robots) == 0:
            return None
        else:
            return wanted_robots
    elif trait == 5:
        res = choose_resolution()
        print(f"\nSearching RESOLUTION: '{res}' ")
        for elem in r_vector:
            print(f"\nRESOLUTION of {elem} is {elem.resolution}")
            if res == elem.resolution:
                print(f"Found in {elem}")
                wanted_robots.append(elem)
            else:
                print(f"Not found in {elem}")
            time.sleep(0.2)
        if len(wanted_robots) == 0:
            return None
        else:
            return wanted_robots


def decision():
    while True:
        try:
            decision = input("Y\\N? :")
            decision = decision.upper()
            if decision == 'Y':
                return True
            elif decision == 'N':
                return False
            else:
                print('Wrong input')

        except Exception as err:
            print(err)


def decision2():
    while True:
        try:
            decision = input("S\\V? :")
            decision = decision.upper()
            if decision == 'S':
                return True
            elif decision == 'V':
                return False
            else:
                print('Wrong input')

        except Exception as err:
            print(err)


def decision3():
    while True:
        try:
            print('\nAdd another?')
            decision = input("Y\\N? :")
            decision = decision.upper()
            if decision == 'Y':
                return True
            elif decision == 'N':
                return False
            else:
                print('Wrong input')

        except Exception as err:
            print(err)


def full_vector_trait():
    search_vector = []
    print('FULL VECTOR SEARCH')
    print('Whick traits you want to use for search?')
    print('Identity?')
    if decision():
        search_vector.append(choose_char_chain())
    else:
        search_vector.append(None)
    print('Add Type trait to use for search?')
    if decision():
        search_vector.append(choose_type())
    else:
        search_vector.append(None)
    print('Add Mass trait to use for search?')
    if decision():
        search_vector.append(choose_mass())
    else:
        search_vector.append(None)
    print('Add Range trait to use for search?')
    if decision():
        search_vector.append(choose_range())
    else:
        search_vector.append(None)
    print('Add Resolution trait to use for search?')
    if decision():
        search_vector.append(choose_resolution())
    else:
        search_vector.append(None)

    return search_vector


def multi_full_vector_trait():
    search_vector = []
    print('\nMULTI FULL VECTOR SEARCH')
    print('Whick traits you want to use for search?')
    print('Identity?')
    if decision():
        identity = []
        identity.append(choose_char_chain())
        while decision3():
            identity.append(choose_char_chain())
        search_vector.append(identity)
    else:
        search_vector.append(None)
    print('\nAdd Type trait to use for search?')
    if decision():
        type = []
        type.append(choose_type())
        while decision3():
            type.append(choose_type())
        search_vector.append(type)
    else:
        search_vector.append(None)
    print('\nAdd Mass trait to use for search?')
    if decision():
        mass = []
        mass.append(choose_mass())
        while decision3():
            mass.append(choose_mass())
        search_vector.append(mass)
    else:
        search_vector.append(None)
    print('\nAdd Range trait to use for search?')
    if decision():
        range = []
        range.append(choose_range())
        while decision3():
            range.append(choose_range())
        search_vector.append(range)
    else:
        search_vector.append(None)
    print('\nAdd Resolution trait to use for search?')
    if decision():
        resolution = []
        resolution.append(choose_resolution())
        while decision3():
            resolution.append(choose_resolution())
        search_vector.append(resolution)
    else:
        search_vector.append(None)

    return search_vector


def full_vector_search(r_vector, search_vec):
    print(f'\nSearching following vector: {search_vec}')
    wanted_robots = []
    for elem in r_vector:
        print(f'\nSearching in: {elem}')
        print('Searching: Identity, Type, Mass, Rang, Resolution')
        ziped = zip(robot_object_unpack(elem),search_vec)

        temp = []
        first_item = True
        for original, wanted in ziped:
            if first_item:
                if wanted == None:
                    print('Not searching. Param is NoneType')
                    temp.append(None)
                else:
                    print(f'Searching: {wanted}')
                    if str(wanted) in str(original):
                        print(f'Found in {elem}')
                        temp.append(wanted)
                    else:
                        print(f'Not found in {elem}')
                        temp.append(None)
                    time.sleep(0.2)
            else:
                if wanted == None:
                    print('Not searching. Param is NoneType')
                    temp.append(None)
                else:
                    print(f'Searching: {wanted}')
                    if str(wanted) == str(original):
                        print(f'Found in {elem}')
                        temp.append(wanted)
                    else:
                        print(f'Not found in {elem}')
                        temp.append(None)
                    time.sleep(0.2)
            first_item = False

        if temp == search_vec:
            wanted_robots.append(elem)

    if len(wanted_robots) == 0:
        return None
    else:
        return wanted_robots

def multi_full_vector_search(r_vector, search_vec):
    print(f'\nSearching following vector: {search_vec}')
    wanted_robots_temp = []

    if search_vec[0] != None:
        print('\nSearching IDENTITY')
        temp = []
        for trait in search_vec[0]:
            for robot in r_vector:
                print(f'\nSearching: {trait}')
                print(f'IDENTITY OF {robot} is {robot.identity}')
                if trait in robot.identity:
                    print(f'Found in {robot}')
                    temp.append(robot)
                else:
                    print(f'Not found in {robot}')
                time.sleep(0.2)

        temp_set = set(temp)
        wanted_robots_temp.append(temp_set)
    else:
        wanted_robots_temp.append(set(r_vector))


    if search_vec[1] != None:
        print('\nSearching TYPE')
        temp = []
        for trait in search_vec[1]:
            for robot in r_vector:
                print(f'\nSearching: {trait}')
                print(f'TYPE OF {robot} is {robot.type}')
                if trait == robot.type:
                    print(f'Found in {robot}')
                    temp.append(robot)
                else:
                    print(f'Not found in {robot}')
                time.sleep(0.2)
        temp_set = set(temp)
        wanted_robots_temp.append(temp_set)
    else:
        wanted_robots_temp.append(set(r_vector))

    if search_vec[2] != None:
        print('\nSearching MASS')
        temp = []
        for trait in search_vec[2]:
            for robot in r_vector:
                print(f'\nSearching: {trait}')
                print(f'MASS OF {robot} is {robot.mass}')
                if trait == robot.mass:
                    print(f'Found in {robot}')
                    temp.append(robot)
                else:
                    print(f'Not found in {robot}')
                time.sleep(0.2)
        temp_set = set(temp)
        wanted_robots_temp.append(temp_set)
    else:
        wanted_robots_temp.append(set(r_vector))

    if search_vec[3] != None:
        print('\nSearching RANGE')
        temp = []
        for trait in search_vec[3]:
            for robot in r_vector:
                print(f'\nSearching: {trait}')
                print(f'RANGE OF {robot} is {robot.range}')
                if trait == robot.range:
                    print(f'Found in {robot}')
                    temp.append(robot)
                else:
                    print(f'Not found in {robot}')
                time.sleep(0.2)
        temp_set = set(temp)
        wanted_robots_temp.append(temp_set)
    else:
        wanted_robots_temp.append(set(r_vector))

    if search_vec[4] != None:
        print('\nSearching RESOLUTION')
        temp = []
        for trait in search_vec[4]:
            for robot in r_vector:
                print(f'\nSearching: {trait}')
                print(f'RESOLUTION OF {robot} is {robot.resolution}')
                if trait == robot.resolution:
                    print(f'Found in {robot}')
                    temp.append(robot)
                else:
                    print(f'Not found in {robot}')
                time.sleep(0.2)

        temp_set = set(temp)
        wanted_robots_temp.append(temp_set)
    else:
        wanted_robots_temp.append(set(r_vector))

    wanted_robots = wanted_robots_temp[0].intersection(wanted_robots_temp[1], wanted_robots_temp[2], wanted_robots_temp[3] , wanted_robots_temp[4])
    wanted_robots = list(wanted_robots)
    if len(wanted_robots) == 0:
        return None
    else:
        return wanted_robots

def robot_object_unpack(robot):
    list =[]
    id = robot.identity
    list.append(id)
    type = robot.type
    list.append(type)
    mass = robot.mass
    list.append(mass)
    range = robot.range
    list.append(range)
    res = robot.resolution
    list.append(res)
    return list

if __name__ == "__main__":
    r_vector = r.generate_M_robots(10)
    r.print_generated_robots(r_vector)

    print('\nSearch algorithm on the foregoing robots data.\n')

    print('Would you like to use single trait or vector trait search?')
    if decision2():
        found = single_trait_search(r_vector)
        print('\nDetected robots with given parameters:')
        r.print_generated_robots(found)
    else:
        print('Would you like to give multiple params to one trait?')
        if decision():
            search_vec = multi_full_vector_trait()
            found = multi_full_vector_search(r_vector, search_vec)
            print('\nDetected robots with given parameters:')
            r.print_generated_robots(found)
        else:
            search_vec = full_vector_trait()
            found = full_vector_search(r_vector, search_vec)
            print('\nDetected robots with given parameters:')
            r.print_generated_robots(found)
