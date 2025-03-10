from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)  # Directed edge u -> v

    def topological_sort_dfs(self):
        visited = set()
        stack = []

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for neighbor in self.graph[node]:
                dfs(neighbor)

            stack.append(node)  # Postorder: Add after visiting neighbors

        # Call DFS for every unvisited node
        for node in list(self.graph.keys()):
            if node not in visited:
                dfs(node)

        return stack[::-1]  # Reverse to get topological order


# Example Graph
g = Graph()
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort (DFS):", g.topological_sort_dfs())