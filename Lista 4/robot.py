import random
import string
from prettytable import PrettyTable

class Robot():

    def __init__(self):
        '''Inicjalizacja robota'''
        self.lenght_of_identity = 6
        self.all_types = ['AUV', 'AFV', 'AGV']
        self.mass_range = (50,2000)  #dag
        self.range_r = (0, 1000)  #km
        self.resolution_range = (1,30)  #MP

        self.identity = self._random_identity()
        self.type = self._random_type()
        self.mass = self._random_mass()
        self.range = self._random_range()
        self.resolution = self._random_resolution()

    def _random_identity(self):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(self.lenght_of_identity))

    def _random_type(self):
        return random.choice(self.all_types)

    def _random_mass(self):
        return random.randint(self.mass_range[0],self.mass_range[1])

    def _random_range(self):
        return random.randint(self.range_r[0], self.range_r[1])

    def _random_resolution(self):
        return random.randint(self.resolution_range[0], self.resolution_range[1])


def generate_M_robots(M):
    vector = []
    for _ in range(M):
        vector.append(Robot())
    return vector

def print_generated_robots(vector):
    count = 1
    for elem in vector:
        print(f'Robot {count}. IDENTITY: {elem.identity}. TYPE: {elem.type}. MASS: {elem.mass}. RANGE: {elem.range}. RESOLUTION {elem.resolution}')
        count +=1

vector = generate_M_robots(2)
print_generated_robots(vector)

