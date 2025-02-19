# Adjacency List Representation
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}


# Function to print neighbors of a vertex
def print_neighbors(vertex):
    if vertex in graph:
        print(f"Neighbors of {vertex}: {graph[vertex]}")
    else:
        print(f"Vertex {vertex} not found in the graph!")


# Demo: Print neighbors of each vertex
print("Adjacency List Representation:")
for vertex in graph:
    print("Vertex ", vertex)
    print_neighbors(vertex)

# Adjacency Matrix Representation
# A = 0, B = 1, C = 2, D = 3
matrix = [
    [0, 1, 1, 0],  # A
    [0, 0, 0, 1],  # B
    [0, 0, 0, 1],  # C
    [0, 0, 0, 0],  # D
]


# Function to print the adjacency matrix
def print_matrix(matrix):
    print("Adjacency Matrix Representation:")
    for row in matrix:
        print(row)


# Demo: Print the adjacency matrix
print_matrix(matrix)


# Check if there's an edge from vertex u to vertex v
def has_edge(u, v, vertex_map):
    u_idx = vertex_map[u]
    v_idx = vertex_map[v]
    return matrix[u_idx][v_idx] == 1


vertex_map = {"A": 0, "B": 1, "C": 2, "D": 3}
print(has_edge("A", "B", vertex_map))  # True
print(has_edge("A", "D", vertex_map))  # False
