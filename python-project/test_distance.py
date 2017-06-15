from unittest import TestCase
import sys
import distance as di
import heapq

class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self.prev = None  # predecessor (built when looking for shortest path)
        self.visited = False
        self.distance_to_source = sys.maxsize

    def add_neighbour(self, neighbour, distance):
        self.neighbours.append((neighbour, distance))  # tuple (immutable)

class TestFind_shortest_path(TestCase):

    @staticmethod
    def send_msg(channel, msg):
        print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

    @staticmethod
    def success():
        print("TECHIO> success true")

    @staticmethod
    def fail():
        print("TECHIO> success false")

    def create_graph(self):
        graph = {}
        for v in self.vertices:
            graph[v] = Vertex(v)

        for e in self.edges:
            graph[e[0]].add_neighbour(e[1], e[2])
            graph[e[1]].add_neighbour(e[0], e[2])

        return graph

    def find_shortest_path(self, graph, source):
        graph[source].distance_to_source = 0
        count_visited = 0

        unvisited_queue = [(graph[v].distance_to_source, v) for v in graph]
        heapq.heapify(unvisited_queue)

        while unvisited_queue:
            count_visited += 1
            u = heapq.heappop(unvisited_queue)
            current = graph[u[1]]
            current.visited = True

            for v in current.neighbours:
                next = graph[v[0]]
                if next.visited:
                    continue
                new_dist = current.distance_to_source + v[1]

                if new_dist < next.distance_to_source:
                    next.distance_to_source = new_dist
                    next.prev = current

            # Rebuild heap
            # 1. Pop every item
            while len(unvisited_queue):
                heapq.heappop(unvisited_queue)
            # 2. Put all vertices not visited into the queue
            unvisited_queue = [(graph[v].distance_to_source, v) for v in graph if not graph[v].visited]
            heapq.heapify(unvisited_queue)


    def setUp(self):
        # Graph definition
        self.vertices = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
        # Attention : undirected graph
        self.edges = [['A', 'B', 10],
                 ['A', 'C', 5],
                 ['A', 'D', 8],
                 ['B', 'G', 2],
                 ['B', 'E', 12],
                 ['C', 'F', 7],
                 ['C', 'G', 4],
                 ['D', 'F', 5],
                 ['G', 'E', 5],
                 ['F', 'E', 7]
                 ]
        self.graph = self.create_graph()
        self.graph_to_check = self.create_graph()
        self.find_shortest_path(self.graph, 'A')
        di.find_shortest_path(self.graph_to_check, 'A')

    def test_find_shortest_path(self):
        print("test find shortest_path")
        for v in self.graph_to_check.values():
            if v.distance_to_source != self.graph[v.name].distance_to_source:
                msg= "Distance to source is wrong for "+v.name+" want "+str(self.graph[v.name].distance_to_source)+" have "+str(v.distance_to_source)
                self.send_msg("Oops! ", msg)
