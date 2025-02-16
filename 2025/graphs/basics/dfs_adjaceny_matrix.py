def dfs_recursive(matrix, node, visited: set):
    """
    Performs Depth-First Search (DFS) on a graph represented as an adjacency matrix.

    Approach:
    1. **Mark the node as visited** by adding it to the `visited` set.
    2. **Process the node** (print it or perform other operations).
    3. **Recursively visit all its unvisited neighbors**:
       - Loop through all possible neighbors (0 to N-1).
       - If `matrix[node][neighbor] == 1` (indicating a connection) and `neighbor` is not visited,
         call `dfs_recursive` on the neighbor.

    Time Complexity:
    - **O(V²)** in the worst case (since we iterate through all V neighbors in an adjacency matrix).

    Space Complexity:
    - **O(V)** for the recursion stack in the worst case (for a fully connected graph).

    Parameters:
    - matrix (list of lists): The adjacency matrix representing the graph.
    - node (int): The starting node for DFS traversal.
    - visited (set): A set to keep track of visited nodes to prevent infinite loops.

    Example:
    Input Graph (Adjacency Matrix):
        [
            [1, 1, 0, 1],  # Node 0 is connected to 1 and 3
            [1, 1, 0, 1],  # Node 1 is connected to 0 and 3
            [0, 0, 1, 0],  # Node 2 is isolated (only connected to itself)
            [1, 1, 0, 1]   # Node 3 is connected to 0 and 1
        ]

    DFS Call: dfs_recursive(graph, 0, visited)
    Output: 0 1 3
    """
    if node in visited:  # Explicit base case
        return

    visited.add(node)  # Mark node as visited
    print(node, end=" ")

    for neighbor in range(len(matrix)):
        if matrix[node][neighbor] == 1 and neighbor not in visited:
            dfs_recursive(matrix, neighbor, visited)


# Example usage
graph = [
    [1, 1, 0, 1],  # Node 0 is connected to 1 and 3
    [1, 1, 0, 1],  # Node 1 is connected to 0 and 3
    [0, 0, 1, 0],  # Node 2 is isolated (only connected to itself)
    [1, 1, 0, 1]  # Node 3 is connected to 0 and 1
]

visited_ = set()
print("DFS Recursive Traversal:")
dfs_recursive(graph, 0, visited_)
