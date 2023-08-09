"""Test bellmanford implementation."""

# pylint: disable = R0904
import unittest
import logging
import sys
from structures.graph import graph
from shortestpath.bellmanford import bellmanford


class BellmanfordTest(unittest.TestCase):
    """Class Bellmanford."""

    def setUp(self):
        """Setup."""
        debug = True
        my_graph = {'A': [('B', 3)], 'B': [('C', 4)], 'C': [('D', 10)], 'E': [('F', 9)], 'F': []}
        self.graph = graph.Graph(my_graph)
        self.graph.add_edge('D', 'E', 1)
        self.bellmangraph = bellmanford.BellmanFord(self.graph)
        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("BellmanfordTestLog")

    def test_init(self):
        """1. Test bellmanford constructor."""
        print(self.bellmangraph.bellgraph.graph_dict['A'])

    def test_bellmanford(self):
        """2. Test bellmanford function."""
        print(self.bellmangraph.bellman_ford('C'))

    def test_bellmanford_2(self):
        """3. Test bellmanford function."""
        self.graph.add_edge('F', 'E', -100)
        self.bellmangraph = bellmanford.BellmanFord(self.graph)
        print(self.bellmangraph.bellman_ford('A'))

    def test_bellmanford_3(self):
        """4. Test bellmanford function."""
        my_graph = {'A': [('B', 3), ('C', 4), ('D', 5)], 'B': [], 'C': [], 'D': []}
        self.graph = graph.Graph(my_graph)
        self.bellmangraph = bellmanford.BellmanFord(self.graph)
        print(self.bellmangraph.bellman_ford('A'))

    def test_bellmanford_4(self):
        """5. Test bellmanford function."""
        my_graph = {'A': [('B', 3), ('C', 4), ('D', 5)], 'B': [], 'C': [], 'D': []}
        self.graph = graph.Graph(my_graph)
        self.bellmangraph = bellmanford.BellmanFord(self.graph)
        print(self.bellmangraph.bellman_ford('C'))

    def test_bellmanford_5(self):
        """6. Test bellmanford function."""
        my_graph = {'A': [('B', 3), ('C', 4)], 'B': [('C', -1)], 'C': [], 'D': []}
        self.graph = graph.Graph(my_graph)
        self.bellmangraph = bellmanford.BellmanFord(self.graph)
        print(self.bellmangraph.bellman_ford('A'))

    def test_bellmanford_6(self):
        """7. Test disconnected bellmanford function."""
        my_graph = {'A': [('C', 3), ('D', 4)], 'B': [('C', -1)], 'C': [('D', -2)], 'D': []}
        self.graph = graph.Graph(my_graph)
        self.bellmangraph = bellmanford.BellmanFord(self.graph)
        print(self.bellmangraph.bellman_ford('A'))

    def test_bellmanford_7(self):
        """8. Test bellmanford function."""
        my_graph = {'A': [('C', 3), ('D', 4)], 'B': [('C', -1)], 'C': [('D', -2)], 'D': [('B', 2)]}
        self.graph = graph.Graph(my_graph)
        self.bellmangraph = bellmanford.BellmanFord(self.graph)
        print(self.bellmangraph.bellman_ford('B'))

    def test_bellmanford_8(self):
        """9. Test bellmanford function."""
        my_graph = {'A': [('C', 3), ('D', 4)], 'B': [('C', -1)], 'C': [('D', -2)], 'D': []}
        self.graph = graph.Graph(my_graph)
        self.bellmangraph = bellmanford.BellmanFord(self.graph)
        print(self.bellmangraph.bellman_ford('B'))

    def test_bellmanford_9(self):
        """10. Test bellmanford function."""
        my_graph = {'A': [('C', -3), ('D', -2)], 'B': [('C', -1)], 'C': [('D', -2)], 'D': []}
        self.graph = graph.Graph(my_graph)
        self.bellmangraph = bellmanford.BellmanFord(self.graph)
        print(self.bellmangraph.bellman_ford('A'))

    def test_bellmanford_10(self):
        """11. Test bellmanford function."""
        my_graph = {'A': [('C', -3), ('D', -2)], 'B': [('C', -1)], 'C': [('D', -2)], 'D': []}
        self.graph = graph.Graph(my_graph)
        self.bellmangraph = bellmanford.BellmanFord(self.graph)
        print(self.bellmangraph.bellman_ford('B'))

    def test_bellmanford_11(self):
        """12. Test bellmanford function."""
        my_graph = {'A': [('C', -3), ('D', -2)], 'B': [('C', -1)], 'C': [('D', -2)], 'D': []}
        self.graph = graph.Graph(my_graph)
        self.bellmangraph = bellmanford.BellmanFord(self.graph)
        print(self.bellmangraph.bellman_ford('C'))

    def test_time_complexity(self):
        """13. Test get time complexity function."""
        self.assertEqual(self.bellmangraph.get_time_complexity(), 'O(|E|*|V|)')

    def test_space_complexity(self):
        """14. Test get space complexity function."""
        self.assertEqual(self.bellmangraph.get_space_complexity(), 'O(V)')
