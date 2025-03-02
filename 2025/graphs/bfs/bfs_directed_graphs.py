from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}  # Adjacency list (key: vertex, value: list of adjacent vertices)

    def add_node_edge(self, u, v):
        """Adds a directed edge from node u to node v"""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []  # Ensure v exists in the graph

        self.graph[u].append(v)  # Only add edge from u to v (directed)

    def get_graph(self):
        return self.graph

    def display(self):
        """Prints the adjacency list of the graph"""
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

    def bfs(self, start):
        """Performs Breadth-First Search from a given start vertex"""
        if start not in self.graph:
            return "Start vertex not found in graph"

        # Initialize BFS structures
        visited = {vertex: False for vertex in self.graph}  # Track visited nodes
        distance = {vertex: float("inf") for vertex in self.graph}  # Distance from start
        predecessor = {vertex: None for vertex in self.graph}  # Store predecessor

        queue = deque([start])
        visited[start] = True
        distance[start] = 0

        while queue:
            u = queue.popleft()  # Dequeue the front vertex

            for neighbor in self.graph[u]:  # Explore neighbors
                if not visited[neighbor]:  # If not visited
                    visited[neighbor] = True
                    distance[neighbor] = distance[u] + 1
                    predecessor[neighbor] = u
                    queue.append(neighbor)

        return distance, predecessor  # Return BFS results


# Example Usage for Directed Graph
g = Graph()
g.add_node_edge(1, 2)
g.add_node_edge(1, 3)
g.add_node_edge(2, 4)
g.add_node_edge(3, 4)
g.add_node_edge(4, 5)  # Directed edge from 4 to 5 (not vice versa)

print("Adjacency List (Directed Graph):")
g.display()

# Running BFS from node 1
distances, predecessors = g.bfs(1)

print("\nBFS Results:")
for node in distances:
    print(f"Node {node}: Distance = {distances[node]}, Predecessor = {predecessors[node]}")

from collections import deque


def bfs(graph, start):
    visited = set()  # Set to track visited nodes
    queue = deque([start])  # Initialize queue with start node
    visited.add(start)

    while queue:
        node = queue.popleft()  # Dequeue front node
        print(node, end=" ")  # Process node

        for neighbor in graph[node]:  # Explore neighbors
            if neighbor not in visited:
                queue.append(neighbor)  # Enqueue unvisited neighbor
                visited.add(neighbor)  # Mark as visited


# Example graph (Adjacency List Representation)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

# Start BFS from node 'A'
bfs(graph, 'A')
