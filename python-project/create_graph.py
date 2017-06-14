class Vertex:
    def __init__(self, name):
        self.name= name
        self.successors= []
        self.distance_to_source= None

    def add_succ(self, successor, distance):
        self.successors.append((successor, distance))   # tuple (immutable)

    '''
    def printNeighbours(self):
        print("Neighbours of %s"%self.name)
        for s in self.successors:
            print("\t%s %d"%(s[0], s[1]))
    '''

def createGraph(vlist, elist):
    graph= {}   # dictionnary
    '''
    for v in vlist:
        edges[v] = Edge(v)
    for e in edges:
        print(e)

    for e in elist:
        edges[e[0]].add_succ(e[1], e[2])
        edges[e[1]].add_succ(e[0], e[2])

    for v in graph:
        graph[v].printNeighbours()
    '''
    return graph


'''
def main():    
    # Graph definition
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    # Attention : undirected graph
    edges = [['A', 'B', 5],
             ['A', 'D', 3],
             ['A', 'E', 12],
             ['A', 'F', 5],
             ['B', 'D', 1],
             ['B', 'G', 2],
             ['C', 'E', 1],
             ['C', 'F', 16],
             ['D', 'E', 1],
             ['D', 'G', 1],
             ['E', 'F', 2]
             ]
    nodes= createGraph(vertices, edges)



if __name__ == '__main__':
    main()
'''    