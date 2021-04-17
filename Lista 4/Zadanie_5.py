import numpy as np

import robot as r

def sorted_identity_vector(r_vector):
    identity = []

    for robot in r_vector:
        identity.append(robot.identity)

    identity_index = np.argsort(identity)

    return identity_index


if __name__ == '__main__':
    robots = r.generate_M_robots(10)
    r.print_generated_robots(robots)

    print(sorted_identity_vector(robots))
