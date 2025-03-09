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
        return hash(self._id)  # Make Node hashable

    def __eq__(self, other):
        return isinstance(other, Node) and self._id == other._id  # Equality check


def dfs_adjacency_list(node: Node, visited: set[Node]):
    if node not in visited:
        print(f"Visiting Node: {node.id}")
        visited.add(node)

        for neighbor in node.neighbors:  # Use a different variable
            dfs_adjacency_list(neighbor, visited)


# Example usage
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.add_neighbor(node2)
node2.add_neighbor(node3)

visited_nodes = set()
dfs_adjacency_list(node1, visited_nodes)
