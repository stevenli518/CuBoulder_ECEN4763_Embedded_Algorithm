# Run-Length Encoding Compression

RLE is a lossless algorithm that only offers decent compression ratios for specific types of data. It replaces sequences of the same data values within a file by a count and a single value. It is one of the simplest compression algorithms.

In Run-Length Encoding, the input data is traversed, character by character. The number of times the current character has been repeated is saved. The output encoding will then be the number of repititions followed by the character that has been repeated. For compression sake, 1s will be ommitted, so if there is no number before a character it can be assumed to have only been repeated once.

Example: 'bbbccdefgggggggg' -> '3b2cdef8g'

In decoding, the process is reversed. So, if data is encoded and then decoded, the same data should be returned.

## Getting Started Steps

- running "make setup" will install correct dependencies and check for correct python version (3.7+)
- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report

# Run-Length Encoding

## Requirements

- You must implement a class that handles the below interfaces for Run Length Encoding.
- The class name must be called "RLE".
- You must implement at least 14 unit tests.
- Must get a 10/10 when running "make style"
- Your unit tests must reach 100% code coverage

## Interface

- The function rle_encode(self, data) should encode the given data with RLE encoding. The encoding should be returned. The return type should be string. Data should be a string.
- The function rle_decode(self, encoding) should decode the input encoding with RLE decoding. The input encoding should be a string, and the output decoding should be a string. 

## Tests

- The encoding and decoding functions should be tested with defined arrays and random testing.
- Encoding and then decoding a string to check if the result is equal to the original.
- Cases including sequences of non-repeating characters should be tested.

## Library

You can only use basic python libraries (no special imports).
