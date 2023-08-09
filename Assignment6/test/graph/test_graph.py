"""Test Graph implementation."""

# pylint: disable = R0904
import unittest
import logging
import sys
from structures.graph import graph


class GraphTest(unittest.TestCase):
    """Class Graph."""

    def setUp(self):
        """Setup."""
        debug = True
        my_graph = {'A': [], 'B': [], 'C': []}
        self.graph = graph.Graph(my_graph)
        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("GraphTestLog")

    def test_init(self):
        """1. Test graph constructor."""
        print("\n")
        print(self.graph.graph_dict)

    def test_add_vertex(self):
        """2. Test add_vertex function."""
        self.graph.add_vertex("D")
        self.graph.add_vertex("E")
        self.graph.add_vertex("F")
        print("\n")
        print(self.graph.graph_dict)

    def test_add_edge(self):
        """3. Test add_edge function."""
        self.graph.add_edge("A", "C", 3)
        self.graph.add_edge("A", "B", -5)
        print("\n")
        print(self.graph.graph_dict)

    def test_add_vertex_return_edges(self):
        """4. Test add_vertex return the number of edge associated with it."""
        self.graph.add_edge("A", "C", 3)
        self.graph.add_edge("A", "B", -5)
        self.assertEqual(self.graph.add_vertex("A"), 2)

    def test_get_number_of_edges(self):
        """5. Test get_number_of_edges."""
        self.graph.add_edge("A", "C", 3)
        self.graph.add_edge("A", "B", -5)
        self.assertEqual(self.graph.get_number_of_edges("A"), 2)

    def test_get_vertices(self):
        """6. Test get_vertices."""
        self.graph.add_edge("A", "C", 3)
        self.graph.add_edge("A", "B", -5)
        mylist = self.graph.get_vertices()
        print(mylist)

    def test_contains(self):
        """7. Test contains."""
        self.assertEqual(self.graph.contains("A"), True)
        self.assertEqual(self.graph.contains("B"), True)
        self.assertEqual(self.graph.contains("C"), True)

    def test_is_empty(self):
        """8. Test is_empty."""
        self.assertEqual(self.graph.is_empty(), False)

    def test_is_empty_2(self):
        """9. Test is_empty_2."""
        self.graph.empty()
        self.assertEqual(self.graph.is_empty(), True)

    def test_get_neighbors(self):
        """10. Test get_neighbors."""
        self.graph.add_edge("A", "C", 3)
        self.graph.add_edge("A", "B", -5)
        self.assertEqual(self.graph.get_neighbors("A"), [('C', 3), ('B', -5)])

    def test_get_neighbors_2(self):
        """11. Test get_neighbors."""
        self.graph.add_edge("A", "C", 3)
        self.graph.add_edge("A", "B", -5)
        self.assertEqual(self.graph.get_neighbors("D"), None)

    def test_remove_vertex(self):
        """12. Test remove vertex."""
        self.graph.add_edge("A", "C", 3)
        self.graph.add_edge("A", "B", -5)
        self.graph.add_edge("B", "C", -5)
        self.graph.add_edge("C", "B", -5)
        self.assertEqual(self.graph.remove_vertex("A"), 'A')
        print("\n")
        print(self.graph.graph_dict)

    def test_remove_vertex_2(self):
        """13. Test remove vertex."""
        self.graph.add_edge("A", "C", 3)
        self.graph.add_edge("A", "B", 2)
        self.graph.add_edge("C", "A", 3)
        self.graph.add_edge("C", "B", 1)
        self.graph.add_edge("B", "A", 1)
        self.graph.add_edge("B", "C", 1)
        self.assertEqual(self.graph.remove_vertex("B"), 'B')
        print("\n")
        print(self.graph.graph_dict)

    def test_remove_vertex_3(self):
        """14. Test remove nonexistent vertex from an empty graph."""
        self.graph.empty()
        self.assertEqual(self.graph.remove_vertex("B"), None)

    def test_remove_vertex_4(self):
        """15. Test remove nonexistent vertex."""
        self.assertEqual(self.graph.remove_vertex("D"), None)

    def test_remove_edge(self):
        """16. Test remove edge."""
        self.graph.add_edge("A", "C", 3)
        self.graph.add_edge("A", "B", -5)
        self.assertEqual(self.graph.remove_edge("A", "C"), {'A': ('C', 3)})
        print("\n")
        print(self.graph.graph_dict)

    def test_remove_edge_2(self):
        """17. Test remove nonexistent edge."""
        self.assertEqual(self.graph.remove_edge("A", "D"), None)

    def test_remove_edge_3(self):
        """18. Test remove nonexistent edge in an empty graph."""
        self.graph.empty()
        self.assertEqual(self.graph.remove_edge("A", "D"), None)

    def test_get_edges(self):
        """19. Test get_edges."""
        self.graph.add_edge("A", "C", 3)
        self.graph.add_edge("A", "B", 1)
        self.graph.add_edge("C", "A", 2)
        self.graph.add_edge("C", "B", 1)
        self.graph.add_edge("B", "A", 1)
        self.graph.add_edge("B", "C", 1)
        lst = self.graph.get_edges()
        print("\n")
        print(lst)

    def test_get_edges_2(self):
        """20. Test get_edges_empty."""
        self.graph.empty()
        self.assertEqual(self.graph.get_edges(), None)

    def test_time_complexity(self):
        """21. Test get_time_complexity."""
        self.assertEqual(self.graph.get_time_complexity(), 'O(V)')

    def test_constructor_2(self):
        """22. Test constructor without input."""
        my_graph = graph.Graph()
        print(my_graph.graph_dict)

    def test_remove_edge_4(self):
        """23. Test remove edge when vertex2 is not associated with vertex1."""
        self.graph.add_vertex("D")
        print(self.graph.graph_dict)
        self.assertEqual(self.graph.remove_edge("A", "D"), None)

    def test_contain_2(self):
        """23. Test contain function, where value not in graph."""
        self.assertEqual(self.graph.contains("D"), False)

    def test_add_edges_2(self):
        """24. Test add_edges: v1 not in graph v2 in graph."""
        self.graph.add_edge("E", "A", 5)
        print("\n", self.graph.graph_dict)

    def test_add_edges_3(self):
        """25. Test add_edges: v2 not in graph v1 in graph."""
        self.graph.add_edge("A", "E", 5)
        print("\n", self.graph.graph_dict)

    def test_add_edges_4(self):
        """26. Test add_edges: v1 not in graph v2 not in graph."""
        self.graph.add_edge("E", "G", 2)
        print("\n", self.graph.graph_dict)

    def test_get_number_of_edges_2(self):
        """27. Test get_number_of_edges of nonexistent vertex."""
        self.graph.add_edge("A", "C", 3)
        self.graph.add_edge("A", "B", 2)
        self.assertEqual(self.graph.get_number_of_edges("D"), 0)

    def test_get_vertices_empty_graph(self):
        """28. Test get_vertices_empty."""
        self.graph.empty()
        self.assertEqual(self.graph.get_vertices(), [])
