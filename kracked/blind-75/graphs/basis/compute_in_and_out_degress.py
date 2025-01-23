from collections import defaultdict

def calculate_degrees(adj_list):
    n = len(adj_list)  # Number of vertices
    in_degree = [0] * n
    out_degree = [0] * n

    # Compute out-degrees and in-degrees
    for u in adj_list:
        out_degree[u] = len(adj_list[u])  # Out-degree = size of adjacency list
        for v in adj_list[u]:  # For each outgoing edge (u -> v)
            in_degree[v] += 1  # Increment in-degree for v

    return in_degree, out_degree


# Example Graph (Directed)
adj_list = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: [0],
}

in_degree, out_degree = calculate_degrees(adj_list)

print("In-Degree:", in_degree)   # Output: [1, 2, 2, 1]
print("Out-Degree:", out_degree) # Output: [2, 1, 1, 1]
