class Graph(object):
    def __init__(self, vertices=[], edges={}, weights={}):
        self.vertices = vertices
        self.edges = edges
        self.weights = weights

    def add_vertice(self, name):
        self.vertices.append(name)

    def add_directed_edge(self, start_vertex, end_vertex, weight):
        if start_vertex not in self.edges.keys():
            self.edges[start_vertex] = []
        self.edges[start_vertex].append(end_vertex)
        self.weights[(start_vertex, end_vertex)] = weight

    def add_undirected_edge(self, vertex_1, vertex_2, weight):
        if vertex_1 not in self.edges.keys():
            self.edges[vertex_1] = []
        if vertex_2 not in self.edges.keys():
            self.edges[vertex_2] = []
        self.edges[vertex_1].append(vertex_2)
        self.edges[vertex_2].append(vertex_1)
        self.weights[(vertex_1, vertex_2)] = weight
        self.weights[(vertex_2, vertex_1)] = weight
