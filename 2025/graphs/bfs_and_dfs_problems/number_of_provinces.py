def findCircleNum(isConnected):
    """
    Finds the number of provinces in the given adjacency matrix.

    Approach:
    - Use DFS to explore all connected cities.
    - Maintain a 'visited' set to track visited cities.
    - Count the number of DFS calls, as each call represents a new province.

    Time Complexity: O(N^2) - We traverse the adjacency matrix once.
    Space Complexity: O(N) - Visited set stores up to N cities.

    :param isConnected: List[List[int]] - Adjacency matrix representing cities.
    :return: int - Number of provinces.
    """

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


# Example Usage
isConnected = [[1, 1, 0],
               [1, 1, 0],
               [0, 0, 1]]

print(findCircleNum(isConnected))  # Output: 2


from collections import deque

def findCircleNum_BFS(isConnected):
    visited = set()
    provinces = 0

    for city in range(len(isConnected)):
        if city not in visited:
            queue = deque([city])
            while queue:
                node = queue.popleft()
                for neighbor in range(len(isConnected)):
                    if isConnected[node][neighbor] == 1 and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            provinces += 1  # Found a new province

    return provinces
