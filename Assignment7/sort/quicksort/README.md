# Quick Sort

Quicksort is an algorithm based on divide and conquer approach in which the array is split into subarrays and these sub-arrays are recursively called to sort the elements. The quick sort is regarded as the best sorting algorithm. This is because of its significant advantage in terms of efficiency because it is able to deal well with a huge list of items. 

## Getting Started Steps

- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report

# Quick Sort 

## Requirements

- You must implement a class that handles the below interfaces for a quick sort.
- The class name must be called "QuickSort".
- You must implement at least 14 unit tests.
- Must get a 10/10 when running "make style"
- Your unit tests must reach 100% code coverage

## Interface

- The function sort(self, array) sorts the array passed in the argument and returns True if was able to sort and False otherwise. The array passed in should be updated to its sorted counterpart. You must use quick sort for this function.
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
