# Assignment 10

## Assignment Description

In this assignment you will copy your Assignment 9 RLE class into this assignment. You will then implement the Burrows-Wheeler Transform. The BWT should then be combined with RLE to create a hybrid compression. Please follow the guidelines located in the README.md. 

## Extra Credit Opportunity

For 25 points of extra credit, implement a Huffman Coding class. You can find more information about Huffman Encoding here https://en.wikipedia.org/wiki/Huffman_coding. I will judge the qualtiy of your codes and accuracy of your tests to grade extra credit, so make sure to include plenty of tests and comments. I will not be running my own tests on the code, so the interface and data types can be done as you see fit.

## Goal

The main goal for this assignment is to learn how to implement RLE with Burrows-Wheeler Transform.

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
- There must be at least 14 UTs for this assignment (every UT missed is an automatic -1)
    - 14 UTs for the hybrid RLE and BWT
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
- If you fail to adhere to the interface that will be an automatic 0 for this section (you have been warned!)