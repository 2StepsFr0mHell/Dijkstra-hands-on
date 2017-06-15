## Hello There!

In this exercise, you'll understand how the algorithm of Djikstra works. You will realize that it's quite simple to implement. You should be able to complete this playground in less than 15 minutes.

### The problem

You're in Salt Lake City and you want to go to Denver urgently. Unfortunately, you down know the shortest way to get there and you don't own a map. The only information you have is a list of distances by road between cities. How do you find the shortest route from Salt Lake City to Denver? 

### Analyzing the problem

The data you have actually correspond to what is called a graph:
- cities (nodes of the graph)
- roads between cities (edges of the graph)
- distances of the roads (weight of the edges)

The algorithm of Djikstra allows you to solve the problem of finding the shortest paths between nodes in a graph. Finding the shortest path between two specific nodes is then a subproblem.

The algorithm requires you to be able to find the neighbors of a node, whatever the node.

You'll then first convert the data into useful **City** objects defined by a *name* and a list of *neighbors*, each defined by a *name* and a *distance* from the city to its neighbor.

For example:
```
City {
	name: Salt Lake City
	neighbors: [(Provo, 50),
				(Rock Springs, 213)]
}```

@[Convert data into Nodes]({"stubs":["create_graph.py"], "command":"bash -c 'python -m unittest test_create_graph.TestCreate_graph.test_create_graph_all_vertices 2> /dev/null'"})

### Exploring the graph

The principle of the algorithm is to divide the graph into two list of nodes:
- on one side, the list of nodes for which now the actual shortest distance from the source, which we usually call "visited nodes". At the beginning, this list is empty.
- on the other side, the list of nodes for which we don't know the shortest distance from the source, called "unvisited nodes".

At each iteration of the algorithm, we'll consider a specific node from the second list: the one with the shortest distance from the source. 
Since this node has the current shortest distance from the source among all unvisited nodes, the shortest path surely passes only through visited nodes. To ensure the shortest distance from the source to the unvisited node cannot be improved, we have to make sure that the distance of the paths from the source to unvisited nodes through visited nodes are correctly updated.
Thus, we have to consider all unvisited neighbors of the specific node and update their distance from the source.


To get a better understanding at it, the best is to have a look at the algorithm in action.

@[Find the shortest path]({"stubs":["distance.py"], "command":"python -m unittest test_distance.TestFind_shortest_path.test_find_shortest_path 2> /dev/null"})

# What's next?

To be continued

We hope you've enjoyed discovering or rediscovering the Dijkstra algorithm. The source code of this hands-on on [GitHub](https://github.com/2StepsFr0mHell/Dijkstra-hands-on), please feel free to come up with proposals to improve it.
