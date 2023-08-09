"""test dfs implementation."""


import unittest
import logging
import sys
from structures.graph import graph
from search.depthfirstsearch import dfs


class DFSearchTest(unittest.TestCase):
    """Class DFS."""

    def setUp(self):
        """Setup."""
        debug = True
        my_graph = {'A': [], 'B': [], 'C': [], 'X': [], 'Y': [], 'Z': []}
        self.graph = graph.Graph(my_graph)
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('B', 'C')
        self.graph.add_edge('C', 'X')
        self.graph.add_edge('X', 'Y')
        self.graph.add_edge('A', 'X')
        self.graph.add_edge('C', 'Y')

        self.dfssearch = dfs.DFSearch(self.graph.graph_dict)
        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("DFSTestLog")

    def test_constructor(self):
        """1.Test dFS Constructor."""
        self.assertEqual(self.dfssearch.dfs_visited, [])

    def test_addgraph(self):
        """2. Test add graph function."""
        my_graph = {'X': ['A'], 'A': []}
        grp = graph.Graph(my_graph)
        self.dfssearch.add_graph_dfs(grp.graph_dict)
        self.assertEqual(self.dfssearch.dfs('X'), ['X', 'A'])

    def test_emptygraph(self):
        """3. Test add graph function."""
        my_graph = {}
        grp = graph.Graph(my_graph)
        self.dfssearch.add_graph_dfs(grp.graph_dict)
        self.assertEqual(self.dfssearch.dfs('X'), [])

    def test_search_doesnt_exist(self):
        """4. Test search a node dne."""
        self.assertEqual(self.dfssearch.dfs('M'), [])

    def test_search_doesnt_connect(self):
        """5. Test search a node doesn't connect."""
        self.assertEqual(self.dfssearch.dfs('Z'), ['Z'])

    def test_get_time_complexity(self):
        """6.Test get_time_complexity()."""
        self.assertEqual(dfs.get_time_complexity(), 'O(b^m)')

    def test_get_space_complexity(self):
        """7.Test get_space_complexity()."""
        self.assertEqual(dfs.get_space_complexity(), 'O(bm)')

    def test_search_connect(self):
        """8. Test search a node connect."""
        self.assertEqual(self.dfssearch.dfs('A'), ['A', 'B', 'C', 'X', 'Y'])

    def test_search_connect_1(self):
        """9. Test search a node connect."""
        self.assertEqual(self.dfssearch.dfs('C'), ['C', 'X', 'Y'])

    def test_search_connect_2(self):
        """10. Test search a node connect."""
        self.assertEqual(self.dfssearch.dfs('B'), ['B', 'C', 'X', 'Y'])

    def test_search_connect_3(self):
        """11. Test search a node connect."""
        self.assertEqual(self.dfssearch.dfs('C'), ['C', 'X', 'Y'])

    def test_search_connect_4(self):
        """12. Test search a node connect."""
        self.assertEqual(self.dfssearch.dfs('X'), ['X', 'Y'])

    def test_search_connect_5(self):
        """13. Test search a node connect."""
        self.assertEqual(self.dfssearch.dfs('Y'), ['Y'])

    def test_search_connect_6(self):
        """14. Test search a node connect."""
        self.graph.add_edge('Y', 'A')
        self.dfssearch = dfs.DFSearch(self.graph.graph_dict)
        self.assertEqual(self.dfssearch.dfs('Y'), ['Y', 'A', 'B', 'C', 'X'])
