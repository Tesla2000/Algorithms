import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def counter(net_x,net_y,safe_dist):
    start_x = 0
    counter_x = 0
    while start_x <= net_x:
        start_x += safe_dist
        counter_x += 1

    start_y = 0
    counter_y = 0
    while start_y <= net_y:
        start_y += safe_dist
        counter_y += 1

    return [counter_x,counter_y,counter_y*counter_x]


def cord_VV(safe_distance,info):
    x_count = info[0]
    y_count = info[1]

    Vx = np.ones(y_count*x_count)
    counter = 0
    for i in range(len(Vx)):
        Vx[i] = counter*safe_distance
        counter += 1
        if Vx[i] > (x_count-1)*safe_distance:
            Vx[i] -= safe_distance
            counter = 0
        elif Vx[i] == (x_count-1)*safe_distance:
            counter = 0

    Vy = np.ones(y_count*x_count)
    counter = 0
    for i in range(len(Vy)):
        Vy[i] = counter*safe_distance
        counter += 1
        if Vy[i] > (y_count-1)*safe_distance:
            Vy[i] -= safe_distance
            counter = 0
        elif Vy[i] == (y_count-1)*safe_distance:
            counter = 0

    return [dict(enumerate(Vx, start=1)),dict(enumerate(Vy, start=1))]

def add_nodes(info,dict):
    x_count = info[0]
    y_count = info[1]
    max_nodes = info[2]

    Vx = dict[0]
    Vy = dict[1]

    print(x_count,y_count,max_nodes)

    gpos = {}

    for i in range(max_nodes):
        g.add_node(i+1)  # add nodes
        gpos[i+1] = [Vx[i+1], Vy[i+1]]  # dictionary of cordinates {'id':[xcord,ycord]
    return gpos

net_x = 300
net_y = 240
safe_dist = 20 #min distance between nodes
max_nodes = 1000

x_y_max = counter(net_x,net_y,safe_dist)
print(x_y_max)
cords = cord_VV(safe_dist,x_y_max)

g = nx.Graph()
gpos = add_nodes(x_y_max,cords)


nx.draw(g, gpos, node_color='yellow')
plt.show()

