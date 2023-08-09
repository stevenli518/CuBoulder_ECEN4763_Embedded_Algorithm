# Data Structures Queues

Queue is similar to stacks, in that it is a linear data structure. The order in which data is accessed is FIFO (First In First Out). Addition of data is done at one end of the queue and the removal is done on the other.

## Getting Started Steps

- running "make setup" will install correct dependencies and check for correct python version (3.7+)
- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report

# Queue

## Requirements

- You must implement a class that handles the below interfaces for a queue.
- The class name must be called "Queue".
- You must implement at least 14 unit tests.
- Must get a 10/10 when running "make style"
- Your unit tests must reach 100% code coverage

## Interface

- The constructor for the class accepts an integer maxsize and nothing else
- The function isEmpty(self) returns TRUE if the queue is empty and FALSE if it is not
- The function enqueue(self,my_queue) adds an element to the queue
- The function dequeue(self) removes the first element added to the queue
- The function queue_size(self) returns the size of the queue
- The function empty(self) empties the entire queue
- The function get_space_complexity(), returns the space complexity of the data structure

## Tests

- Check if the queue is empty or not
- Enqueue and dequeue and check the size of the queue
- Check the order in which the elements are being added and removed from the queue
- Check the maximum size of the queue
- Enqueue a full queue and dequeue an empty queue
- space complexity of the data structure

## Corner Cases

- How to handle a dequeue when the queue is empty or an enqueue when the queue is full

## Library

You can only use basic python libraries (no special imports).
