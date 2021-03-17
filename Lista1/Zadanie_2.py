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
    pass

number_of_nodes = 10
nodes = nodes_name_list(number_of_nodes)
edges = list(combinations(nodes, 2))  #returns list of tuples,all edges - full graph
gpos = nodes_cord(number_of_nodes,nodes)  #dictionary of cordinates of our nodes
distance = distance_calc(edges,gpos)

print("NODES:")
print(nodes)
print("CORDINATIONS OF NODES")
print(gpos)
print("EDGES")
print(edges)
print("DISTANCE BETWEEN EACH NODE")
print(distance)

test=[]
for i in range(10):
    temp=[]
    for elem in edges:
        if i+1 in elem:
            index_temp = edges.index(elem)
            temp.append(index_temp)
    test.append(temp)


print("TEST")
print(test)
print(len(test))



g = nx.Graph()
g.add_nodes_from(nodes)  #add our nodes
nx.draw(g, gpos, with_labels=True, node_color='purple',font_size="10")
plt.show()


