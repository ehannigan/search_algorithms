class DijkstrasAlgorithm(object):
    def __init__(self):
        self.visited = {}  # holds {vertex: path_to_start}
        self.unvisited = {}  # holds {vertex: current_best_path_to_start}
        self.path = {}  # holds {vertex: previous vertex in best path so far

    def run(self, graph, start_vertex):
        for vertex in graph.vertices:
            if vertex is start_vertex:
                self.unvisited.append({node: 0})
            else:
                self.unvisited.append({node: np.inf})
            self.path[vertex] = None

        current_vertex = start_node

        while not Done:

            current_vertex_ = min(self.unvisited, key=self.unvisited.get)
            for neighbor in graph.edges[current_vertex]:
                # check distance to each neighbor and see if it reduces the neighbors distance to start
                if neighbor not in self.visited.keys():
                    distance_to_neighbor = graph.weights[(current_vertex, neighbor)]
                    neighbor_distance_to_start = self.visited[current_vertex]+distance_to_neighbor
                    if neighbor_distance_to_start < self.unvisited[neighbor]:
                        self.unvisited[neighbor] = neighbor_distance_to_start
                        self.path[neighbor] = current_vertex
                else:
                    continue
            # after all neighbors explored, add current vertex to list of visited vertices
            # remove node from unvisited list
            self.visited[current_vertex] = self.unvisited[current_vertex]
            del self.unvisited[current_vertex]



