# Data Structures Graph

Graph is a non-linear data structure. It consists of a finite number of vertices and edges. Vertices are also known as nodes. The nodes are linked to one another with the help of the edges. A pair of (x,y) edge connects the node x with node y.

## Getting Started Steps

- running "make setup" will install correct dependencies and check for correct python version (3.7+)
- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report

# Graph

## Requirements

- You must implement a class that handles the below interfaces for a graph data structure.
- The class name must be called "Graph".
- You must implement at least 14 unit tests.
- Must get a 10/10 when running "make style"
- Your unit tests must reach 100% code coverage

## Interface

- The constructor __init__(self, graph=None) should initialize the graph if given, or initialize it to be empty if not.
    - Note: the graph must be a dictionary containing arrays, with vertices as the keys, and items in the array are other vertices connected to their respective key. 
    Example:         graph = {
            'A': ['B'],
            'B': ['A'],
            'C': ['A'],
            'D': []
        }
- The function is_empty(self) returns True if the graph is empty, False if populated.
- The function empty(self) empties the graph.
- The function remove_vertex(self, vertex) removes the passed vertex and returns the same, else return None.
- The function remove_edge(self, vertex1, vertex2) removes the edges and returns {'vertex1': 'vertex2'} if successful, else return None.
- The function get_vertices(self) returns the list of all vertices in the graph.
- The function contains(self, vertex) returns True if the value is present in the graph, else returns False.
- The function get_edges(self) returns a list of all the edge pairs.
- The function add_vertex(self, vertex) adds a vertex to the graph and returns the number of edges associated with the vertex.
- The function add_edge(self, vertex1, vertex2) adds an edge between vertex 1 and vertex 2.
- The function get_number_of_edges(self, vertex) returns the number of edges associated with the passed vertex.
- The function get_neighbors(self, node) returns all of the vertixes connected to the node passed in (return empty list if the graph is empty or if the node does not exist)
- The function get_time_complexity(self), returns the time complexity of adding an edge to the data structure, return a string, example: return 'O(|V|^15)'.

## Tests

- test for empty graph
- test for removal of existing and nonexistent edges and vertices
- test to get the number of edges and vertices in a graph
- test for addition and deletion of edges and vertices
- time complexity of the data structure

## Corner Cases

- Removal of nonexistent vertices and edges

## Library

You can only use basic python libraries (no special imports).
