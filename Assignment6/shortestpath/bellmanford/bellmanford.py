"""This module is for the bellmanford implementation."""
# Citation: Adapted from GeeksforGeeks


class BellmanFord:
    """Class implementation for BellmanFord."""

    def __init__(self, graph):
        """Construct the data structure."""
        self.add_graph(graph)

    def add_graph(self, graph):
        """Add a graph to the BellmanFord class."""
        self.bellgraph = graph

    def bellman_ford(self, src):
        """Implement the Bellman Ford algorithm."""
        dist = {}
        for node in self.bellgraph.graph_dict:
            dist[node] = float("Inf")
        dist[src] = 0
        for _ in range(len(dist)-1):  # Iterate V-1 times
            for node in self.bellgraph.graph_dict:
                my_tup = self.bellgraph.graph_dict[node]
                for tup in my_tup:
                    if dist[node] != float("Inf") and dist[node] + tup[1] < dist[tup[0]]:
                        dist[tup[0]] = dist[node] + tup[1]

        for node in self.bellgraph.graph_dict:
            my_tup = self.bellgraph.graph_dict[node]
            for tup in my_tup:
                if dist[node] != float("Inf") and dist[node] + tup[1] < dist[tup[0]]:
                    return [[-1, -1]]
        dist = sorted(dist.items())
        new_list = []
        for node in dist:
            temp = []
            temp.append(node[0])
            temp.append(node[1])
            new_list.append(temp)
        return new_list

        # return dist

    def get_time_complexity(self):
        """Get the time complexity of the data structure."""
        return 'O(|E|*|V|)'

    def get_space_complexity(self):
        """Get the space complexity of the data structure."""
        return 'O(V)'
