import networkx as nx
import matplotlib.pyplot as plt
import random as rd
from itertools import combinations
from math import sqrt

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

def tree(nodes,organized_distance):             #function to connect all nodes,
    nodes_used = []
    connections = []
    temp_node= rd.choice(nodes)
    nodes.remove(temp_node)                     #random 2 nodes and connect them
    temp_node2 = rd.choice(nodes)
    nodes.remove(temp_node2)
    g.add_edge(temp_node,temp_node2)
    connections.append([temp_node,temp_node2])

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
        connections.append([temp_node, node_to_connect])
    return connections

def dictionary_nodes(connections,nodes):
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


def distance_between_two_random_nodes(graph,start,goal):
    explored = []

    # Queue for traversing the
    # graph in the
    queue = [[start]]

    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return

    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Codition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return
            explored.append(node)

            # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting" \
          "path doesn't exist :(")
    return new_path


number_of_nodes = 10
nodes = nodes_name_list(number_of_nodes)
edges = list(combinations(nodes, 2))  #returns list of tuples,all edges - full graph
gpos = nodes_cord(number_of_nodes,nodes)  #dictionary of cordinates of our nodes
distance = distance_calc(edges,gpos)
organized_distance = lists_of_edges_for_every_node()

g = nx.Graph()
g.add_nodes_from(nodes)  #add our nodes
connections = tree(nodes,organized_distance)
dic_of_connections = dictionary_nodes(connections,nodes_name_list(10))
distance_between_two_random_nodes(dic_of_connections,3,5)
nx.draw(g, gpos, with_labels=True, node_color='maroon', font_size="10", node_shape='o', font_color="white")
plt.show()




