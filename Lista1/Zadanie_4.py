import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def add_nodes(VV,Vx,Vy):
    gpos = {}
    for v in VV:
        g.add_node(v)  # add nodes
        gpos[v] = [Vx[v], Vy[v]]  # dictionary of cordinates {'id':[xcord,ycord]
    return gpos

def add_labels(Vx,Vy,VV,WW):
    for v1 in VV:
        for v2 in VV:
            if (v1, v2) in WW:
                label = (np.sqrt((Vx[v1] - Vx[v2]) ** 2 + (Vy[v1] - Vy[v2]) ** 2))  # distance between nodes
                label = round(label, 2)
                g.add_weighted_edges_from([(v1, v2, str(label))])  # add edge

VV = [1,2,3,4,5,6,7,8,9,10]   #vertex/node
WW = [(1,3),(1,2),(1,7),(2,3),(2,5),(5,2),(3,4),(5,6),(8,7),(8,9),(8,10),(9,10)]
Vx = {1:0,2:-1,3:1,4:2,5:-2,6:-2,7:-1.5,8:1.5,9:2.5,10:2}
Vy = {1:0,2:1,3:1,4:2,5:2,6:3,7:-1.5,8:-2,9:-2.5,10:-3}

g = nx.Graph()
add_labels(Vx,Vy,VV,WW)
nx.draw(g, add_nodes(VV,Vx,Vy), with_labels=True, node_color='yellow')  #draw grapg
labels = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(g, add_nodes(VV,Vx,Vy), edge_labels=labels) #draw edge labels
plt.show()
