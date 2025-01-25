def dfs(graph, start_node):
    """
    Perform Depth-First Search (DFS) on a graph starting from the given node.

    Args:
    graph: Dictionary representing the adjacency list of the graph.
    start_node: The node to start DFS from.

    Returns:
    List of nodes in DFS traversal order.
    """
    visited = set()  # Use a set for efficient O(1) lookups
    stack = [start_node]  # Use list as stack
    traversal_order = []  # Store the order of visited nodes

    while stack:
        current_node = stack.pop()  # Pop the node from the stack

        if current_node not in visited:
            traversal_order.append(current_node)  # Add it to the traversal order
            visited.add(current_node)  # Mark the node as visited

            # Push all unvisited neighbors onto the stack
            for neighbor in reversed(graph[current_node]):  # Reverse to maintain order
                if neighbor not in visited:
                    stack.append(neighbor)

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
result
