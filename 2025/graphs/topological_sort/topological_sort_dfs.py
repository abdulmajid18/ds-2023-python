

from collections import defaultdict, deque

def topological_sort(graph):
    visited = set()
    stack = deque()

    def dfs(node):
        visited.add(node)
        for nbr in graph.get(node, []):
            if nbr not in visited:
                dfs(nbr)
        stack.appendleft(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return list(stack)

from collections import deque

def topological_sort_two(graph):
    visited = set()
    result = deque()

    def dfs(u):
        visited.add(u)
        for v in graph.get(u, []):
            if v not in visited:
                dfs(v)
        result.appendleft(u)

    for u in graph:
        if u not in visited:
            dfs(u)

    return list(result)


def topological_sort_three(graph):
    visited = set()
    result = []

    def dfs(u):
        visited.add(u)
        for v in graph.get(u, []):
            if v not in visited:
                dfs(v)
        result.append(u)

    for u in graph:
        if u not in visited:
            dfs(u)
    ordering = []
    while result:
        ordering.append(result.pop())
    return ordering

if __name__ == "__main__":
    graph = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['d'],
        'd': ['e'],
        'e': []
    }
    print(topological_sort(graph))  # e.g. ['a', 'c', 'b', 'd', 'e']

    print(topological_sort_two(graph))  # e.g. ['a', 'c', 'b', 'd', 'e']
    print(topological_sort_three(graph))