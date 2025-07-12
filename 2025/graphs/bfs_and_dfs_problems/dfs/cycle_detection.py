def detect_cycle_dfs(vertices, edges=None):
    """
    Detects a cycle in a directed graph using DFS.

    Args:
        vertices: A dict representing the adjacency list,
                  or an int/list of nodes (to construct the graph).
        edges: List of (from, to) edges, required if vertices is not a dict.

    Returns:
        True if there is a cycle, False otherwise.
    """

    def construct_graph(n, edges):
        graph = {i: [] for i in range(n)} if isinstance(n, int) else {i: [] for i in n}
        for u, v in edges:
            graph[u].append(v)
        return graph

    # Build the graph if needed
    if not isinstance(vertices, dict):
        if edges is None:
            raise ValueError("Edges must be provided if vertices is not a dict.")
        graph = construct_graph(vertices, edges)
    else:
        graph = vertices

    visited = set()
    in_path = set()

    def dfs(node):
        visited.add(node)
        in_path.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in in_path:
                return True
        in_path.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False


from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices  # Number of vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:  # Found a back edge
                return True

        rec_stack[v] = False
        return False

    def is_cyclic(self):
        visited = [False] * self.V
        rec_stack = [False] * self.V

        for node in range(self.V):
            if not visited[node]:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True
        return False

# Example usage:
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)  # Introduces a cycle

print("Graph has a cycle:" if g.is_cyclic() else "Graph has no cycle.")

def detect_cycle_topo_sort_dfs(vertices, edges):
    graph = {i: [] for i in range(vertices)}
    for u, v in edges:
        graph[u].append(v)

    state = [0] * vertices  # 0=unvisited, 1=visiting, 2=visited

    def dfs(node):
        if state[node] == 1:  # Found a back edge → cycle
            return True
        if state[node] == 2:
            return False

        state[node] = 1
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        state[node] = 2
        return False

    for node in range(vertices):
        if state[node] == 0:
            if dfs(node):
                return True
    return False

class TopologicalSorter:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.rec_stack = set()
        self.stack = []
        self.has_cycle = False

    def dfs(self, node):
        self.visited.add(node)
        self.rec_stack.add(node)

        for neighbor in self.graph.get(node, []):
            if neighbor not in self.visited:
                if self.dfs(neighbor):
                    return True  # Cycle detected
            elif neighbor in self.rec_stack:
                return True  # Cycle found

        self.rec_stack.remove(node)
        self.stack.append(node)
        return False

    def sort(self):
        for node in self.graph:
            if node not in self.visited:
                if self.dfs(node):
                    self.has_cycle = True
                    return None  # Cycle detected

        # Reverse the stack to get topological order
        return self.stack[::-1]


if __name__ == "__main__":
    V = 4
    edges = [
        (0, 1),
        (1, 2),
        (2, 0),  # introduces cycle 0 → 1 → 2 → 0
        (2, 3)
    ]
    has_cycle = detect_cycle_dfs(V, edges)
    print("\nCycle detected?" , has_cycle)