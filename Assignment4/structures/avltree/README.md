# Data Structures AVL Tree

AVL tree is a self balancing binary tree. The difference of heights of the left and the right branches is maintained to be 1 at its maximum. It was developed by Adelson, Velskii, and Landi. Hence, the name.

## Getting Started Steps

- running "make setup" will install correct dependencies and check for correct python version (3.7+)
- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report

# AVL Tree

## Requirements

- You must implement a class that handles the below interfaces for an AVL tree.
- The class name must be called "AVLTree".
- You must have a Node class called "Node".
- You must implement at least 14 unit tests.
- Must get a 10/10 when running "make style"
- Your unit tests must reach 100% code coverage

## Node Interface

- The constructor __init__(self, value, right=None, left=None, height=None) should set all class variables to those passed.
- The function get_height(self) returns the height variable of the node.
- The function set_height(self, height) sets the height variable of the node to height.

## AVLTree Interface

- The constructor __init__(self) sets the root of the tree to None.
- The function get_root(self) returns the root of the tree.
- The function remove(self, val) removes a value from the tree and returns the value removed or None if not in the tree. The balance of the tree should be maintained.
- The function insert(self, val) inserts a value into the tree and returns True if successful, False otherwise. The balance of the tree should be maintained.
- The function height(self) returns the height of the tree
- The function min(self) returns the minimum value present in the tree
- The function max(self) returns the maximum value present in the tree
- The function is_empty(self) returns True if no root is present, False otherwise
- The function get_space_complexity() returns the space complexity of the data structure
- The function get_time_complexity() returns the time complexity of insertion into the data structure

## Tests

- Insertion and deletion of values from the node
- Tests to check that the tree is balanced after various operations
- Test to check the tree height
- Checks to see if the tree is empty
- Tests to obtain minimum and maximum values of a tree
- Obtain space and time complexity

## Corner Cases

- Remove a non-existent value from the tree

## Library

You can only use basic python libraries (no special imports).
