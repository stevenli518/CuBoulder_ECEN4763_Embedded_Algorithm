# Breadth first search

Breadth-first search (BFS) is an algorithm used to traverse a tree on graphs or tree data structures. It is a queue based algorithm. BFS can be easily implemented using recursion and data structures like dictionaries and lists.

## Getting Started Steps

- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report

# Breadth first search

## Requirements

- You must implement a class that handles the below interfaces for a BFS search.
- The class name must be called "BFSearch".
- You must implement at least 5 unit tests.
- Must get a 10/10 when running "make style"
- Your unit tests must reach 100% code coverage

## Interface

- The constructor __init__(self, graph=None) should set the graph to the graph passed. A queue and list of visited nodes should also be initialized here, as these are used in bfs. The queue can just be a list, using operations append and pop to operate as a queue.
- The function bfs(self, node) performs the breadth first search algorithm starting from node, appending the nodes visited to the visited array. It should return the 'visited' array based on the node that was passed in. If the graph is empty or the node does not exist in the graph an empty array should be returned.
- The function add_graph(self, graph) should replace the current graph to search on. The visited and queue lists should also be set back to the empty list.
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
