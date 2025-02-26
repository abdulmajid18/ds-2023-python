from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        # Build adjacency list (fix incorrect tuple appending)
        for i, (a, b) in enumerate(equations):
            adj[a].append((b, values[i]))  # a → b with weight values[i]
            adj[b].append((a, 1 / values[i]))  # b → a with reciprocal weight

        # BFS function
        def bfs(start, end):
            if start not in adj or end not in adj:
                return -1.0
            if start == end:
                return 1.0  # Fix: if start == end, return 1.0

            queue = deque([(start, 1.0)])  # Fix: Move queue inside bfs
            visited = set()

            while queue:
                node, cur_product = queue.popleft()
                if node == end:
                    return cur_product

                visited.add(node)

                for neighbor, value in adj[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, cur_product * value))

            return -1.0  # Fix: should return -1.0 instead of -1

        # Process each query
        return [bfs(a, b) for a, b in queries]


# Example Usage
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

sol = Solution()
print(sol.calcEquation(equations, values, queries))
