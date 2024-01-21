# Dijkstra's Algorithm 

This code implements `Dijkstra's algorithm` for finding the shortest paths from a source node to all other nodes in a weighted graph.

# Code Overview
## Class graph

This will represent a graph with nodes, edges, distances between nodes and previous nodes

- 'add_node': Adds a node to the graph, initializing its distance to infinity and previous node to None.
- 'add_edge': Adds an edge between two nodes with a given distance.

## Dijkstra's Algorithm

The `Dijkstra` function takes a `Graph` and a starting node as input and calculates the shortest distances and previous nodes using Dijkstra's algorithm.

1. Initialize the start node distance to 0
2. Use a priority queue (`priorqueue`) to keep track of nodes in increasing order of distance.
3. For each unvisited neighbor of the current node, update the distance if a shorter path is found.
4. Continue the process until all the nodes are visited.

## Example Usage

An example graph is created with nodes 'A' through 'G' and corresponding edges.

![Graph](https://github.com/samAK02/Applied-Math-Problems/assets/131418700/920823d9-eea8-4d1c-be22-4dc419aaf436)

## Output
The result of this code is the following:

![output](https://github.com/samAK02/Applied-Math-Problems/assets/131418700/32357c3a-d241-49b0-ad02-8fbc9f44bed6)

- The minimal distance to reach each vertexe from the starting node
- The path for each node, for example:
    - The distance from A to A is 0 so the path is inexistant
    - The minimal distance to reach B is from A 
    - The minimal distance to reach C is from B which strats from A
    - The minimal distance to reach D is from B which starts from A
