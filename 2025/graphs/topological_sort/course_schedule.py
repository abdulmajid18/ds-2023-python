from collections import deque, defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)  # Adjacency list for graph representation

        # Build the graph from prerequisites
        for course_a, course_b in prerequisites:
            graph[course_a].append(course_b)

        def bfs(graph):
            in_degree = defaultdict(int)  # Track in-degrees of nodes (courses)

            # Calculate in-degree for each course
            for node in graph:
                for neighbor in graph[node]:
                    in_degree[neighbor] += 1

            # Initialize queue with courses having no prerequisites (in-degree == 0)
            queue = deque([node for node in range(numCourses) if in_degree[node] == 0])
            result = []  # List to store topologically sorted nodes

            # BFS to process all nodes with zero in-degree
            while queue:
                node = queue.popleft()
                result.append(node)

                # Decrease the in-degree of neighboring nodes
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            # If result contains all nodes, then no cycle exists
            return len(result) == numCourses

        # Call BFS to check if we can finish all courses
        return bfs(graph)

class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0  # To count the number of processed courses

        while queue:
            course = queue.popleft()
            count += 1
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return count == numCourses  # If all courses are processed, return True


from collections import defaultdict


class SolutionDFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)

        visited = [0] * numCourses  # 0: unvisited, 1: visiting, 2: visited

        def dfs(course):
            if visited[course] == 1:  # Currently visiting this course
                return False  # Cycle detected
            if visited[course] == 2:  # Already visited, no cycle
                return True

            visited[course] = 1  # Mark as visiting
            for pre in graph[course]:
                if not dfs(pre):  # Visit all prerequisites
                    return False
            visited[course] = 2  # Mark as visited
            return True

        for course in range(numCourses):
            if visited[course] == 0:  # If the course is unvisited
                if not dfs(course):  # If a cycle is detected
                    return False

        return True

from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for dest, src in prerequisites:
        graph[src].append(dest)
        in_degree[dest] += 1

    # Queue for nodes with in-degree 0
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    visited = 0

    while queue:
        course = queue.popleft()
        visited += 1
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return visited == numCourses


def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    for dest, src in prerequisites:
        graph[src].append(dest)

    visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited

    def dfs(course):
        if visited[course] == 1:  # cycle detected
            return False
        if visited[course] == 2:
            return True

        visited[course] = 1  # mark as visiting
        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False
        visited[course] = 2  # mark as visited
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False
    return True
