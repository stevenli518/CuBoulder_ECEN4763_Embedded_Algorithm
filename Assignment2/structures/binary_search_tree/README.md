# Data Structures Binary Tree

A binary tree is a non-linear data structure. The nodes are classified as Parent, Child and Leaf nodes. All nodes other than root and leaf nodes have two child nodes, left child and right child. Each node, except the root has one parent node. A complete binary tree is one in which each parent has zero or two child nodes. 

In a Binary Search Tree, the value of the left node should be lesser than that of the parent and the value of the right node should be greater.

## Getting Started Steps

- running "make setup" will install correct dependencies and check for correct python version (3.7+)
- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report

# Binary Tree

## Requirements

- You must implement a class that handles the below interfaces for a binary search tree.
- The class name must be called "Node".
- You must implement at least 14 unit tests.
- Must get a 10/10 when running "make style"
- Your unit tests must reach 100% code coverage

## Interface

- The function insert(self, value) inserts value into the the tree trying to maintain its balance as a binary tree
- The function findval(self, data) returns True if a value is present in the tree and False if the value is not present
- The function depth(self,node) returns the height of the binary tree from the root till the leaves
- The function printbtree(self) prints the values in the tree
- The function delete_Node(self, key) deletes a particular value (key) from the tree. It returns False if there is no value to be deleted
- The function get_space_complexity(), returns the space complexity of the data structure
- The function get_time_complexity(), returns the time complexity of findval based on the number of elements in the tree

## Tests

- Check insertion and deletion
- Check insertion of repeated values
- Check double deletion of values
- Check if a value is present in the tree or not
- Check the maximum height of the tree
- Space and time complexity of the data structure

## Corner Cases

- Repeated insertion and deletion of values 

## Library

You can only use basic python libraries (no special imports).
