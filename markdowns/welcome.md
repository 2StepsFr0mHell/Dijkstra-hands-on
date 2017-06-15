# Welcome!

You have probably heard once in your life the name of Dijkstra. This is an algorithm used to find the shortest paths between nodes -- or vertices -- in a graph. Let's get our hands dirty.


# Let's analyze the problem

So you're given what we call a graph with the list of its nodes and its edges. What is easier to work with is actually a list of nodes and for each node a list of "neighbors" or "successors".

@[Convert data into useful objects]({"stubs": ["create_graph.py"], "command": "python3 test_create_graph.py"})
@[Test unittest: create_graph]({"stubs":["create_graph.py"], "command":"test_create_graph.TestCreate_graph.test_create_graph_all_vertices"})

# Exploring the graph

@[Update the distance to the source]({"stubs": ["distance.py"], "command": "python3 test_distance.py"})

# Finding the shortest path

@[Keep the shortest path]({"stubs": ["distance.py"], "command": "python3 test_distance.py"})

# The whole Dijkstra Algorithm

@[Write your own Dijkstra]({"stubs": ["distance.py"], "command": "python3 test_distance.py"})

# What's next?

We hope you've enjoyed discovering or rediscovering the Dijkstra algorithm. The source code of this hands-on on [GitHub](https://github.com/2StepsFr0mHell/Dijkstra-hands-on), please feel free to come up with proposals to improve it.
