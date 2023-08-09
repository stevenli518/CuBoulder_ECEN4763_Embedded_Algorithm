# Data Structures Stack

Stack is a linear data structure that collects and stores data in a linear manner. The operations used to store and retrieve data are push and pop respectively. The order in which data is accessed is usually LIFO (Last In First Out).

## Getting Started Steps

- running "make setup" will install correct dependencies and check for correct python version (3.7+)
- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report

# Stack

## Requirements

- You must implement a class that handles the below interfaces for a stack.
- The class name must be called "Stack".
- You must implement at least 14 unit tests.
- Must get a 10/10 when running "make style"
- Your unit tests must reach 100% code coverage

## Interface

- The constructor for the class accepts an integer maxsize and nothing else
- The function isEmpty(self) returns TRUE if the stack is empty and FALSE if it is not
- The function push(self,my_stack) adds an element to the stack
- The function pop(self) removes the last element added to the stack
- The function stack_size(self) returns the size of the stack
- The function top_peek(self) returns the value of the topmost element of the stack (last pushed)
- The function empty(self) empties the entire stack
- The function get_space_complexity(), return the space complexity of the data structure

## Tests

- Check if the stack is empty or not
- Push and pop elements from the stack
- Check the order in which the elements are being pushed to the stack is reverse compared to the order in which elements are popped
- Check the maximum size of the stack
- Check for the value of the topmost element in the stack
- Push an element to a full stack and pop an element from an empty stack
- space complexity of the data structure

## Corner Cases

- How to handle a pop when the stack is empty or a push when the stack is full

## Library

You can only use basic python libraries (no special imports).
