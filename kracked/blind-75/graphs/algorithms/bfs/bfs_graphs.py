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

from collections import deque


def bfs2(graph, start_node):
    """
    Perform Breadth-First Search (BFS) on a graph starting from the given node.

    Args:
    graph: Dictionary representing the adjacency list of the graph.
    start_node: The node to start BFS from.

    Returns:
    List of nodes in BFS traversal order.
    """
    visited = set()  # Use a set for efficient O(1) lookups
    queue = deque([start_node])  # Use deque for efficient queue operations
    traversal_order = []  # Store the order of visited nodes

    while queue:
        current_node = queue.popleft()  # Dequeue the next node
        if current_node not in visited:
            traversal_order.append(current_node)
            visited.add(current_node)  # Mark the node as visited

            # Enqueue all unvisited neighbors
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)

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

# Call BFS
result = bfs(graph, 'A')
print("BFS Traversal Order:", result)


from collections import deque

def bfs3(graph, start):
    # Initialize the visited set and distance dictionary
    visited = set()
    distance = {}

    # Initialize the queue with the starting node
    queue = deque([start])
    visited.add(start)
    distance[start] = 0  # Distance to the starting node is 0

    # Perform BFS
    while queue:
        current = queue.popleft()
        print(f"Processing node: {current}, Distance from start: {distance[current]}")

        # Explore neighbors of the current node
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[current] + 1  # Update the distance
                queue.append(neighbor)  # Add to queue for further processing

    return distance  # Return distances for all reachable nodes

# Example Graph (Adjacency List)
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

# Perform BFS from starting node 0
start_node = 0
distances = bfs3(graph, start_node)

# Output the distances from the starting node
print("\nShortest distances from the starting node:")
for node, dist in distances.items():
    print(f"Node {node}: Distance {dist}")
