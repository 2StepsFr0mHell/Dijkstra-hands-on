class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def add_neighbour(self, neighbour, distance):
        self.neighbours.append((neighbour, distance))  # tuple (immutable)


def create_graph(vlist, elist):
    graph = {}  # dictionnary of vertices where name is the key

    return graph
