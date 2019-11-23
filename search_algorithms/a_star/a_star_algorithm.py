import math


class AStarAlgorithm(object):
    def __init__(self, heuristic=None):
        self.visited = {}  # holds {vertex: best distance to start}
        self.unvisited = {}  # holds {vertex: current best distance to start g(vertex)}
        self.f_c = {}  # holds {vertex: g(vertex) + h(vertex, goal_vertex)
        self.previous_vertex = {}  # holds {vertex: previous vertex in best path so far}
        self.start_vertex = None
        self.goal_vertex = None
        self.heuristic = heuristic

    def run(self, graph, start_vertex, goal_vertex):
        """
        a_star requires a goal vertex for the heuristic
        Args:
            graph: Graph object
            start_vertex: str representing the name of the start_vertex
            goal_vertex: str representing the name of the goal_vertex

        """
        self.start_vertex = start_vertex
        self.goal_vertex = goal_vertex
        for vertex in graph:
            if vertex is start_vertex:
                self.unvisited[vertex] = 0
            else:
                self.unvisited[vertex] = math.inf
        goal_reached = False
        while self.unvisited and (not goal_reached):
            unvisited_f = [(key, value+self.heuristic(key, goal_vertex)) for key,value in self.unvisited.items()]
            current_vertex = min(unvisited_f, key=lambda t: t[1])
            for neighbor in graph[current_vertex].edges:
                if neighbor in self.unvisited.keys():
                    current_to_neighbor = graph.weights[(current_vertex, neighbor)]
                    g = self.unvisited[neighbor] + current_to_neighbor
                    if g < self.unvisited[neighbor]:
                        self.unvisited[neighbor] = g
                        self.f_c[neighbor] = g + self.heuristic(neighbor, goal_vertex)
                        self.previous_vertex[neighbor] = current_vertex
                if neighbor is goal_vertex:
                    goal_reached = True
                    break

    def get_shortest_path(self, goal_vertex):
        path = [goal_vertex]
        vertex = goal_vertex
        while vertex is not self.start_vertex:
            next_vertex = self.previous_vertex[vertex]
            path.append(next_vertex)
            vertex = next_vertex
        path.reverse()
        return path



