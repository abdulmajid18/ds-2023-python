from collections import deque


def bfs_adjacency_list(graph, start):
    visited = set()  # Set to track visited nodes
    queue = deque([start])  # Initialize queue with start node
    visited.add(start)

    while queue:
        node = queue.popleft()  # Dequeue front node
        print(node, end=" ")  # Process node

        for neighbor in graph[node]:  # Explore neighbors
            if neighbor not in visited:
                queue.append(neighbor)  # Enqueue unvisited neighbor
                visited.add(neighbor)  # Mark as visited


# Example graph (Adjacency List Representation)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

# Start BFS from node 'A'
bfs_adjacency_list(graph, 'A')

from collections import deque


def bfs_one(graph, root):
    visited = set()
    queue = deque([root])
    res = []
    while queue:
        qLen = len(queue)

        for i in range(qLen):
            current_node = queue.popleft()
            if current_node not in visited:
                visited.add(current_node)
                res.append(current_node)
            for new_node in graph[current_node]:
                if new_node not in visited:
                    queue.append(new_node)
    return res

def bfs_two(graph, root):
    visited = set()
    queue = deque([root])
    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for v in graph[vertex]:
            if v not in visited:
                queue.append(v)
    print(visited)
    return visited
if __name__ == "__main__":

    graph = {
        0: [1,2,3],
        1: [0,2],
        2:[0,1],
        3: [0],
        4: [2]
    }

    res = bfs_one(graph, 0)
    print(res)
    res_2 = bfs_two(graph, 0)
    print(res_2)