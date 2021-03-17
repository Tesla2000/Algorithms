import networkx as nx
import matplotlib.pyplot as plt
import random as rd
from itertools import combinations

def nodes_cord(number_of_nodes,nodes):
    iterations = 0
    nodes_cordinates = {}
    while len(nodes_cordinates) < number_of_nodes:      #to count iterations and quit if greater than 100
        for elem in nodes:
            temp_cordinates = (round(rd.uniform(0, 1), 2), round(rd.uniform(0, 1), 2)) #random cordinates
            if temp_cordinates not in nodes_cordinates:             #if already exist try again
                nodes_cordinates[elem] = list(temp_cordinates)
            iterations += 1
            if iterations >= 100:                       #quit if too many iterations
                print("Error")
                quit()
    return nodes_cordinates

def nodes_name_list(number_of_nodes):
    nodes = []
    for i in range(number_of_nodes):
        nodes.append(i + 1)
    return nodes

def delete_edges(edges):
    for i in range(rd.randint(30, 35)):
        random_edge_to_be_deleted = rd.choice(edges)
        edges.remove(random_edge_to_be_deleted)
    return edges


number_of_nodes = 10
nodes = nodes_name_list(number_of_nodes)
edges = list(combinations(nodes, 2))  #returns list of tuples,all edges - full graph
edges = delete_edges(edges)
print(len(edges))




gpos = nodes_cord(number_of_nodes,nodes)  #dictionary of cordinates of our nodes
print(gpos)

g = nx.Graph()
g.add_nodes_from(nodes)  #add our nodes
g.add_edges_from(edges) #add edges
nx.draw(g, gpos, with_labels=True, node_color='purple',font_size="10")
plt.show()