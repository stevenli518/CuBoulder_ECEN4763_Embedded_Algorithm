# Bellman Ford

The Bellman Ford algorithm calculates the shortest path between one vertex and all other vertices in a weighted graph. It is capable of handling graphs in which edge weights are provided with negative numbers.

## Getting Started Steps

- running "make setup" will install correct dependencies and check for correct python version (3.7+)
- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report

# Bellman Ford

## Requirements

- You must implement a class that handles the below interfaces for a graph data structure.
- The class name must be called "BellmanFord".
- You must implement at least 4 unit tests.
- Must get a 10/10 when running "make style"
- Your unit tests must reach 100% code coverage

## Interface

- The constructor __init__(self, graph) should just call self.add_graph(graph)
- The function add_graph(self, graph) adds a graph to the BellmanFord class
    - Note this graph should be an instance of your graph class from assignment 3
- The function bellman_ford(self, src) implements the Bellman Ford algorithm, returning a list of the vertices in the graph along with their associated distances from the vertex src, where src is a string.
    - ex. [['A', 18], ['B', 6], ['C', 0], ['D', 9], ['E', float("Inf")]]
    - This list should be sorted by the vertex strings.
    - If negative cycles are found, then return a list containing [[-1, -1]].

## Tests

- Test to calculate the shortest paths from a given vertex on a variety of graphs.
- Test to see if there are any negative cycles.
- Time and space complexity of the data structure.

## Corner Cases

- Disconnected graphs

## Library

You can only use basic python libraries (no special imports).
