from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            """DFS traversal marking all connected nodes as visited."""
            for neighbor in range(len(isConnected)):
                if isConnected[node][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        visited = set()
        provinces = 0

        for city in range(len(isConnected)):
            if city not in visited:
                dfs(city)  # Start a new DFS search
                provinces += 1  # A new connected component (province) found

        return provinces


def findCircleNumDFS(isConnected: List[List[int]]) -> int:
    def dfs(node, neighbors, visited, isConnected):
        for neighbor in range(neighbors):
            if isConnected[node][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor, neighbors, visited, isConnected)

    nodes = len(isConnected)
    neighbors = len(isConnected[0])

    visited = set()
    provinces = 0

    for node in range(nodes):
        if node not in visited:
            visited.add(node)
            dfs(node, neighbors, visited, isConnected)
            provinces += 1

    return provinces


def findCircleNumDFSA(isConnected: List[List[int]]) -> int:

    def dfs(node):
        for neighbor in range(len(isConnected[0])):
            if isConnected[node][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)

    provinces = 0
    visited = set()

    nodes = len(isConnected)

    for node in range(nodes):
        if node not in visited:
            dfs(node)
            provinces += 1

    return provinces


def findCircleNumBFS(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    visited = set()
    provinces = 0

    for i in range(n):
        if i not in visited:
            queue = deque([i])
            visited.add(i)

            while queue:
                node = queue.popleft()
                for neighbor in range(n):
                    if isConnected[node][neighbor] == 1 and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            provinces += 1

    return provinces

