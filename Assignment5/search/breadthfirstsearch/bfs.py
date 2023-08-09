"""This BFS Module can be used to solve the breadth first search algorithm."""


class BFSearch:
    """Class implementation for BFSearch."""

    def __init__(self, graph=None):
        """Set the graph to the graph passed."""
        self.my_graph = graph
        self.queue = []
        self.visited = []

    def bfs(self, node):
        """Perform the breadth first search algorithm starting from node."""
        # Empty Graph
        if self.my_graph == {}:
            return self.visited
        # Search a node doesn't exist
        if node not in self.my_graph:
            return self.visited
        # Start Searching
        self.queue.append(node)
        self.visited.append(node)

        while self.queue:
            temp = self.queue.pop()
            for edges in self.my_graph[temp]:
                if edges not in self.visited:
                    self.queue.append(edges)
                    self.visited.append(edges)
        print(self.visited)
        return self.visited

    def add_graph(self, graph):
        """Replace the current graph to search on."""
        self.my_graph = graph
        self.queue = []
        self.visited = []


def get_space_complexity():
    """Return the space complexity of the search."""
    return 'O(bm)'


def get_time_complexity():
    """Return the time complexity of the search."""
    return 'O(bm)'
