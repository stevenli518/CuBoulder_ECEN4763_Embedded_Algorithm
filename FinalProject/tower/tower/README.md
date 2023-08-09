# Tower Problem

Using your previous graph structure, you will implement an algorithm that determines radio signals for each Tower in a given set, such that adjacent towers do not interfere with eachother. In other words, map the N vertices in the graph (towers) to M numbers (signals), such that adjacent vertices do not share the same signal.

## Getting Started Steps

- running "make setup" will install correct dependencies and check for correct python version (3.7+)
- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report

# Tower

## Requirements

- You must implement a class that handles the below interfaces for selecting which radio signal goes to which tower.
- The class name must be called "Tower".
- You must implement at least 14 unit tests.
- Must get a 10/10 when running "make style"
- Your unit tests must reach 100% code coverage

## Interface

- The initialization of the class must be Tower(self, graph=None, max_allowed_radio_signals=None)
    - Graph must use the implementation from Assignment 3, if graph is None, then an empty graph must be created
    - If max_allowed_radio_signals is None, then the max number of radio signals is N, where N is the number of vertices in graph
- The function get_time_complexity(), returns the time complexity of the tower algorithm
- The function get_space_complexity(), returns the space complexity of the tower algorithm
- The function create_mapping(), maps each tower to a signal
- The function get_all_tower_to_radio_signal_mapping(), returns a dictionary of all the towers and the signal they are mapped to
- The function get_max_radio_signals(), returns the max number of radio signals used for the mapping
- The function get_max_allowed_radio_signals(), returns the max allowed radio signals for the mapping
- The function get_radio_signal_for_tower(tower), returns the radio signal for the specific tower passed in
- The function is_valid(), return true if create mapping was able to be solved, without running out of radio signals

## Tests

- Check on a variety of graphs, including large graphs, complete graphs, etc.
- Check in cases where there are sections of the graph, or vertices, that are not connected to the rest.
- Make sure your algorithm is fast enough that it can be tested on graphs with many vertices
- There are multiple ways to do this with differing complexities. Make sure your time complexity is consistent with your code, not the optimal time complexity for this probleem.

## Corner Cases

- Check on the empty graph

## Library

You can only use basic python libraries (no special imports)
