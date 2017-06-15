class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def add_neighbour(self, neighbour, distance):
        self.neighbours.append((neighbour, distance))  # tuple (immutable)


def create_graph(vlist, elist):
    graph = {}  # dictionnary of vertices where name is the key
    '''
    for v in vlist:
        graph[v] = Vertex(v)

    for e in elist:
        graph[e[0]].add_neighbour(e[1], e[2])
        graph[e[1]].add_neighbour(e[0], e[2])
    '''
    return graph
