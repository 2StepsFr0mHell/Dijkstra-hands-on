import heapq
import create_graph

def find_shortest_path(graph, source):
    graph[source].distance_to_source = 0

    unvisited_queue = [(graph[v].distance_to_source, v) for v in graph]
    heapq.heapify(unvisited_queue)

    while unvisited_queue:
        count_visited += 1
        u = heapq.heappop(unvisited_queue)
        current_city = graph[u[1]]
        current_city.visited = True

        for city_name in current_city.neighbours:
            # @TODO
            # get neighbor object which hasn't been visited yet
            # neighbor_city =

            # compute distance from source
            # new_dist=

            # if this distance is better than the current distance to source, then update neighbor_city


        # @Don't worry about that
        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(graph[v].distance_to_source, v) for v in graph if not graph[v].visited]
        heapq.heapify(unvisited_queue)