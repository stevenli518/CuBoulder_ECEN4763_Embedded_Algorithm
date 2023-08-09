# Assignment 6

## Assignment Description

In this assignment you will create a class for Bellman Ford based on your graph data structure. Note: you must support negative weights and be able to handle negatice cycles correctly. Please follow the guidelines located in the README.md.

## Goal

The main goal for this assignment is to learn how to write a Bellman Ford algorithm and use data structures you have created.

## Grading

- The grading is broken down into 4 sections. There is code format, your UTs, code coverage and Solution UTs.
- This assignment is worth 75pts.
- The code format is worth 7.5 points, your UTs are worth 15, coverage is worth 15, and my UTs are worth 37.5.

### Lint

- You will receive an all or nothing for lint for 10% of the overall grade.
- If you run `make style` and fix all errors you will get the 10%.
- If there are any style issues you automatically receive a 0 for this section

### Student UTs

- Your Unit Tests account for 20% of the overall grade for this assignment.
- There must be at least 28 UTs for this assignment (every UT missed is an automatic -1)
    - 14 UTs for Bellman Ford
    - 14 UTs for Graph (copied from assignment 3)
- All unit tests belong in the test folder and each file must begin with test i.e. (test_array.py)

### Code Coverage

- Code Coverage accounts for 10% of the overall grade.
- After all of your UTs are run, we will be checking the code coverage.
- We will take the amount and round it down to the nearest whole number. (i.e. 85% becomes an 80/100 or 8pts)

### Solution Level UTs

- We will run our UTs against your program.
- You need to ensure you adhere to the 'Interface' section in each README.md to ensure you get all points.
- There will be a -1 automatically deducted for every UT that does not pass. If you fail to adhere to the interface that will be an automatic 0 for this section (you have been warned!)