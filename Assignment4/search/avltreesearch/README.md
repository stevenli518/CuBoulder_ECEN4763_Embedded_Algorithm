# Data Structures AVL Search

AVL tree is a self balancing binary tree. The difference of heights of the left and the right branches is maintained to be 1 at maximum. It was developed by Adelson, Velskii, and Landi. Hence, the name. Implementing a methid to search in AVL tree can help in reducing the search time to a great extent.

## Getting Started Steps

- running "make setup" will install correct dependencies and check for correct python version (3.7+)
- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report

# AvlTreeSearch

## Requirements

- You must implement a class that handles the below interfaces for an avltree search.
- The class name must be called "AVLTreeSearch".
- You must implement at least 14 unit tests.
- Must get a 10/10 when running "make style"
- Your unit tests must reach 100% code coverage

## Interface

- The constructor __init__(self, bstree) initializes the class variable storing the tree to bstree. This is the tree that will be search through and can be changed.
- The function add_tree(self, bstree) sets the class variable for the tree to bstree. This changes the tree variable to the new tree passed to the function.
- The function search(self, value_to_find, steps=0) returns the value if it is found or None if it is not, and the number of steps it took to find that value. These values should be returned in a list with only two entries, whether it is found in the first index and the number of steps in the second.


## Tests

- Search of values from the Tree in numerous situations

## Corner Cases

- Search when tree is empty.

## Library

You can only use basic python libraries (no special imports).
