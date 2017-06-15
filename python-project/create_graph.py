import collections

Neighbour = collections.namedtuple('Neighbour', 'name distance')

class City:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, name, distance):
        self.neighbors.append(Neighbor(name= name, distance= distance)) 

def create_graph(vlist, elist):
    graph = {}  # dictionnary of cities where name is the key
    # @TODO
    return graph

