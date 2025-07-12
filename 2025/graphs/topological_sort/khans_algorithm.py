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

from collections import defaultdict

def topological_sort(graph):  # Kahn's algorithm
    degree = defaultdict(int)
    topological_order = []

    # Compute in-degrees
    for source in graph:
        for destination in graph[source]:
            degree[destination] += 1

    # Collect all nodes with in-degree 0
    free_vertices = [vertex for vertex in graph if degree[vertex] == 0]

    while free_vertices:
        vertex = free_vertices.pop()  # Order can be influenced by pop strategy
        topological_order.append(vertex)
        for destination in graph[vertex]:
            degree[destination] -= 1
            if degree[destination] == 0:
                free_vertices.append(destination)

    # Detect cycle
    if len(topological_order) != len(graph):
        raise ValueError("There is a cycle in the graph!")

    return topological_order


from collections import defaultdict, deque

def topological_sort_bfs(graph):
    in_degree = defaultdict(int)

    # Ensure every node is in in_degree (including sources with 0 edges)
    for node in graph:
        in_degree[node] = 0

    # Compute in-degrees
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Start with nodes having in-degree 0
    queue = deque([node for node in graph if in_degree[node] == 0])
    res = []

    while queue:
        node = queue.popleft()
        res.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return res if len(res) == len(graph) else []


graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H', 'F'],
    'F': ['G'],
    'G': [],
    'H': []
}

print(topological_sort_bfs(graph))


def matrix_topo_sort(matrix):
    V = len(matrix)
    in_degree = [0] * V
    for i in range(V):
        for j in range(V):
            if matrix[i][j]:
                in_degree[j] += 1

    queue = deque([i for i in range(V) if in_degree[i] == 0])
    result = []

    while queue:
        u = queue.popleft()
        result.append(u)
        for v in range(V):
            if matrix[u][v]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

    if len(result) != V:
        return []  # Cycle detected
    return result

# Example
matrix = [
    [0, 0, 0, 0, 0, 0],  # 0
    [0, 0, 0, 0, 0, 0],  # 1
    [0, 0, 0, 1, 0, 0],  # 2
    [0, 1, 0, 0, 0, 0],  # 3
    [0, 1, 0, 0, 0, 0],  # 4
    [1, 0, 1, 0, 0, 0],  # 5
]
print(matrix_topo_sort(matrix))


from collections import defaultdict, deque

def topo_sort_adj_list(graph, V):
    in_degree = defaultdict(int)  # Automatically 0 for unseen keys

    # Step 1: Compute in-degrees
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # Step 2: Collect nodes with in-degree 0
    queue = deque([i for i in range(V) if in_degree[i] == 0])
    result = []

    # Step 3: Kahn’s Algorithm
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(result) != V:
        return []  # Cycle detected
    return result


from collections import deque, defaultdict

def detect_cycle_topo_sort_kahn(vertices, edges):
    graph = defaultdict(list)
    indegree = defaultdict(int)

    # Initialize graph
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
        if u not in indegree:
            indegree[u] = 0

    queue = deque([node for node in indegree if indegree[node] == 0])
    visited_count = 0

    while queue:
        node = queue.popleft()
        visited_count += 1
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return visited_count != len(indegree)

def topological_sort_dfs(vertices, edges):
    from collections import defaultdict

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = set()
    in_path = set()
    result = []

    def dfs(node):
        if node in in_path:
            return True  # cycle detected
        if node in visited:
            return False

        in_path.add(node)
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        in_path.remove(node)
        visited.add(node)
        result.append(node)  # Add after visiting children (post-order)
        return False

    for node in range(vertices):
        if node not in visited:
            if dfs(node):
                return None  # cycle detected → topological sort not possible

    return result[::-1]  # reverse to get topological order

class TopoSort:
    def dfs(self,graph, vertex, stack, visited):
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                self.dfs(graph, neighbor, stack, visited)

        stack.append(vertex)



    def topological_sort(self, graph):
        stack = []
        visited = set()

        for vertex in graph:
            if vertex not in visited:
                self.dfs(graph, vertex, stack, visited)

        ordering = []
        while stack:
            ordering.append(stack.pop())
        return ordering
