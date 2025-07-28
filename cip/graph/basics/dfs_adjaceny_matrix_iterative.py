def dfs_adjacency_matrix(matrix: list[list[int]], node: int, visited: set[int]):
    stack = [node]
    while stack:
        node = stack.pop()  # Get the top node
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)

            # Add all unvisited neighbors to the stack (reverse order for correct DFS order)
            for neighbor in range(len(matrix) - 1, -1, -1):
                if matrix[node][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)


if "__main__" == __name__:
    adj_matrix = [
        [0, 1, 1, 0, 0],  # Node 0 connected to 1, 2
        [1, 0, 0, 1, 0],  # Node 1 connected to 0, 3
        [1, 0, 0, 0, 1],  # Node 2 connected to 0, 4
        [0, 1, 0, 0, 0],  # Node 3 connected to 1
        [0, 0, 1, 0, 0]  # Node 4 connected to 2
    ]
    visited_nodes = set()
    dfs_adjacency_matrix(adj_matrix, 0, visited_nodes)

