# Hybrid Sort

A hybrid sort is the algorithm that combines two or more sorting algorithms to eventually sort a single array in the increasing or decreasing order. In this case, you will be implementing TimSort which combines together Merge Sort and Insertion Sort. TimSort is used as the default sorting algorithm in many programming languages, including python.

TimSort performs insertion sort on runs of a given size, in our case 32. 

The first 32 entries in the list will be sorted with insertion sort, then the next 32, and so on until the end of the list is reached. For lists of size smaller than 32, the full sorting process will be equivalent to insertion sort. For longer lists, merge sort is then used to complete the process. 

The merge operation from merge sort is used to combine together neighboring runs of length 32, so that all runs are of length 64. Then, neighboring runs of length 64 can be combined into runs of length 128. This process is repeated until the run length is greater than the length of the list.

In testing, it is very important to tests large lists for this class. This is because shorter lists may have a smaller size than the run length, and so the merge operation will never be run. A size of greater than 1024 will allow for good testing. An example test array is given below:

test_arr = [random.uniform(-10000, 10000) for _ in range(0, 1000)]

You can then check that your sorted array is equal to sorted(test_arr)

## Getting Started Steps

- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report

# Hybrid Sort

## Requirements

- You must implement a class that handles the below interfaces for a Hybrid Sort.
- The class name must be called "HybridSort".
- You must implement at least 14 unit tests.
- Must get a 10/10 when running "make style"
- Your unit tests must reach 100% code coverage

## Interface

- The constructor __init__(self) initializes the variable self.array to an empty array to use when sorting and any other variables you find necessary.
- The function sort(self, array) sorts the array using TimSort passed in the argument and returns True if was able to sort and False otherwise. The sorted array should be stored in the class variable self.array.
- The function get_sorted_list(self) returns the sorted array
- The function get_space_complexity(), returns the space complexity of the sorting algorithm.
- The function get_time_complexity(), returns the time complexity of the sorting algorithm.
- You should probably include helper functions to implement TimSort, but these will not be tested.

## Tests

- Space and time complexity of the sorting algorithm.
- Sort a given array
- Sort small and very large arrays. Use random in your testing to generate sufficiently large arrays.
- Sort characters, strings, numbers, floats, etc.

## Corner Cases

- Sorting an array consisting of same values in different indices.
- Sorting an array that includes values of different types (return false)

## Library

You can only use basic python libraries (no special imports).
