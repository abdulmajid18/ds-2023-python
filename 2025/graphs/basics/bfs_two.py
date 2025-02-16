from collections import deque


# BFS function
def bfs(graph, source):
    # Initialize vertex attributes
    color = {v: "WHITE" for v in graph}  # WHITE: undiscovered
    distance = {v: float("inf") for v in graph}  # Infinite distance initially
    predecessor = {v: None for v in graph}  # NIL predecessor

    # Source vertex initialization
    color[source] = "GRAY"  # Source is discovered
    distance[source] = 0  # Distance from source to itself is 0
    predecessor[source] = None  # No predecessor for the source

    # Queue initialization
    queue = deque([source])  # Add the source to the queue

    # BFS loop
    while queue:
        u = queue.popleft()  # Dequeue the front vertex

        # Process all adjacent vertices
        for v in graph[u]:
            if color[v] == "WHITE":  # If the vertex is undiscovered
                color[v] = "GRAY"  # Mark it as discovered
                distance[v] = distance[u] + 1  # Update distance
                predecessor[v] = u  # Set predecessor
                queue.append(v)  # Enqueue the vertex

        color[u] = "BLACK"  # Mark the vertex as fully explored

    # Return BFS result
    return color, distance, predecessor


# Graph adjacency list
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}

# Run BFS
color, distance, predecessor = bfs(graph, "A")

# Output BFS attributes
print("Vertex Colors:", color)
print("Distances:", distance)
print("Predecessors:", predecessor)
