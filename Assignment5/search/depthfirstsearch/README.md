# Depth first search

Depth-first search (DFS) is an algorithm used to determine whether there is a path between two nodes. It traverse down one single path in a graph, until it can’t traverse any further, checking one child node at a time.

## Getting Started Steps

- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report

# Depth first search

## Requirements

- You must implement a class that handles the below interfaces for a DFS search.
- The class name must be called "DFSearch".
- You must implement at least 5 unit tests.
- Must get a 10/10 when running "make style"
- Your unit tests must reach 100% code coverage

## Interface

- The constructor __init__(self, graph=None) should initialize the graph and initialize a list named 'visited' to the empty list, used in dfs.
- The function dfs(self, node) appends the visited array with the nodes visited while traversing the graph to obtain the value using depth first search. It returns the 'visited' array.
- The function add_graph_dfs(self, graph) should replace the current graph to search on. This function should also set the 'visited' array back to the empty list.
- The function get_space_complexity(), returns the space complexity of the search.
- The function get_time_complexity(), returns the time complexity of the search.

## Tests

- Space and time complexity of the sorting algorithm.
- Search for the given value

## Corner Cases

- empty graph
- searching for a node that does not exist
- searching for a node that is not connected to any others

## Library

You can only use basic python libraries (no special imports).
