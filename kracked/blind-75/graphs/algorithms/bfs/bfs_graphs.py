# Initialize visited list and queue
visited = []  # Keeps track of visited nodes
queue = []  # Keeps track of nodes to be visited next


# Function for BFS
def bfs(visited, graph, start_node):
    """
    Perform Breadth-First Search (BFS) on a graph starting from the given node.

    Args:
    visited: List to keep track of visited nodes.
    graph: Dictionary representing the adjacency list of the graph.
    start_node: The node to start BFS from.

    Returns:
    None. Prints the nodes in BFS traversal order.
    """
    visited.append(start_node)  # Mark the start node as visited
    queue.append(start_node)  # Enqueue the start node

    print("BFS Traversal:")
    while queue:
        # Dequeue a node and print it
        current_node = queue.pop(0)
        print(current_node, end=" ")

        # Enqueue all unvisited neighbors of the current node
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


# Example Graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Call BFS
bfs(visited, graph, 'A')
