"""test bfs implementation."""


import unittest
import logging
import sys
from structures.graph import graph
from search.breadthfirstsearch import bfs


class BFSearchTest(unittest.TestCase):
    """Class BFS."""

    def setUp(self):
        """Setup."""
        debug = True
        my_graph = {'X': [], 'Y': [], 'Z': [], 'A': [], 'B': [], 'C': [], }
        self.graph = graph.Graph(my_graph)
        self.graph.add_edge('X', 'Y')
        self.graph.add_edge('X', 'A')
        self.graph.add_edge('X', 'B')
        self.graph.add_edge('Y', 'Z')
        self.graph.add_edge('Y', 'B')
        self.graph.add_edge('Z', 'A')
        self.bfssearch = bfs.BFSearch(self.graph.graph_dict)
        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("BFSTestLog")

    def test_constructor(self):
        """1.Test BFS Constructor."""
        self.assertEqual(self.bfssearch.queue, [])
        self.assertEqual(self.bfssearch.visited, [])

    def test_addgraph(self):
        """2. Test add graph function."""
        my_graph = {'X': ['A'], 'A': []}
        grp = graph.Graph(my_graph)
        self.bfssearch.add_graph(grp.graph_dict)
        self.assertEqual(self.bfssearch.bfs('X'), ['X', 'A'])

    def test_emptygraph(self):
        """3. Test add graph function."""
        my_graph = {}
        grp = graph.Graph(my_graph)
        self.bfssearch.add_graph(grp.graph_dict)
        self.assertEqual(self.bfssearch.bfs('X'), [])

    def test_search_doesnt_exist(self):
        """4. Test search a node dne."""
        self.assertEqual(self.bfssearch.bfs('M'), [])

    def test_search_doesnt_connect(self):
        """5. Test search a node doesn't connect."""
        self.assertEqual(self.bfssearch.bfs('X'), ['X', 'Y', 'A', 'B', 'Z'])
        if 'C' not in self.bfssearch.bfs('X'):
            return True
        return False

    def test_get_time_complexity(self):
        """6.Test get_time_complexity()."""
        self.assertEqual(bfs.get_time_complexity(), 'O(bm)')
        bfs.get_time_complexity()

    def test_get_space_complexity(self):
        """7.Test get_space_complexity()."""
        self.assertEqual(bfs.get_space_complexity(), 'O(bm)')

    def test_search_1(self):
        """8. Test search at B."""
        self.assertEqual(self.bfssearch.bfs('B'), ['B'])

    def test_search_2(self):
        """9. Test search at Y."""
        self.assertEqual(self.bfssearch.bfs('Y'), ['Y', 'Z', 'B', 'A'])

    def test_search_3(self):
        """10. Test search at Z."""
        self.assertEqual(self.bfssearch.bfs('Z'), ['Z', 'A'])

    def test_search_4(self):
        """11. Test search at Z."""
        self.graph.add_edge('A', 'X')
        self.assertEqual(self.bfssearch.bfs('A'), ['A', 'X', 'Y', 'B', 'Z'])

    def test_search_5(self):
        """12. Test search at Z."""
        self.graph.add_edge('B', 'A')
        self.assertEqual(self.bfssearch.bfs('B'), ['B', 'A'])

    def test_search_6(self):
        """13. Test search at Z."""
        self.graph.add_edge('C', 'X')
        self.assertEqual(self.bfssearch.bfs('C'), ['C', 'X', 'Y', 'A', 'B', 'Z'])

    def test_search_7(self):
        """14. Test search at Z."""
        self.assertEqual(self.bfssearch.bfs('Y'), ['Y', 'Z', 'B', 'A'])
