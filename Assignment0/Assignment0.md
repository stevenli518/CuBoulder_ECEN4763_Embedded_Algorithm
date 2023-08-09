# Assignment 0

## Assignment Description

In this assignment you will practice your Unit Test skills.

## Goal

The main goal for this assignment is to learn how to generate Unit Tests.

## Grading

- The grading is broken down into 4 sections. There is joining slack, code format, your UTs, and code coverage.
- This assignment is worth 25pts.
- In future assignments, your code will be tested with our own Unit Tests, alongside the metrics listed below.

### Joining Slack

- Joining slack is worth 20% of the grade for this assignment.
- You will need to create a profile on the class Slack that has the same name as the name on this submission.
- This section is all or nothing.

### Lint

- You will receive an all or nothing for lint for 20% of the overall grade.
- If you run `make style` and fix all errors you will get the 20%.
- If there are any style issues you automatically receive a 0 for this section

### Student UTs

- Your Unit Tests account for 30% of the overall grade for this assignment.
- There must be at least 8 UTs for this assignment.
- Information on how to write Unit Tests can be found in the documentation here: https://docs.python.org/3/library/unittest.html
- The percentage of Unit Tests that are both present and passing will determine your grade for this section.
- To check if your tests pass, run `make test`.
- Every UT that does not pass is an automatic -1, so if you write 12 tests and 4 do not pass, it will count as 4/8 instead of 8/8 even though 8 tests pass.
- All unit tests belong in the test folder and each file must begin with test i.e. (test_fib.py)

### Code Coverage

- Code Coverage (the percentage of code covered by your Unit Tests) accounts for 30% of the overall grade.
- After all of your UTs are run, we will be checking the code coverage.
- The percentage of code coverage is found by running `make coverage`.
