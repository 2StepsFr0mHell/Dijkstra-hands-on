import create_graph as cg


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")

def create_graph(self):
    graph = {}
    for v in self.vertices:
        graph[v] = cg.Vertex(v)

    for e in self.edges:
        graph[e[0]].add_succ(e[1], e[2])
        graph[e[1]].add_succ(e[0], e[2])

    return graph

def is_equal(self, v1, vuser):
    if v1.name != vuser.name:
        return "Name differs", False
    set_succ = set(v1.successors)
    set_user_succ = set(vuser.successors)
    if len(set_succ) != len(set_user_succ):
        return "Different number of successors", False
    for s in set_user_succ:
        if s not in set_succ:
            return "Different successors", False
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
    self.graph = self.create_graph()
    self.edges[2] = ['A', 'E', 13]
    #self.vertices.add('Z')
    self.graph_to_check = cg.create_graph(self.vertices, self.edges)
    #self.vertices.remove('Z')

def test_create_graph_all_vertices(self):
    print("Test vertices names")
    try:
        # retrieve all names
        names = list(self.graph_to_check)
        # compare length
        self.assertEqual(len(names), len(self.vertices))
        # compare values
        names = set(names)
        for n in names:
            self.assertIn(n, self.vertices)
        success()

    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)

def test_create_graph_all_successors(self):
    print("Test successors")
    #for v in
    #msg, result = self.is_equal(self.graph, self.graph_to_check)
    #self.assertEqual(result, True)
    # for v in self.graph_to_check:
    # find equivalent node in
    # check that its successors are correct : name and distance
    # self.assertEqual(uppercase.to_upper('foo'), 'FOO', "Wrong uppercase value for foo")
    # self.assertEqual(uppercase.to_upper('Bar'), 'BAR')

if __name__ == "__main__":
    test_create_graph_all_vertices()