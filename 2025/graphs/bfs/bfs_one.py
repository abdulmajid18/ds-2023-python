from .graphoop import GraphOOP
from collections import deque


def BFS(graph: GraphOOP, start_key):
    """Breadth-First Search starting from the given node"""
    if start_key not in graph.get_graph():
        return "Start node not found in graph"

    for vertex in graph.get_graph().values():
        vertex.color = "WHITE"
        vertex.distance = float("inf")
        vertex.predecessor = None

    start_vertex = graph.get_graph()[start_key]
    start_vertex.color = "GRAY"
    start_vertex.distance = 0
    start_vertex.predecessor = None

    queue = deque([start_vertex])

    while queue:
        u = queue.popleft()

        for neighbor in u.adj:
            if neighbor.colr == "WHITE":
                neighbor.color = "GRAY"
                neighbor.distance = u.distance + 1
                neighbor.predecessor = u
                queue.append(neighbor)
        u.color = "BLACK"

    return graph