import heapq

class Graph(object):
    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.distances = {}
        self.previous = {}

    def add_node(self, node):
        self.nodes.append(node)
        self.distances[node] = float('infinity')  # initialize distance to infinity
        self.previous[node] = None  # initialize previous node to None

    def add_edge(self, from_node, to_node, dist):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, dist))

        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[to_node].append((from_node, dist))


def Dijkstra(graph, start):
    graph.distances[start] = 0  # initialization for the source node

    is_visited = {node: False for node in graph.nodes}

    priorqueue = [(0, start)]  # ensures that nodes are explored in order of increasing distance, and here we add the start node with a distance of 0

    while len(priorqueue) > 0:  #  Extract node with the minimum distance from the priority queue
        _, u = heapq.heappop(priorqueue)

        if is_visited[u]:
            continue

        is_visited[u] = True

        # Explore neighbors and update distance
        for v, d in graph.edges[u]:
            if graph.distances[u] + d < graph.distances[v]:
                graph.distances[v] = graph.distances[u] + d
                graph.previous[v] = u
                heapq.heappush(priorqueue, (graph.distances[v], v))

    return graph.distances, graph.previous

graph = Graph()

#example of use

for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
    graph.add_node(i)

graph.add_edge('A', 'B', 1)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 3)
graph.add_edge('C', 'D', 1)
graph.add_edge('C', 'E', 5)
graph.add_edge('D', 'E', 1)
graph.add_edge('D', 'F', 1)
graph.add_edge('E', 'F', 2)
graph.add_edge('F', 'G', 3)

result, prev = Dijkstra(graph, 'A')

print(result)
print(prev)
