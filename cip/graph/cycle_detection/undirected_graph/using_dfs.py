def has_cycle_adj_list(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True
    return False




def has_cycle_adj_matrix(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n

    def dfs(node, parent):
        visited[node] = True
        for neighbor in range(n):
            if adj_matrix[node][neighbor]:
                if not visited[neighbor]:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
        return False

    for node in range(n):
        if not visited[node]:
            if dfs(node, -1):
                return True
    return False