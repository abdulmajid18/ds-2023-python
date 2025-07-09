from collections import deque


def bfs_distance(graph, root, target):
    from collections import deque

    distance = {root: 0}
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node == target:
            return distance[node]
        for neighbor in graph[node]:
            if neighbor not in distance:
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

    return -1


def bfs_distance_two(graph, root, target):
    visited = set()
    queue = deque([(root, 0)])  # (node, distance)

    while queue:
        vertex, dist = queue.popleft()
        if vertex == target:
            return dist
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append((neighbor, dist + 1))

    return -1


# Sample graph (undirected)
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1, 5],
    4: [2],
    5: [3]
}

# Test the function
root = 0
target = 5
print(f"Distance from {root} to {target}:", bfs_distance(graph, root, target))

