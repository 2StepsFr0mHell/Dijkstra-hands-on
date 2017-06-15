import heapq
import create_graph

def find_shortest_path(graph, source):
    graph[source].distance_to_source = 0

    unvisited_queue = [(graph[v].distance_to_source, v) for v in graph]
    heapq.heapify(unvisited_queue)

    while unvisited_queue:
        count_visited += 1
        u = heapq.heappop(unvisited_queue)
        current = graph[u[1]]
        current.visited = True

        for v in current.neighbours:
            # get neighbour object
            # next=
            # if it has already been visited, continue

            # compute distance to source (don't forgate to add distance from current node to next)
            # new_dist=
            # if this distance is better, then update next: distance and prev
            #if new_dist < next.distance_to_source:
            #    next.distance_to_source = 
            #    next.prev = 
            '''
            next = graph[v[0]]
            if next.visited:
                continue
            new_dist = current.distance_to_source + v[1]

            if new_dist < next.distance_to_source:
                next.distance_to_source = new_dist
                next.prev = current
            '''
        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(graph[v].distance_to_source, v) for v in graph if not graph[v].visited]
        heapq.heapify(unvisited_queue)