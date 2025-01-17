#########################
# Course: COMP 2113 FA01, 2023
# Assignment 8, Question 1
# Author: Brendan Toscano
# Student ID: 0301485t
# email address: 0301485t@acadiau.ca
# Date: 2023-11-26
# I certify that this code is my own.
# I have not broken any rules concerning Academic Dishonesty.
#########################
# What does this program?
# To implement a graph class with addVertex, addEdge, outEdges and inEdges.
# The program should also implement a breath first search and depth first search of the directed graph.
# It created a graph class with 4 functions.
# add vertex creates a vertex and adds it to the dictionary.
# add edge directs vertex1 to vertex2.
# Out edges finds all the edges that vertex 1 points to.
# In edges finds all the edges that are being pointed to.
# dfs will perform a depth first search from the first vertex of the given graph.
# bfs will perform a breath first search from the first vertex of the given graph.
# Both dfs and bfs will return the vertices in the order they are visited.
# Connected components will find all the connected components in the graph.
#########################

# 4:30 - 6:47
# Creating the graph class with addVertex, addEdge, outEdge and inEdge as functions.
class Graph:
    def __init__(self):
        # Creating a dictionary which will be used as the graph. We are using adjecency lists over matrix.
        self.graph = {}
    # Adding the vertex to the dictionary with a empty list to store the values it points to.
    def addVertex(self, vertex):
        if vertex not in graph:
            self.graph[vertex] = []
    # Making one vertex point to another.
    def addEdge(self, vertex1, vertex2):
        # Checking if the vertices exist before using them.
        if vertex1 in self.graph and vertex2 in self.graph:
            # Storing the pointed value in a list.
            self.graph[vertex1].append(vertex2)
        else:
            print("One or both of the vertex does not exist. Add the vertex first before use.")
    # Printing the values of the key. The key here is the vertice and the values are the ones being pointed to.
    def outEdges(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        else:
            return "The vertex doesn't exist."
    # Printing the keys which have the vertex in the values list.
    def inEdges(self, vertex):
        vertices = []
        # Basically using .items to get it in a tuple format where the first value is the key and second the list.
        if vertex in self.graph:
            for item in self.graph.items():
                # If the vertex in the values list then append to the key to the vertices list.
                if vertex in item[1]:
                    vertices.append(item[0])
            return vertices
        else:
            return "The given vertex doesn't exist."

# 8:14 - 10:25
# Implementation of a depth first search of a directed graph.
def dfs(graph, startVertex):
    if startVertex not in graph.graph:
        return "Vertex not in graph"
    # DFS works using stacks so implementing a stack.
    stack = [startVertex]
    # To store the visited values in.
    visited = []
    # Will run till there is nothing left to process.
    while len(stack) != 0:
        # Since a DFS works with stack we remove from the end of the list.
        item = stack.pop()

        # Checking if the item has already been visited before adding.
        if item not in visited:
            visited.append(item)

        # Will add all the items to the proccessing stack.
        for edge in graph.outEdges(item):
            if edge not in visited:
                stack.append(edge)

    return visited

# 6:47 - 8:14
# Implementation of a breath first search of a directed graph.
def bfs(graph, startVertex):
    if startVertex not in graph.graph:
        return "Vertex not in graph"
    # BFS works using stacks so implementing a queue.
    queue = [startVertex]
    # To store the visited values in.
    visited = []
    # Will run till there is nothing left to process.
    while len(queue) != 0:
        # Since a BFS works with stack we remove from the start of the list.
        item = queue.pop(0)

        # Checking if the item has already been visited before adding.
        if item not in visited:
            visited.append(item)

        # Will add all the items to the proccessing queue.
        for edge in graph.outEdges(item):
            if edge not in visited:
                queue.append(edge)

    return visited

# Next day 9:54 - 10:30
# Connected components will find all the connected components in the graph.
def connectedComponents(graph):
    connectedList = []
    # Going through all vertices.
    for vertex in graph.graph:
        # Getting the list from dfs
        list = dfs(graph, vertex)
        # If one element in the list that means it is unconnected.
        if len(list) == 1:
            continue
        else:
            # Going through the returned list then adding it to the connectedList if it isn't already added.
            for item in list:
                if item not in connectedList:
                    connectedList.append(item)
    print("The connected elements are")
    print(connectedList)

# 10:30 - 11:47
# Finds the hortest apth between the vertices in the function.
def shortestPath(graph, startVertex, endVertex):
    if startVertex not in graph.graph or endVertex not in graph.graph:
        return "One or both of the vertex does not exist. Add the vertex first before use."

    # BFS works using stacks so implementing a queue.
    queue = [startVertex]
    # To store the visited values in.
    visited = []
    paths = {startVertex: [startVertex]}
    # Will run till there is nothing left to process.
    while len(queue) != 0:
        # Since a BFS works with stack we remove from the start of the list.
        item = queue.pop(0)

        # Once item is found will return the current queue.
        if item == endVertex:
            print(f"The shortest path from {startVertex} and {endVertex}")
            print(paths[item])
            return

        # Checking if the item has already been visited before adding.
        if item not in visited:
            visited.append(item)

        # Will add all the items to the processing queue.
        for edge in graph.outEdges(item):
            if edge not in visited:
                queue.append(edge)
                # Keeping track of current queue.
                paths[edge] = paths[item] + [edge]

    print("No path exists between the two vertices.")
    return


graph1 = Graph()
graph1.addVertex(0)
graph1.addVertex(1)
graph1.addVertex(2)
graph1.addVertex(3)
graph1.addVertex(4)
graph1.addVertex(5)
graph1.addVertex(6)
graph1.addVertex(7)
graph1.addVertex(8)
graph1.addVertex(10)

graph1.addEdge(3, 1)
graph1.addEdge(3, 8)
graph1.addEdge(6, 1)
graph1.addEdge(5, 1)
graph1.addEdge(2, 2)
graph1.addEdge(1, 2)
graph1.addEdge(2, 3)
graph1.addEdge(3, 4)
graph1.addEdge(4, 5)
graph1.addEdge(5, 6)
graph1.addEdge(6, 7)
graph1.addEdge(7, 8)

print("Graph 1:")
print("Out Edges of 1")
print(graph1.outEdges(1))
print("Out Edges of 3")
print(graph1.outEdges(3))
print("In Edges of 8")
print(graph1.inEdges(8))
print("In Edges of 1")
print(graph1.inEdges(1))
connectedComponents(graph1)
shortestPath(graph1, 1, 8)


print("Breath First Search")
print(bfs(graph1, 1))

print("Depth First Search")
print(dfs(graph1, 1))

print("-" * 50)

graph2 = Graph()
graph2.addVertex(1)
graph2.addVertex(2)
graph2.addVertex(3)
graph2.addVertex(4)
graph2.addVertex(5)
graph2.addVertex(6)
graph2.addVertex(7)
graph2.addVertex(8)

graph2.addEdge(1, 2)
graph2.addEdge(2, 3)
graph2.addEdge(3, 4)
graph2.addEdge(4, 5)
graph2.addEdge(5, 3)
graph2.addEdge(3, 6)
graph2.addEdge(3, 7)
graph2.addEdge(3, 8)
graph2.addEdge(6, 5)
graph2.addEdge(7, 6)
graph2.addEdge(7, 8)
graph2.addEdge(2, 6)
graph2.addEdge(8, 1)

print("Graph 2:")
print("Out Edges of 3")
print(graph2.outEdges(3))
print("Out Edges of 7")
print(graph2.outEdges(7))
print("In Edges of 6")
print(graph2.inEdges(6))
print("In Edges of 8")
print(graph2.inEdges(8))
connectedComponents(graph2)
shortestPath(graph2, 1, 7)

print("Breath First Search")
print(bfs(graph2, 1))

print("Depth First Search")
print(dfs(graph2, 1))