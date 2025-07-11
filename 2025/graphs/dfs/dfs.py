result = []

def dfs(graph, root):
    if root not in visited:
        visited.add(root)
        result.append(root)
        for neighbor in graph[root]:
            dfs(graph, neighbor)

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1, 5],
    5: [4]
}

# Start DFS from node 0
start_node = 0
visited = set()
dfs(graph, start_node)

print("DFS traversal order:", result)

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    res = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            res.append(node)
            # Add neighbors in reverse order to match recursive DFS order
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return res
