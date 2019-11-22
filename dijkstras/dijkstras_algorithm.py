import math


class DijkstrasAlgorithm(object):
    def __init__(self):
        self.visited = {}  # holds {vertex: best distance to start}
        self.unvisited = {}  # holds {vertex: current best distance to start}
        self.previous_vertex = {}  # holds {vertex: previous vertex in best path so far}
        self.start_vertex = None

    def run(self, graph, start_vertex, goal=None):
        self.start_vertex = start_vertex
        for vertex in graph.vertices:
            if vertex is start_vertex:
                self.unvisited[vertex] = 0
            else:
                self.unvisited[vertex] = math.inf
            self.previous_vertex[vertex] = None

        goal_reached = False
        while self.unvisited or goal_reached:  # while there are unvisited vertices
            # select unvisited vertex that has the shortest distance to the goal
            # initially, this will be the start_vertex
            current_vertex = min(self.unvisited, key=self.unvisited.get)

            # if we gave a goal node, check to see if it has been reached
            if goal and current_vertex == goal:
                goal_reached = True
                continue

            for neighbor in graph.edges[current_vertex]:
                # check distance to each (unvisited) neighbor and see if it reduces the neighbors distance to start
                if neighbor not in self.visited.keys():
                    distance_to_neighbor = graph.weights[(current_vertex, neighbor)]
                    neighbor_distance_to_start = self.unvisited[current_vertex]+distance_to_neighbor
                    if neighbor_distance_to_start < self.unvisited[neighbor]:
                        self.unvisited[neighbor] = neighbor_distance_to_start
                        self.previous_vertex[neighbor] = current_vertex
                else:
                    continue
            # after all neighbors explored, add current vertex to list of visited vertices
            self.visited[current_vertex] = self.unvisited[current_vertex]
            # remove node from unvisited list
            del self.unvisited[current_vertex]
        return True

    def get_shortest_path(self, goal_vertex):
        path = [goal_vertex]
        vertex = goal_vertex
        while vertex is not self.start_vertex:
            next_vertex = self.previous_vertex[vertex]
            path.append(next_vertex)
            vertex = next_vertex
        path.reverse()
        return path



