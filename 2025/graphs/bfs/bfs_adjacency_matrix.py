from collections import deque


def bfs_adj_matrix(graph, start):
    n = len(graph)  # Number of nodes
    visited = [False] * n  # Track visited nodes
    queue = deque([start])  # Initialize queue
    visited[start] = True  # Mark start node as visited

    while queue:
        node = queue.popleft()
        print(node, end=" ")  # Process node

        # Traverse all possible neighbors
        for neighbor in range(n):
            if graph[node][neighbor] == 1 and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True


# Example Graph as an Adjacency Matrix
graph = [
    [0, 1, 1, 0, 0, 0],  # Node 0 -> connected to 1, 2
    [1, 0, 0, 1, 1, 0],  # Node 1 -> connected to 0, 3, 4
    [1, 0, 0, 0, 0, 1],  # Node 2 -> connected to 0, 5
    [0, 1, 0, 0, 0, 0],  # Node 3 -> connected to 1
    [0, 1, 0, 0, 0, 0],  # Node 4 -> connected to 1
    [0, 0, 1, 0, 0, 0],  # Node 5 -> connected to 2
]

# Start BFS from node 0
bfs_adj_matrix(graph, 0)
