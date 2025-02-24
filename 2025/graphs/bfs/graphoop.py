from vertex import Vertex


class GraphOOP:
    def __init__(self):
        self.graph = {}  # {int: [Vertex, Vertex, ...]}

    def add_node_edge(self, u, v):
        """Adds an edge between Vertex(u) and Vertex(v)"""
        if u not in self.graph:
            self.graph[u] = Vertex(u)
        if v not in self.graph:
            self.graph[v] = Vertex(v)

        # Ensure adjacency list exists
        if not hasattr(self.graph[u], "adj"):
            self.graph[u].adj = []
        if not hasattr(self.graph[v], "adj"):
            self.graph[v].adj = []

        # Add to adjacency list
        self.graph[u].adj.append(self.graph[v])
        self.graph[v].adj.append(self.graph[u])

    def get_graph(self):
        return self.graph

    def display(self):
        """Prints the adjacency list of the graph"""
        for node in self.graph:
            print(f"{node} -> {[neighbor.key for neighbor in self.graph[node].adj]}")


# Example Usage
g = GraphOOP()
g.add_node_edge(1, 2)
g.add_node_edge(1, 3)
g.add_node_edge(2, 4)
g.add_node_edge(3, 4)
g.add_node_edge(4, 5)

g.display()
