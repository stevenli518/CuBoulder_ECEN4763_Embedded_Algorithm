# Assignment 12 - Final Project

## Assignment Description

This assignment will serve as your final project for the course. It will be worth 10 percent of your grade overall, so make sure to spend plenty of time making your submission great!

In this assignment you will create an algorithm for specifying which radio signal a tower is allowed to use. The idea is that if you have a group of towers represented by a graph, how do you know the minimum number of signal lengths required based on the fact that no two connected Towers can share the same radio signal.

Given X towers and Y Radio Signals, how can you give each tower a different radio signal so they don't interfere with towers near them?

If you have 4 radio towers and you have 4 radio waves, each tower will get a different radio signal. However, if you have 5 towers and only 3 radio waves, how can you assign a radio signal to each tower to ensure that the towers that are connected do not share a common radio signal?

## Goal

The main goal for this assignment is to learn how to use graphs and create an algorithm based on everything you have learned this semester.

## Grading

- The grading is broken down into 4 sections. There is code format, your UTs, code coverage and Solution UTs.
- This assignment is worth 100pts.
- The code format is worth 10 points, your UTs are worth 20, coverage is worth 20, and my UTs are worth 50.

### Lint

- You will receive an all or nothing for lint for 10% of the overall grade.
- If you run `make style` and fix all errors you will get the 10%.
- If there are any style issues you automatically receive a 0 for this section

### Student UTs

- Your Unit Tests account for 20% of the overall grade for this assignment.
- There must be at least 28 UTs for this assignment (every UT missed is an automatic -1)
    - 28 UTs for Tower
- All unit tests belong in the test folder and each file must begin with test i.e. (test_array.py)

### Code Coverage

- Code Coverage (the percentage of code covered by your Unit Tests) accounts for 20% of the overall grade.
- After all of your UTs are run, we will be checking the code coverage.
- The percentage of code coverage is found by running `make coverage`.

### Solution Level UTs

- Our unit tests make up the remaining 50% of the overall grade.
- We will run our UTs against your program.
- The percentage of our tests that pass using your code will determine your score for this section.
- You need to ensure you adhere to the 'Interface' section in each README.md to ensure you get all points.
- If you fail to adhere to the interface that will be an automatic 0 for this section (you have been warned!)e that will be an automatic 0 for this section (you have been warned!)