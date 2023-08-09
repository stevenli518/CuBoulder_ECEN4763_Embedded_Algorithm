# LZSS Compression

Lempel–Ziv–Storer–Szymanski is a dictionary based compression algorithm where previously seen sequences of data and their locations are saved, and when the same sequence is seen again it is replaced by a reference to the previous. 

Example:
'I am Sam\n\nSam I am\n\nThat Sam-I-am!\nThat Sam-I-am!\nI do not like\nthat Sam-I-am'
->
'I am Sam\n\nSam I am\n\nThat Sam-I-am!(19,16)I do not like\nt(21,12)'

Here, (19,16) represents positions 19-35, or the substring '\nThat Sam-I-am!\n'.

Notice that smaller phrases like 'Sam' are not referenced in this way. This is because the reference should only be included if it will reduce (or maintain) the overall length of the compression. If this was done at index 10, the reference (5,3) would have a length longer than just keeping the string the same at this section, i.e. length('(5,3)') > length('Sam'). In LZSS, the option with a shorter or equal length should always be chosen.

The encoding process is broken down into the following steps.
1. Loop over the data character by character. Let i be the index of the current character in the following steps.
2. Find the first occurrence of the character in the string. If there is none, after adding the character to the encoding, continue to the character at index i+1.
3. If there is an occurrence of the character, try including the next character to get a current substring of length 2. Find the first occurrence of this substring.
4. Repeat this process, including more characters in the substring, until there is a substring which isn't found. The longest substring that was found should be saved.
5. Check if the length of the position string '(pos,length)' for the longest substring found is shorter than or equal in length to the substring. If so, add this position string to the encoding and continue to the character after this longest substring, i.e. go back to the top with the character at index i+length.
6. If the position string is longer, then go back to the top at the character with index i+1. 

In all the steps shown above, the location of a substring or character should only be found up to (not including) the current position in the original data. This location will mark the beginning of a substring, so the occurrence of the substring found can overlap with the substring itself.

Consider the following example:

'cars' * 100
->
'cars(0,396)')

Since this data contains just a repitition of the same word over and over again, the steps above will continue adding letters to the substring until the end of the string is reached. The final substring has length 396, but 392 of those characters overlap with the substring itself.

LZSS decoding should do the reverse of encoding. It should copy the characters found to a decoding, until it reaches the '(' symbol, where it will read a position and a length followed by ')'. When this happens, it will copy the given length string starting at the position to the decoding, character by character to allow for the above overlap. 

## Getting Started Steps

- running "make setup" will install correct dependencies and check for correct python version (3.7+)
- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report

# Run-Length Encoding

## Requirements

- You must implement a class that handles the below interfaces for LZSS Compression.
- The class name must be called "LZSS".
- You must implement at least 14 unit tests.
- Must get a 10/10 when running "make style"
- Your unit tests must reach 100% code coverage

## Interface

- The function lzss_encode(self, data) should encode the given data with LZSS encoding. The encoding should be returned. The return type should be string. Data should be a string.
- The function lzss_decode(self, encoding) should decode the input encoding with LZSS decoding. The input encoding should be a string, and the output decoding should be a string. 

## Tests

- The encoding and decoding functions should be tested with defined arrays and random testing.
- Encoding and then decoding strings should be tested, i.e. test that the same string is returned after decoding.
- Cases including parenthesis do not need to be tested, as this will break decoding. Assume there are no parenthesis in the input.

## Corner Cases

- Strings containing many repitions of the same word or phrase, as in the cars example above
- Strings where the reprition of a phrase is at the end of the string

## Library

You can only use basic python libraries (no special imports).
