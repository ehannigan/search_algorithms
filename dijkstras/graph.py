class Graph(object):
    def __init__(self, vertices=[], edges={}, weights={}):
        self.vertices = vertices
        self.edges = edges
        self.weights = weights

    def add_vertice(self, name):
        self.vertices.append(name)

    def add_directed_edge(self, start_vertex, end_vertex, weight):
        self.edges[start_vertex] = end_vertex
        self.weights[(start_vertex, end_vertex)] = weight

    def add_undirected_edge(self, vertex_1, vertex_2, weight):
        self.edges[vertex_1].append(vertex_2)
        self.edges[vertex_2].append(vertex_1)
        self.weights[(vertex_1, vertex_2)] = weight
