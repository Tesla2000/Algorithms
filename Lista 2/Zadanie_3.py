#Napisz program wyświetlający graf pełny o parametrach:
# liczba wierzchołków zadana parametrycznie (jako stała w programie),
# wierzchołki rozmieszczone na okręgu, w równych odstępach,
# etykiety wierzchołkow są kolejnymi liczbami naturalnymi.

import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

number_of_nodes=15
nodes =[]
for i in range(number_of_nodes):
    nodes.append(i+1)

edges = combinations(nodes, 2) #returns list of tuples
g = nx.Graph() #stwórz graph
g.add_nodes_from(nodes)
g.add_edges_from(edges)

pos = nx.circular_layout(g)  #zdefiniowany okrągły rozkład nodes
nx.draw_networkx_nodes(g, pos, node_size = 300,node_color="maroon")
nx.draw_networkx_labels(g, pos, font_size=10, font_color="white")
nx.draw_networkx_edges(g, pos)


plt.show()