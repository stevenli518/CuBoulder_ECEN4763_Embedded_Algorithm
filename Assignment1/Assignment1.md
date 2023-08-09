# Assignment 1

## Assignment Description

In this assignment you will create 3 classes. A class for array, stack and queue. Please follow the guidelines located in each README.md in the array, stack and queue folders.

## Goal

The main goal for this assignment is to learn how to create classes, generate UTs, understand how each assignment will be graded, and ensure you understand basic data structures.

## Grading

- The grading is broken down into 4 sections. There is code format, your UTs, code coverage and Solution UTs.
- This assignment is worth 50pts.
- Code format is worth 5 points, your UTs are worth 10 points, coverage is 10 points, and passing our UTs accounts for the remaining 25 points.

### Lint

- You will receive an all or nothing for lint for 10% of the overall grade.
- If you run `make style` and fix all errors you will get the 10%.
- If there are any style issues you automatically receive a 0 for this section

### Student UTs

- Your Unit Tests account for 20% of the overall grade for this assignment.
- There must be at least 42 UTs for this assignment (every UT that does not pass is an automatic -1)
    - 14 UTs for Array
    - 14 UTs for Stack
    - 14 UTs for Queue
    - 42 UTs only for Array will only get you 14/42 of the total possible points for this section, 14 tests for all categories are needed
- All unit tests belong in the test folder and each file must begin with test i.e. (test_array.py)
- To check if your tests pass, run `make test`.

### Code Coverage

- Code Coverage (the percentage of code covered by your Unit Tests) accounts for 20% of the overall grade.
- After all of your UTs are run, we will be checking the code coverage.
- The percentage of code coverage is found by running `make coverage`.

### Solution Level UTs

- Our unit tests make up the remaining 50% of the overall grade.
- We will run our UTs against your program.
- The percentage of our tests that pass using your code will determine your score for this section.
- You need to ensure you adhere to the 'Interface' section in each README.md to ensure you get all points.
- If you fail to adhere to the interface that will be an automatic 0 for this section (you have been warned!)
