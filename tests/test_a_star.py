import unittest
from search_algorithms import DijkstrasAlgorithm
from search_algorithms import Graph


class TestDijkstras(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # graph taken from: https://www.youtube.com/watch?v=pVfj6mxhdMw
        vertices = {'A', 'B', 'C', 'D', 'E'}
        cls.graph = Graph(vertices)
        cls.graph.add_undirected_edge('A', 'B', 6)
        cls.graph.add_undirected_edge('A', 'D', 1)
        cls.graph.add_undirected_edge('B', 'C', 5)
        cls.graph.add_undirected_edge('B', 'D', 2)
        cls.graph.add_undirected_edge('B', 'E', 2)
        cls.graph.add_undirected_edge('C', 'E', 5)
        cls.graph.add_undirected_edge('D', 'E', 1)

    def test_run_dijkstras(self):
        dijkstras = DijkstrasAlgorithm()
        dijkstras.run(self.graph, 'A')
        shortest_path = dijkstras.get_shortest_path('C')
        self.assertTrue(shortest_path == ['A', 'D', 'E', 'C'])

if __name__ == '__main__':
    unittest.main()
