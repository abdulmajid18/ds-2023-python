class Vertex:
    def __init__(self, id):
        self.id = id
        self.distance = float("inf")
        self.color = None

    def __repr__(self):
        return f"Vertex({self.id}, distance={self.distance}, color={self.color})"


class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight  # Edge attribute

    def __repr__(self):
        return f"Edge({self.u} -> {self.v}, weight={self.weight})"


# Example Usage
# Create vertices
vertices = [Vertex(i) for i in range(4)]  # Create vertices 0, 1, 2, 3

edges = [
    Edge(vertices[0], vertices[1], 5),
    Edge(vertices[1], vertices[2], 3),
    Edge(vertices[2], vertices[3], 2),
]

# Update vertex attribute
vertices[0].distance = 0  # Source vertex distance = 0

# Display graph data
print("Vertices:")
for v in vertices:
    print(v)

print("\nEdges:")
for e in edges:
    print(e)