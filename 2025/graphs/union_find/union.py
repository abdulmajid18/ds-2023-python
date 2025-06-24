def find(parent, u):
    if parent[u] != u:
        parent[u] = find(parent, parent[u])  # Path compression
    return parent[u]

def union(u, v, parent, rank):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u == root_v:
        return False  # already connected

    # Union by rank
    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_v] = root_u
        rank[root_u] += 1
    return True

def kruskal(n, edges):
    """
    n: number of nodes (0 to n-1)
    edges: list of tuples (weight, u, v)
    """
    parent = list(range(n))
    rank = [0] * n
    mst = []
    total_cost = 0

    # Sort edges by weight
    edges.sort()

    for weight, u, v in edges:
        if union(u, v, parent, rank):
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost
