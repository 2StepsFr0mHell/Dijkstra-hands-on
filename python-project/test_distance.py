from unittest import TestCase
import sys
import distance as di
import heapq
import collections

Neighbour = collections.namedtuple('Neighbour', 'name distance')

class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self.prev = None  # predecessor (built when looking for shortest path)
        self.visited = False
        self.distance_to_source = sys.maxsize

    def add_neighbour(self, neighbour, distance):
        self.neighbours.append(Neighbour(name=neighbour, distance=distance))  # tuple (immutable)


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

    @staticmethod
    def find_shortest_path(graph, source):
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
                next = graph[v.name]
                if next.visited:
                    continue
                new_dist = current.distance_to_source + v.distance

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

    def get_shortest_path_to(self, target):
        if target.prev:
            return self.get_shortest_path_to(target.prev) + " -> " + target.name
        else:
            return target.name

    def setUp(self):
        # Graph definition
        self.vertices = ('Springfield', 'Saint-Louis', 'Louisville', 'Cincinnati', 'Pittsburgh',
                         'Indianapolis', 'Chicago', 'Fort Wayne', 'Cleveland', 'Columbus')
        # self.vertices = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
        # Attention : undirected graph
        self.edges = [['Saint-Louis', 'Springfield', 5],
                      ['Saint-Louis', 'Indianapolis', 8],
                      ['Saint-Louis', 'Louisville', 12],
                      ['Springfield', 'Chicago', 10],
                      ['Springfield', 'Indianapolis', 8],
                      ['Chicago', 'Fort Wayne', 6],
                      ['Chicago', 'Indianapolis', 7],
                      ['Indianapolis', 'Fort Wayne', 3],
                      ['Indianapolis', 'Columbus', 6],
                      ['Indianapolis', 'Louisville', 4],
                      ['Louisville', 'Cincinnati', 2],
                      ['Cincinnati', 'Columbus', 3],
                      ['Fort Wayne', 'Cleveland', 5],
                      ['Cleveland', 'Pittsburgh', 4],
                      ['Cleveland', 'Columbus', 5],
                      ['Pittsburgh', 'Columbus', 8]
                      ]
        self.graph = self.create_graph()
        self.graph_to_check = self.create_graph()
        self.find_shortest_path(self.graph, 'Saint-Louis')
        di.find_shortest_path(self.graph_to_check, 'Saint-Louis')

    def test_find_shortest_path(self):
        for v in self.graph_to_check.values():
            if v.distance_to_source != self.graph[v.name].distance_to_source:
                msg = "Distance to source is wrong for " + v.name + " have " + str(
                    self.graph[v.name].distance_to_source) + " have " + str(v.distance_to_source)
                self.send_msg("Oops! ", msg)
                self.fail()
                return
        correct_path = self.get_shortest_path_to(self.graph['Pittsburgh'])
        path = self.get_shortest_path_to(self.graph_to_check['Pittsburgh'])
        if correct_path != path:
            msg = "Path from Saint-Louis to Cleveland is wrong, want " + correct_path + " found " + path
            self.send_msg("Oops! ", msg)
            self.fail()
        else:
            msg = "Shortest path is " + correct_path + " Length= " + str(self.graph['Pittsburgh'].distance_to_source)
            self.send_msg("Congrats!", msg)