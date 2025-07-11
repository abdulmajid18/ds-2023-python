
def construct_graph(vertices, edges):
    graph = {i : [] for i in range(V)}
    for u, v in edges:
        graph[u].append(v)

    print("Graph adjacency list:")
    for u in graph:
        print(f"  {u} -> {graph[u]}")

    return graph



def detect_cycle_dfs(vertices, edges):
    if not isinstance(vertices, dict):
        graph = construct_graph(vertices, edges)
    else:
        graph = vertices

    def dfs(node):
        visited.add(node)
        in_path.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in in_path:
                return True
        in_path.remove(node)
        return False

    visited = set()
    in_path = set()

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False


if __name__ == "__main__":
    V = 4
    edges = [
        (0, 1),
        (1, 2),
        (2, 0),  # introduces cycle 0 → 1 → 2 → 0
        (2, 3)
    ]
    has_cycle = detect_cycle_dfs(V, edges)
    print("\nCycle detected?" , has_cycle)