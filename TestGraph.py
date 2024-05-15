import unittest
from Graph import Graph, floyd_warshall, find_graph_center, load_graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        # Setup a graph instance for each test
        self.graph = Graph()
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_vertex("C")
        self.graph.add_edge("A", "B", 1)
        self.graph.add_edge("B", "C", 2)
        self.graph.add_edge("A", "C", 3)

    def test_add_vertex(self):
        self.graph.add_vertex("D")
        self.assertIn("D", self.graph.vertices)
        self.assertEqual(len(self.graph.vertices), 4)

    def test_add_edge(self):
        self.graph.add_edge("C", "A", 1)
        src_index = self.graph.vertices["C"]
        dest_index = self.graph.vertices["A"]
        self.assertEqual(self.graph.matrix[src_index][dest_index], 1)

    def test_remove_edge(self):
        self.graph.remove_edge("A", "C")
        src_index = self.graph.vertices["A"]
        dest_index = self.graph.vertices["C"]
        self.assertEqual(self.graph.matrix[src_index][dest_index], float('inf'))

    def test_update_edge(self):
        self.graph.update_edge("A", "C", 2)
        src_index = self.graph.vertices["A"]
        dest_index = self.graph.vertices["C"]
        self.assertEqual(self.graph.matrix[src_index][dest_index], 2)

    def test_floyd_warshall(self):
        distances = floyd_warshall(self.graph)
        self.assertEqual(distances[self.graph.vertices["A"]][self.graph.vertices["C"]], 3)
        self.assertEqual(distances[self.graph.vertices["B"]][self.graph.vertices["A"]], float('inf'))

    def test_find_graph_center(self):
        distances = floyd_warshall(self.graph)
        center_index = find_graph_center(distances)
        center_city = list(self.graph.vertices.keys())[center_index]
        self.assertEqual(center_city, "B")

if __name__ == '__main__':
    unittest.main()
