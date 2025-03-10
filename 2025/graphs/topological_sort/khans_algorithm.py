from collections import deque, defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)  # Directed edge u → v

    def topological_sort_bfs(self):
        in_degree = defaultdict(int)

        # calculate in-degree
        for node in self.graph:
            for neighbor in self.graph[node]:
                in_degree[neighbor] += 1

        queue = deque([node for node in self.graph if in_degree[node] == 0])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in self.graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result if len(result) == len(self.graph) else "Cycle detected!"


# Example Graph
g = Graph()
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort (BFS):", g.topological_sort_bfs())

from collections import deque, defaultdict


class GraphTwo:
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = set()  # Track all unique nodes

    def add_edge(self, u, v):
        self.graph[u].append(v)  # Directed edge u → v
        self.nodes.update([u, v])  # Track all nodes

    def topological_sort_bfs(self):
        in_degree = {node: 0 for node in self.nodes}  # Initialize in-degrees

        # Compute in-degrees
        for u in self.graph:
            for v in self.graph[u]:
                in_degree[v] += 1

        # Collect nodes with in-degree 0
        queue = deque([node for node in self.nodes if in_degree[node] == 0])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            # Reduce in-degree for neighbors
            for neighbor in self.graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If we processed all nodes, return result; otherwise, there’s a cycle
        return result if len(result) == len(self.nodes) else "Cycle detected!"


# Example Graph
g = GraphTwo()
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort (BFS):", g.topological_sort_bfs())
