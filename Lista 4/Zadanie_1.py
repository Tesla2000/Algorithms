from prettytable import PrettyTable

import robot as r

def choose_trait():
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
            if number in [1,2,3,4,5]:
                return number
            else:
                print('\nInvalid number')
                print(t)
        except Exception as err:
            print(err)
            print(t)

def choose_char_chain():
    print('Type identity to be searched')
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
    print(f'Type one of the following types to be searched: "AGV", "AFV", "AUV"')

    t = PrettyTable(['CHOOSE:', ''])
    t.add_row(['1 - ', 'AGV'])
    t.add_row(['2 - ', 'AFV'])
    t.add_row(['3 - ', 'AUV'])
    print(t)

    while True:
        try:
            number = int(input("Type number: "))
            if number in [1,2,3]:
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
    print('Type the mass of robot to be searched')
    while True:
        try:
            int_mass = int(input("Type mass: "))
            if int_mass < 50 or int_mass >200:
                print('All robots mass is between 50 and 200')
            else:
                return  int_mass

        except Exception as err:
            print(err)

def choose_range():
    print('Type the range of robot to be searched')
    while True:
        try:
            int_range = int(input("Type range: "))
            if int_range < 0 or int_range >1000:
                print('All robots range is between 0 and 1000')
            else:
                return  int_range

        except Exception as err:
            print(err)

def choose_resolution():
    print('Type the resolution of robot to be searched')
    while True:
        try:
            int_res = int(input("Type resolution: "))
            if int_res < 1 or int_res >30:
                print('All robots resolution is between 1 and 30')
            else:
                return  int_res

        except Exception as err:
            print(err)

def single_trait_search(r_vector):
    trait = choose_trait()
    wanted_robots = []
    if trait == 1:
        identity = choose_char_chain()
        for elem in r_vector:
            if identity in elem.identity:
                wanted_robots.append(elem)
        if len(wanted_robots) == 0:
            return None
        else:
            return wanted_robots
    elif trait == 2:
        type = choose_type()
        for elem in r_vector:
            if type == elem.type:
                wanted_robots.append(elem)
        if len(wanted_robots) == 0:
            return None
        else:
            return wanted_robots
    elif trait == 3:
        mass = choose_mass()
        for elem in r_vector:
            if mass == elem.mass:
                wanted_robots.append(elem)
        if len(wanted_robots) == 0:
            return None
        else:
            return wanted_robots
    elif trait == 4:
        range = choose_range()
        for elem in r_vector:
            if range == elem.mass:
                wanted_robots.append(elem)
        if len(wanted_robots) == 0:
            return None
        else:
            return wanted_robots
    elif trait == 5:
        res = choose_resolution()
        for elem in r_vector:
            if res == elem.mass:
                wanted_robots.append(elem)
        if len(wanted_robots) == 0:
            return None
        else:
            return wanted_robots

if __name__ == "__main__":
    r_vector = r.generate_M_robots(10)
    r.print_generated_robots(r_vector)

    t = single_trait_search(r_vector)
    r.print_generated_robots(t)

