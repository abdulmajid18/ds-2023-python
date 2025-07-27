from collections import defaultdict, deque

def topo_bfs(graph: dict):
    in_degree = defaultdict(int)

    # Step 1: Calculate in-degrees
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # Step 2: Initialize queue with nodes having in-degree 0
    queue = deque([node for node in graph if in_degree[node] == 0])
    result = []

    # Step 3: Kahn's algorithm
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # Step 4: Check for cycles
    if len(result) != len(graph):
        return []  # Cycle detected
    return result





if "__main__" == __name__:
    adj_list = {
        0: [],
        1: [],
        2: [3],
        3: [1],
        4: [0, 1],
        5: [0, 2]
    }

    res = topo_bfs(adj_list)
    print(res)
    ...