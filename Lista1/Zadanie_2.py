import networkx as nx
import matplotlib.pyplot as plt
import random as rd
from itertools import combinations
from math import sqrt
import numpy as np

def nodes_cord(number_of_nodes,nodes):       #function to return dictionary of lists random cordinates of nodes on 100x100 {'id':'[cordx,cordy]'}
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

def distance_calc(edges,gpos):      #calculate distance between each node
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

def tree():
    for i in range(number_of_nodes):
        min_val = min(organized_distance[i])
        min_index = organized_distance[i].index(min_val)+1
        print(min_index,min_val)
        g.add_edge(i+1,min_index)




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
tree()
g.add_nodes_from(nodes)  #add our nodes
nx.draw(g, gpos, with_labels=True, node_color='maroon',font_size="10",node_shape='o',font_color="white")
plt.show()


