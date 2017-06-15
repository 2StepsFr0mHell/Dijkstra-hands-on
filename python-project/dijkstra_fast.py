
def find_shortest_path_to(graph, source, target_name):
    graph[source].distance_to_source = 0

    unvisited_queue = [(graph[v].distance_to_source, v) for v in graph]
    heapq.heapify(unvisited_queue)

    while unvisited_queue:
        count_visited += 1
        u = heapq.heappop(unvisited_queue)
        if DEBUG: print(u)
        current = graph[u[1]]
        if DEBUG: current.print_neighbours()
        current.visited = True

        for v in current.neighbours:
            next = graph[v[0]]
            # check if this vertex is the target, exit is so
            '''
            if next.name == target_name:
                print("Visited : %d" % count_visited)
                return
            '''                
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