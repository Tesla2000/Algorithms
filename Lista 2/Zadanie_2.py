import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
VV = [1, 2, 3, 4, 5]      #nodes
WW = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 3), (3, 5)]       #edges
Vx = {1:0, 2:1, 3:2, 4:3, 5:4}    #xcords of nodes
Vy = {1:0, 2:1, 3:0, 4:-1, 5:0}   #ycords of nodes
g = nx.Graph()
gpos = {}
for v in VV:
  g.add_node(v)     #add nodes
  gpos[v] = [Vx[v], Vy[v]]      #dictionary of cordinates {'id':[xcord,ycord]
for v1 in VV:
  for v2 in VV:
    if (v1, v2) in WW:
      label = str(np.sqrt((Vx[v1] - Vx[v2])**2 + (Vy[v1] - Vy[v2])**2))   #distance between nodes
      g.add_weighted_edges_from([(v1, v2, label)])  #add edge
nx.draw(g, gpos, with_labels=True, node_color='yellow')  #draw grapg
labels = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(g, gpos, edge_labels=labels) #draw edge labels
plt.show()