from collections import deque

class Node:
    def __init__(self, id):
        self._id = id
        self._neighbors = []

class Graph:
    def __init__(self):
        self.visited = set()

    def bfs(self, start_node):
        queue = deque([start_node])

        # Mark the starting node as visited
        self.visited.add(start_node)

        while queue:
            # Dequeue a node from the front of the queue
            current_node = queue.popleft()

            # Process the dequeued node
            print(current_node.id)

            for neighbor in current_node.neighbors:
                if neighbor not in self.visited:
                    # Enqueue unvisited neighbors
                    queue.append(neighbor)
                    # Mark the neighbor as visited
                    self.visited.add(neighbor)

# Create Nodes and add neighbors
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.add_neighbor(node2)
node2.add_neighbor(node3)

# Create a Graph object and perform BFS
g = Graph()
g.bfs(node1)