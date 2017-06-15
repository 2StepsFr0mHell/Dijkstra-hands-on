class Vertex:
    def __init__(self, name):
        self.name= name
        self.successors= []
        self.distance_to_source= None

    def add_succ(self, successor, distance):
        self.successors.append((successor, distance))   # tuple (immutable)


def createGraph(vlist, elist):
    graph= {}   # dictionnary
    # @TODO
    return graph