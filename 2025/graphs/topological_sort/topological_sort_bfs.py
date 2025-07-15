from collections import defaultdict, deque

def topo_sort(edges, num_nodes):
    """
    Perform topological sort (BFS / Kahn's algorithm).

    :param edges: List of (u, v) directed edges
    :param num_nodes: Number of nodes (0 to num_nodes-1)
    :return: List of nodes in topologically sorted order,
             or raises ValueError if a cycle is detected.
    """
    adj = defaultdict(list)
    indegree = [0] * num_nodes

    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1

    q = deque([u for u in range(num_nodes) if indegree[u] == 0])
    topo = []

    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    if len(topo) != num_nodes:
        raise ValueError("Graph has at least one cycle")
    return topo

if __name__ == "__main__":
    edges = [(5,2), (5,0), (4,0), (4,1), (2,3), (3,1)]
    order = topo_sort(edges, 6)
    print("Topological order:", order)
