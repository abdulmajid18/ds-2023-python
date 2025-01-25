def dfs(graph, node, visited=None):
    """
    Perform Depth-First Search (DFS) on a graph starting from the given node.

    Args:
    graph: Dictionary representing the adjacency list of the graph.
    node: The node to start DFS from.
    visited: Set of visited nodes (used for recursion).

    Returns:
    List of nodes in DFS traversal order.
    """
    if visited is None:
        visited = set()  # Initialize the visited set if not provided

    visited.add(node)  # Mark the node as visited
    traversal_order = [node]  # Start traversal order with the current node

    # Recurse on all the neighbors of the node
    for neighbor in graph[node]:
        if neighbor not in visited:
            traversal_order.extend(dfs(graph, neighbor, visited))  # Recur and extend the traversal list

    return traversal_order


# Example Graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Call DFS
result = dfs(graph, 'A')
print("DFS Traversal Order:", result)
