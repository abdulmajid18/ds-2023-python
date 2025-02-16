def dfs_iterative(matrix, start):
    """
    Performs Depth-First Search (DFS) on a graph represented as an adjacency matrix using an iterative approach.

    Approach:
    1. **Use a stack** (LIFO) instead of recursion.
    2. **Push the start node** onto the stack.
    3. While the stack is not empty:
       - Pop a node from the stack.
       - If the node is not visited:
         - Mark it as visited.
         - Process the node (print it or perform other operations).
         - **Push all its unvisited neighbors** onto the stack in reverse order (to maintain correct DFS order).

    Time Complexity:
    - **O(V²)** in the worst case (since we iterate through all V neighbors in an adjacency matrix).

    Space Complexity:
    - **O(V)** in the worst case (if all nodes are stored in the stack at some point).

    Parameters:
    - matrix (list of lists): The adjacency matrix representing the graph.
    - start (int): The starting node for DFS traversal.

    Example:
    Input Graph (Adjacency Matrix):
        [
            [1, 1, 0, 1],  # Node 0 is connected to 1 and 3
            [1, 1, 0, 1],  # Node 1 is connected to 0 and 3
            [0, 0, 1, 0],  # Node 2 is isolated (only connected to itself)
            [1, 1, 0, 1]   # Node 3 is connected to 0 and 1
        ]

    DFS Call: dfs_iterative(graph, 0)
    Output: 0 1 3
    """
    visited = set()  # Track visited nodes
    stack = [start]  # Stack for DFS

    while stack:
        node = stack.pop()  # Get the top node
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)

            # Add all unvisited neighbors to the stack (reverse order for correct DFS order)
            for neighbor in range(len(matrix) - 1, -1, -1):
                if matrix[node][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)


# Example usage
graph = [
    [1, 1, 0, 1],  # Node 0 is connected to 1 and 3
    [1, 1, 0, 1],  # Node 1 is connected to 0 and 3
    [0, 0, 1, 0],  # Node 2 is isolated (only connected to itself)
    [1, 1, 0, 1]  # Node 3 is connected to 0 and 1
]

print("\nDFS Iterative Traversal:")
dfs_iterative(graph, 0)
