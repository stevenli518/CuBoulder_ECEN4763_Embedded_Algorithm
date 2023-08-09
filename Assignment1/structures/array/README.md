# Data Structures Array

Array is a data structure that stores data in continuous memory locations where each element is accessed using an array index. The location of each element can be determined by adding an offset to the first element in the array. Your implementation can be built onto the existing python array data structure.

## Getting Started Steps

- running "make setup" will install correct dependencies and check for correct python version (3.7+)
- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report
- running "make runner" will run a script to calculate time and memory for the Array class

# Array

## Requirements

- You must implement a class that handles the below interfaces for an array.
- The class name must be called "Array".
- You must implement at least 14 unit tests.
- Must get a 10/10 when running "make style"
- Your unit tests must reach 100% code coverage

## Interface

- insert(self, value, index=-1), when index >= 0 insert into that specific index otherwise append to the end.
- get_value(index), return the value at the specific index, return None if index does not exist
- get_index(value), return the index for the specific value, return None if value does not exist
- remove(value), remove value and return the value, return None if value does not exist
- empty(), remove all values from array
- is_empty(), return true if the array is empty
- exists(value), return true if the array contains value
- get_size(), return the number of elements in the array
- get_space_complexity(), return the space complexity of the data structure as a string, ex. return 'O(2^n)'

## Tests

- insert in the beginning, middle and end
- insert and verify the size changes
- verify empty removes all elements
- insert an element and verify it exists
- space complexity of the data structure

## Corner Cases

- How to handle a remove when the array is empty or value doesn't exist

## Library

You can only use basic python libraries (no special imports).
