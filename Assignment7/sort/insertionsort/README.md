# Insertion Sort

In insertion sort, the array is processed as a sorted part and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part. It is efficient for smaller data sets, but very inefficient for larger lists. Insertion sort is adaptive, that means it reduces its total number of steps if a partially sorted array is provided as input, making it efficient in these cases.

## Getting Started Steps

- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report

# Insertion Sort 

## Requirements

- You must implement a class that handles the below interfaces for an insertion sort.
- The class name must be called "InsertionSort".
- You must implement at least 14 unit tests.
- Must get a 10/10 when running "make style"
- Your unit tests must reach 100% code coverage

## Interface

- The function sort(self, array) sorts the array passed in the argument and returns True if was able to sort and False otherwise. The array passed in should be updated to its sorted counterpart. You must use insertion sort for this function.
- The function get_space_complexity(), returns the space complexity of the sorting algorithm.
- The function get_time_complexity(), returns the time complexity of the sorting algorithm.

## Tests

- Space and time complexity of the sorting algorithm.
- Sort a given array

## Corner Cases

- Sorting an array consisting of same values in different indices. 
- If different types are in an array (i.e. 1 and 'A') then you must return False

## Library

You can only use basic python libraries (no special imports).
