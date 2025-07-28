from collections import deque

def bfs_adjacency_matrix(matrix: list[list[int]], start: int):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # Enqueue all unvisited neighbors
            for neighbor in range(len(matrix)):
                if matrix[node][neighbor] == 1 and neighbor not in visited:
                    queue.append(neighbor)

adj_matrix = [
    [0, 1, 1, 0, 0],  # Node 0 connected to 1, 2
    [1, 0, 0, 1, 0],  # Node 1 connected to 0, 3
    [1, 0, 0, 0, 1],  # Node 2 connected to 0, 4
    [0, 1, 0, 0, 0],  # Node 3 connected to 1
    [0, 0, 1, 0, 0]   # Node 4 connected to 2
]

# Run BFS starting from node 0
if __name__ == "__main__":
    bfs_adjacency_matrix(adj_matrix, 0)

