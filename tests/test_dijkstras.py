import unittest
from dijkstras import DijkstrasAlgorithm
from dijkstras import Graph


class TestDijkstras(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
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




if __name__ == '__main__':
    unittest.main()
