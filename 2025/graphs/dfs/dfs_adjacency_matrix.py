def dfs_adjacency_matrix(matrix: list[list[int]], node: int, visited: set[int]):
    if node not in visited:
        print(f"Visiting Node: {node}")
        visited.add(node)

        for neighbor, is_edge in enumerate(matrix[node]):
            if is_edge == 1 and neighbor not in visited:
                dfs_adjacency_matrix(matrix, neighbor, visited)


# Example Graph (Adjacency Matrix)
adj_matrix = [
    [0, 1, 1, 0],  # Node 0 is connected to 1 and 2
    [1, 0, 0, 1],  # Node 1 is connected to 0 and 3
    [1, 0, 0, 1],  # Node 2 is connected to 0 and 3
    [0, 1, 1, 0]   # Node 3 is connected to 1 and 2
]

visited_nodes = set()
dfs_adjacency_matrix(adj_matrix, 0, visited_nodes)
