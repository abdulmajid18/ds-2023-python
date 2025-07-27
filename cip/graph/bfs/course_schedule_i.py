from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):
    # Build graph
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for a, b in prerequisites:
        graph[b].append(a)
        in_degree[a] += 1

    # Start with courses that have no prerequisites
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    taken = 0

    while queue:
        course = queue.popleft()
        taken += 1
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return taken == numCourses
