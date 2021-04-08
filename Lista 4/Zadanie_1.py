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
    print('Type identity to be search')
    while True:
        try:
            string = input("Type chain of char: ")
            if len(string) > r.Robot().lenght_of_identity:
                print(f'Too long. Max char is {r.Robot().lenght_of_identity}')
            else:
                return string.upper()
        except Exception as err:
            print(err)


if __name__ == "__main__":
    r_vector = r.generate_M_robots(10)
    r.print_generated_robots(r_vector)

    print(choose_char_chain())

    choosen_trait = choose_trait()
    print(choosen_trait)