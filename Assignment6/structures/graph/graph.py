"""This module is for the graph implementation."""


class Graph:
    """Class implementation for Graph."""

    def __init__(self, graph=None):
        """Graph constructor."""
        if graph is None:
            self.graph_dict = {}
            return
        self.graph_dict = graph

    def is_empty(self):
        """Return True if the graph is empty, False if populated."""
        if self.graph_dict == {}:
            return True
        return False

    def empty(self):
        """Empty the graph."""
        self.graph_dict = {}

    def remove_vertex(self, vertex):
        """Remove the passed vertex and returns the same, else return None."""
        if self.is_empty() is True:
            return None
        if vertex not in self.graph_dict:
            return None
        for node in self.graph_dict.copy():
            my_lst = self.get_neighbors(node)
            for tup in my_lst:
                if tup[0] == vertex:
                    my_lst.remove(tup)
            if node == vertex:
                self.graph_dict.pop(node)
        return vertex

    def remove_edge(self, vertex1, vertex2):
        """Remove the edges and returns {'vertex1': 'vertex2'} if successful, else return None."""
        if self.is_empty() is True:
            return None
        if vertex1 not in self.graph_dict or vertex2 not in self.graph_dict:
            return None
        my_lst = self.get_neighbors(vertex1)
        flag = False
        my_set = {}
        for tup in my_lst:
            if tup[0] == vertex2:
                my_set[vertex1] = tup
                my_lst.remove(tup)
                flag = True
        if flag is False:
            return None
        return my_set

    def get_vertices(self):
        """Return the list of all vertices in the graph."""
        my_list = []
        if self.is_empty() is True:
            return my_list
        for i in self.graph_dict:
            my_list.append(i)
        return my_list

    def contains(self, vertex):
        """Return True if the value is present in the graph, else returns False."""
        if vertex in self.graph_dict:
            return True
        return False

    def get_edges(self):
        """Return a list of all the edge pairs."""
        if self.is_empty() is True:
            return None
        my_edges = []
        for node in self.graph_dict:
            my_lst = self.get_neighbors(node)
            for val in my_lst:
                my_tuple = {}
                my_tuple[node] = val
                my_edges.append(my_tuple)
        return my_edges

    def add_vertex(self, vertex):
        """Add a vertex to the graph and returns the number of edges associated with the vertex."""
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
            return len(self.graph_dict[vertex])
        return len(self.graph_dict[vertex])

    def add_edge(self, vertex1, vertex2, weight):
        """Add an edge between vertex 1 and vertex 2."""
        temp = (vertex2, weight)
        if vertex1 in self.graph_dict and vertex2 in self.graph_dict:  # v1 and v2 in the graph
            self.graph_dict[vertex1].append(temp)
        if vertex1 not in self.graph_dict and vertex2 in self.graph_dict:  # v1 not in; v2 in
            self.add_vertex(vertex1)
            self.graph_dict[vertex1].append(temp)
        if vertex2 not in self.graph_dict and vertex1 in self.graph_dict:  # v2 not in; v1 in
            self.add_vertex(vertex2)
            self.graph_dict[vertex1].append(temp)
        if vertex1 not in self.graph_dict and vertex2 not in self.graph_dict:  # v1 not in v2 not in
            self.add_vertex(vertex1)
            self.add_vertex(vertex2)
            self.graph_dict[vertex1].append(temp)

    def get_number_of_edges(self, vertex):
        """Return the number of edges associated with the passed vertex."""
        if vertex in self.graph_dict:
            return len(self.graph_dict[vertex])
        self.add_vertex(vertex)
        return len(self.graph_dict[vertex])

    def get_neighbors(self, node):
        """Return all of the vertixes connected to the node."""
        if node not in self.graph_dict or self.graph_dict is None:
            return None
        return self.graph_dict[node]

    def get_time_complexity(self):
        """Return the time complexity of adding an edge."""
        return 'O(V)'
