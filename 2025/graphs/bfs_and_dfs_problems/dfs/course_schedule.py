def canFinish(numCourses, prerequisites):
    from collections import defaultdict
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[b].append(a)

    visiting = set()
    visited = set()

    def dfs(u):
        if u in visiting:
            return False  # cycle found
        if u in visited:
            return True   # already confirmed acyclic

        visiting.add(u)
        for v in graph.get(u, []):
            if not dfs(v):
                return False
        visiting.remove(u)
        visited.add(u)
        return True

    return all(dfs(i) for i in range(numCourses))
