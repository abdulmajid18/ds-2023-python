from collections import deque


def bfs_adjacency_list(graph, start):
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
bfs_adjacency_list(graph, 'A')