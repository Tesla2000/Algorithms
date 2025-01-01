from collections.abc import Iterable
from collections.abc import Mapping
from collections.abc import Sequence

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def add_nodes(VV: Iterable,Vx: Mapping,Vy: Mapping):
    gpos = {}
    for v in VV:
        g.add_node(v)  # add nodes
        gpos[v] = [Vx[v], Vy[v]]  # dictionary of cordinates {'id':[xcord,ycord]
    return gpos

def add_labels(Vx: Mapping,Vy: Mapping,VV: Iterable,WW):
    for v1 in VV:
        for v2 in VV:
            if (v1, v2) in WW:
                label = (np.sqrt((Vx[v1] - Vx[v2]) ** 2 + (Vy[v1] - Vy[v2]) ** 2))  # distance between nodes
                label = round(label, 2)
                g.add_weighted_edges_from([(v1, v2, str(label))])  # add edge

def dictionary_nodes(connections: Iterable[Iterable],nodes: Iterable):
    dic = {}

    for node in nodes:
        nodes_connected = []
        for connection in connections:
            if node in connection:
                temp = 0
                for numbers in connection:
                    if numbers != node:
                        temp = numbers

                nodes_connected.append(temp)

        dic[node] = nodes_connected
    return dic

def same(lista: Sequence):    #sprawdza czy jest poprawne polaczenie,czy w WW pary maja te same wartosci
    for i in WW:    #jezeli maja to zwraca false
        if lista[i[0]-1]==lista[i[1]-1]:
            return False
    return True

def ok(VV: Iterable):            #przejscie wszystkich mozliwych mozliwosci
    n = 3
    done = []
    for _ in VV:
        done.append(1)
    k = 0
    while True:
        done[0]+=1
        for i in range(len(done)):
            if done[i]>n:
                done[i]=1
                done[i+1]+=1
        if same(done):
            return done


VV = [1,2,3,4,5,6,7,8,9,10]   #vertex/node
WW = [(1,3),(1,2),(1,7),(2,3),(2,5),(3,4),(5,6),(8,7),(8,9),(8,10),(9,10)]
Vx = {1:0,2:-1,3:1,4:2,5:-2,6:-2,7:-1.5,8:1.5,9:2.5,10:2}
Vy = {1:0,2:1,3:1,4:2,5:2,6:3,7:-1.5,8:-2,9:-2.5,10:-3}

print(dictionary_nodes(WW,VV))
print(f"List of facilities {ok(VV)}")
print(f"Min number of different facilities is {max(ok(VV))}")
g = nx.Graph()
add_labels(Vx,Vy,VV,WW)
nx.draw(g, add_nodes(VV,Vx,Vy), with_labels=True, node_color='yellow')  #draw grapg
labels = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(g, add_nodes(VV,Vx,Vy), edge_labels=labels) #draw edge labels
plt.show()


names = ok(VV)
rename = {}
for i in range(10):
    rename[VV[i]] = names[i]



nx.draw(g,add_nodes(VV,Vx,Vy), labels=rename, with_labels = True)
plt.show()
