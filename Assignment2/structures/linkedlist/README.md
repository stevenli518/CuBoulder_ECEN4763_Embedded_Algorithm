# Data Structures XOR Linked List

An XOR linked list is a memory efficient doubly linked list. It actually is a singly linked list behaving like a doubly linked list. It has addresses to the previous and the next node in the list. Instead of storing the address of the next node, it stores the XOR of the previous and the next addresses. However, it is more complex and hard to debug.

## Getting Started Steps

- running "make setup" will install correct dependencies and check for correct python version (3.7+)
- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format" will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report

# XOR Linked List

## Requirements

- You must implement a class that handles the below interfaces for an xor list.
- The class name must be called "XORList".
- Will have another class called "Node"
- You must implement at least 14 unit tests.
- Must get a 10/10 when running "make style".
- Your unit tests must reach 100% code coverage

## Interface

- The function get_address(self) gets the address of a Node will be in the Node class.
- The function get_value(self) gets the value of a Node will be in the Node class.
- The function get_head(self) gets the head pointer of the linked list.
- The function get_tail(self) gets the tail pointer of the linked list.
- The function insert_begin(self, value) inserts a node storing value at the beginning of the linked list.
- The function insert_end(self, value) inserts a node stroing value at the end of the linked list.
- The function insert_before(self, next_node, value) inserts a node storing value before the specified value of next_node already in the list.
- The function insert_after(self, prev_node, value) inserts a node storing value after the specified value of prev_node already in the list.
- The function find(self, value) returns true if value is in list and false if value is not in list.
- The function length(self) returns the lenght of the linked list, returns 0 if the list is empty.
- The function printxorlist(self) prints the values in the linked list.
- The function isempty(self) returns true if the linked list is empty and false if the list is not empty.
- The function delete_head(self) deletes the head of the linked list.
- The function delete_tail(self) deletes the tail of the linked list.
- The function delete_node(self, value) deletes the node containing value.
- The function empty_list(self) deletes the entire linked list.
- The function type_cast(i_d) casts the address of i_d so that we can use pointers in python,
- The function xor(xor_a, xor_b) returns the xor of the inputs xor_a and xor_b
- The function get_space_complexity(), returns the space complexity of the data structure
- The function get_time_complexity(), returns the time complexity of find based on the number of elements in the list
## Tests

- Check insertion and deletion this includes all the different ways to insert and delete (i.e. beginning, end, before, after)
- Check insertion of repeated values
- Check double deletion of values
- Check if value is present in list or not
- Check length of list
- Check the time complexity of the data structure
- Check that as you insert nodes they insert into the correct places in the list 

## Corner Cases

- Delete when list is empty
- Insert before or after a value that is not in the list 
- Insert before the head or after the tail

## Library

You can only use basic python libraries (no special imports).
