class Graph:
    def __init__(self):
        self.graph = {}  # Adjacency list (key: vertex, value: list of adjacent vertices)

    def add_node_edge(self, u, v):
        """Adds an edge between nodes u and v (undirected graph)"""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def get_graph(self):
        return self.graph

    def display(self):
        """Prints the adjacency list of the graph"""
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")


# Example Usage
g = Graph()
g.add_node_edge(1, 2)
g.add_node_edge(1, 3)
g.add_node_edge(2, 4)
g.add_node_edge(3, 4)
g.add_node_edge(4, 5)

print(g.get_graph())
g.display()
