from unittest import TestCase
import create_graph as cg


class TestCreate_graph(TestCase):
    def send_msg(self, channel, msg):
        print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


    def success(self):
        print("TECHIO> success true")


    def fail(self):
        print("TECHIO> success false")

    def create_graph(self):
        graph = {}
        for v in self.vertices:
            graph[v] = cg.City(v)

        for e in self.edges:
            graph[e[0]].add_neighbor(e[1], e[2])
            graph[e[1]].add_neighbor(e[0], e[2])

        return graph

    def is_equal(self, v1, vuser):
        if v1.name != vuser.name:
            return "Name differs", False
        set_succ = set(v1.neighbours)
        set_user_succ = set(vuser.neighbours)
        if len(set_succ) != len(set_user_succ):
            return "Different number of neighbours", False
        for s in set_user_succ:
            if s not in set_succ:
                return "Different neighbours", False
        return "Perfect", True


    def setUp(self):
        self.vertices = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
        # Attention : undirected graph
        self.edges = [['A', 'B', 5],
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
        self.correct_graph = self.create_graph()
        #self.edges[2] = ['A', 'E', 13]
        #self.vertices.add('Z')
        self.graph_to_check = cg.create_graph(self.vertices, self.edges)
        #self.vertices.remove('Z')

    def test_create_graph_all_vertices(self):
        #print("Test vertices names")
        # retrieve all names
        if not self.graph_to_check:
            self.fail()
            self.send_msg("Oops! ", "It seems the graph is not initialized at all")
            return
        try:   
            for key in self.correct_graph:
                print(key)
                self.assertIn(key, self.graph_to_check.keys(), "It seems the graph does not contain all nodes")
        except AssertionError as e:
            self.fail()
            self.send_msg("Oops! ", e)
            return
        try:
            for node in self.correct_graph.values():
                msg, result = self.is_equal(node, self.graph_to_check[node.name])
                print(msg)
                self.assertTrue(result, "One node has a wrong neighbor")
            self.success()
            self.send_msg("Congrats! The graph of cities is properly initialized.")
        except AssertionError as e:
            self.fail()
            self.send_msg("Oops! ", e)