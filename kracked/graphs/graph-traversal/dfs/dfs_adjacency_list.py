graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1, 5],
    5: [4]
}

result = []

def dfs_recursive(graph, start):
    if start not in visited:
        visited.add(start)
        result.append(start)
        v = graph[start]
        for u in v:
            dfs_recursive(graph, u)

start_node = 0
visited = set()
dfs_recursive(graph, start_node)

print("DFS traversal order:", result)

def dfs_iterative(graph, start):
    stack = [start]
    res = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            res.append(node)
            v = graph[node]
            for u in reversed(v):
                stack.append(u)
    return res

start_node = 0
visited = set()
res = dfs_iterative(graph, start_node)
print("DFS iterative:", res)