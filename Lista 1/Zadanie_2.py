import random as rd
from collections.abc import Iterable
from collections.abc import MutableSequence
from collections.abc import Sequence
from itertools import combinations
from math import sqrt

import matplotlib.pyplot as plt
import networkx as nx

def nodes_cord(number_of_nodes,nodes: Iterable):       #function to return dictionary of lists random cordinates of nodes on 100x100 {'id':'[cordx,cordy]'}
    iterations = 0
    nodes_cordinates = {}
    while len(nodes_cordinates) < number_of_nodes:      #to count iterations and quit if greater than 100
        for elem in nodes:
            temp_cordinates = (round(rd.uniform(0, 100), 2), round(rd.uniform(0, 100), 2)) #random cordinates
            if temp_cordinates not in nodes_cordinates:             #if already exist try again
                nodes_cordinates[elem] = list(temp_cordinates)
            iterations += 1
            if iterations >= 100:                       #quit if too many iterations
                print("Error")
                quit()
    return nodes_cordinates

def nodes_name_list(number_of_nodes):   #return list of numbers to n, nodes names
    nodes = []
    for i in range(number_of_nodes):
        nodes.append(i + 1)
    return nodes

def distance_calc(edges: Iterable[Sequence],gpos: Sequence):      #calculate distance between each node
    distance = []
    for items in edges:
        x_diff = abs(gpos[items[0]][0] - gpos[items[1]][0])
        y_diff = abs(gpos[items[0]][1] - gpos[items[1]][1])
        distance.append(round(sqrt(x_diff ** 2 + y_diff ** 2),2))
    return distance

def lists_of_edges_for_every_node():
    test = []
    for i in range(number_of_nodes):
        temp = []
        for elem in edges:
            if i + 1 in elem:
                index_temp = edges.index(elem)
                temp.append(distance[index_temp])
        test.append(temp)
        temp[i:i] = [999]     #add 999 e.g. 1-1,2-2 etc
    return test

def tree(nodes: MutableSequence,organized_distance: Sequence):             #function to connect all nodes,
    nodes_used = []
    temp_node= rd.choice(nodes)
    nodes.remove(temp_node)                     #random 2 nodes and connect them
    temp_node2 = rd.choice(nodes)
    nodes.remove(temp_node2)
    nx.draw(g, gpos, with_labels=True, node_color='maroon', font_size="10", node_shape='o', font_color="white")
    plt.show()
    g.add_edge(temp_node,temp_node2)
    nx.draw(g, gpos, with_labels=True, node_color='maroon', font_size="10", node_shape='o', font_color="white")
    plt.show()
    nodes_used.append(temp_node)
    nodes_used.append(temp_node2)

    temp_len= len(nodes)

    while len(nodes_used) <= temp_len+1:                #random another node and check distance to all previously connected nodes, connect to the closest one
        temp_node = rd.choice(nodes)
        nodes.remove(temp_node)
        distance_temp = []
        for items in nodes_used:
            distance_temp.append(organized_distance[temp_node-1][items-1])
            minimal_distance = min(distance_temp)
            node_to_connect = organized_distance[temp_node-1].index(minimal_distance)+1

        nodes_used.append(temp_node)
        g.add_edge(temp_node,node_to_connect)

        nx.draw(g, gpos, with_labels=True, node_color='maroon', font_size="10", node_shape='o', font_color="white")
        plt.show()

number_of_nodes = 10
nodes = nodes_name_list(number_of_nodes)
edges = list(combinations(nodes, 2))  #returns list of tuples,all edges - full graph
gpos = nodes_cord(number_of_nodes,nodes)  #dictionary of cordinates of our nodes
distance = distance_calc(edges,gpos)
organized_distance = lists_of_edges_for_every_node()

print("CORDINATIONS OF NODES")
print(gpos)
print("DISTANCE BETWEEN EACH NODE")
for elem in organized_distance:
    print(elem)

g = nx.Graph()
g.add_nodes_from(nodes)  #add our nodes
tree(nodes,organized_distance)
