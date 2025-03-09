class Node:
    def __init__(self, id):
        self._id = id
        self._neighbors = []

    @property
    def id(self):
        return self._id

    @property
    def neighbors(self):
        return self._neighbors

    def add_neighbor(self, neighbor):
        self._neighbors.append(neighbor)  # Add a neighbor connection

    def __hash__(self):
        return hash(self._id)  # Make Node hashable for set operations

    def __eq__(self, other):
        return isinstance(other, Node) and self._id == other._id


def dfs_iterative_stack(start_node: Node):
    stack = [start_node]  # Stack for DFS
    visited = set()  # Set to track visited nodes

    while stack:
        node = stack.pop()  # Get the last inserted node (LIFO)
        if node not in visited:
            print(f"Visiting Node: {node.id}")
            visited.add(node)

            # Add neighbors to stack (reverse order for correct DFS behavior)
            for neighbor in reversed(node.neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)


# Example Graph Construction
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.add_neighbor(node2)
node1.add_neighbor(node3)
node2.add_neighbor(node4)
node3.add_neighbor(node4)

# Run Iterative DFS
dfs_iterative_stack(node1)
