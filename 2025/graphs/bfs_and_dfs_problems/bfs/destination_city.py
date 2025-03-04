from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city_set = {path[0] for path in paths}

        for _,second_city in paths:
            if second_city not in city_set:
                return second_city
        return ""

class Solution2:
    def destCity(self, paths: List[List[str]]) -> str:
        from collections import defaultdict, deque
        graph =   defaultdict(list)
        for city_1, city_2 in paths:
            graph[city_1].append(city_2)


        def bfs(graph):
            q = deque([paths[0][0]])

            while q:
                node = q.popleft()
                if node not in graph:
                    return node
                for i in graph[node]:
                    q.append(i)

            return ""
        return bfs(graph)