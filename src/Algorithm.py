# Nama : Muhammad Gilang Ramadhan
# NIM  : 13520137
# MainAlgorithm Used for Frobenius Problem

from HeapGraph import *

def dijkstra(Graph, Start=1):
    """
    input  : graph from {node1: {node2: distance, node3: distance, ... }, ...}
    output : dictionary {node: shortest path from start to node}
    """
    V = set(Graph.keys())
    StoresNodes = HeapGraph()  # stores nodes in form node = (label, key)
    X = {Start}  # Vertices passed so far
    temp = {Start: 0}  # count shortest path distances

    # Dijkstra greedy score for nodes with edge from 1 is the values of the edges

    heapFill = V - X - set(Graph[Start].keys())  # fill heap with all of the nodes that 1 doesn't have an edge to
    StoresNodes.heapify([(x, 10**6) for x in heapFill])
    for node in Graph[Start]:
        StoresNodes.insert((node, Graph[Start][node]))
    while X != V:
        NodeKey = StoresNodes.extract_min()
        X.add(NodeKey[0])
        temp[NodeKey[0]] = NodeKey[1]
        for v in Graph[NodeKey[0]]:
            if v in V - X:
                StoresNodes.heapList[0] = (0, 0)
                vKey = dict(StoresNodes.heapList)[v]
                StoresNodes.delete((v, vKey))
                vKey = min(temp[NodeKey[0]] + Graph[NodeKey[0]][v], vKey)
                StoresNodes.insert((v, vKey))
    return temp

def make_GreedyGraph(Set):
    """
    input  : Set Of Integers as the numbers of frobenius Problem that will compute the largest number not a linear combination
    output : form {node1: {node2: distance, node3: distance, ... }, ...}
    """
    graph = {}
    m = min(Set)
    for i in range(m):
        graph[i] = {}
        for j in Set:
            if ((i + j) % m not in graph[i]) or (graph[i][(i + j) % m] > j):
                graph[i][(i + j) % m] = j
    return graph

def GreedyDijkstra(Set):
    """
    input  : Set Of Integers as the numbers of frobenius Problem that will compute the largest number not a linear combination
    output : An integer as the solution of Frobenius Problem, i.e. the largest number not a linear combination of inputs
    """

    graph = make_GreedyGraph(Set)
    shortest_paths = dijkstra(graph, 0) # Calculate the shortest paths from the 0 vertex to each non-zero vertex
    v = max(shortest_paths, key=shortest_paths.get)
    return shortest_paths[v] - min(Set)