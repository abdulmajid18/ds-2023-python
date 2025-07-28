def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph.get(node, []):
            dfs_recursive(graph, neighbor, visited)