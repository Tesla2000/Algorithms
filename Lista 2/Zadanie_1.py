import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()     #create an empty graph with no nodes or edges
G.add_edge('A', 'B', weight=4)      #add edge between A and B,nodes will be added automatically, weight - data about the edgee
G.add_edge('B', 'D', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=4)
pos = nx.spring_layout(G)  #Position nodes using Fruchterman-Reingold force-directed algorithm.
nx.draw_networkx_nodes(G, pos, node_size = 500)   #draw nodes
nx.draw_networkx_labels(G, pos)         #draw labels
nx.draw_networkx_edges(G, pos)          #draw edges

plt.show()              #display the result