"""Depth first search."""


class DFSearch:
    """Class implementation for DFSearch."""

    def __init__(self, graph=None):
        """Set the graph to the graph passed."""
        self.my_graph = graph
        self.dfs_visited = []

    def dfs(self, node):
        """Perform the breadth first search algorithm starting from node."""
        # Empty DFS Graph
        if self.my_graph == {}:
            return self.dfs_visited
        # DFS: Search a node doesn't exist
        if node not in self.my_graph:
            return self.dfs_visited
        # DFS: Start Searching
        if node not in self.dfs_visited:
            self.dfs_visited.append(node)
            for edge in self.my_graph[node]:
                self.dfs(edge)
        return self.dfs_visited

    def add_graph_dfs(self, graph):
        """Replace the current graph to search on."""
        self.my_graph = graph
        self.dfs_visited = []


def get_space_complexity():
    """Return the space complexity of the search."""
    return 'O(bm)'


def get_time_complexity():
    """Return the time complexity of the search."""
    return 'O(b^m)'
