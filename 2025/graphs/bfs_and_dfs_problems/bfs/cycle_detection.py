n = 5
edges = [[0,1], [1,2], [2,3], [3,4], [4,1]]

from collections import defaultdict

def has_cycle_dfs_undirected(n, edges):
    graph = defaultdict(list)

    for node, neighbor in edges:
        graph[node].append(neighbor)
        graph[neighbor].append(node)

    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in range(n):
        if node not in visited:
            if dfs(node, -1):
                return True

    return False


# Output: True (Cycle exists)
# print(has_cycle_bfs(n, edges))
print(has_cycle_dfs_undirected(n, edges))




from collections import defaultdict, deque

def has_cycle_bfs_undirected(n, edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def bfs(start):
        queue = deque([(start, -1)])  # (node, parent)
        visited.add(start)

        while queue:
            node, parent = queue.popleft()

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    # If neighbor is visited and not parent → cycle
                    return True
        return False

    for node in range(n):
        if node not in visited:
            if bfs(node):
                return True

    return False
