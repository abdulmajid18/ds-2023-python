class Vertex:
    def __init__(self, key):
        self.key = key
        self.color = "WHITE"
        self.distance = float("inf")
        self.predecessor = None

    def __repr__(self):
        return f"Vertex({self.key})"
