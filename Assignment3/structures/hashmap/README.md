# Data Structures HashMap

Hashmap is a data structure that maps a key to a value. It implements an associative array. This data structure is faster than arrays and linked list. Most data types can be used for keys.

## Getting Started Steps

- running "make setup" will install correct dependencies and check for correct python version (3.7+)
- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report

# HashMap

## Requirements

- You must implement a class that handles the below interfaces for a hashmap.
- The class name must be called "Hashmap".
- You must implement at least 14 unit tests.
- Must get a 10/10 when running "make style"
- Your unit tests must reach 100% code coverage

## Interface

- The initiazation function will create the hashmap
    - Note: the hashmap must be an array of arrays. The number of arrays is the size of the hash, for example if my hashmap size was 4:
    [[], [], [], []]
- The function add_value(self, key, value) adds key and value (updates if key is identical)
    - If the key already exists then you need to append the (key, value) pair onto the list for that hash value
- The function get_value(self, key) return the value in the specified key
- The function delete_value(self, key) deletes a key and returns value if delete, None if key does not exist
- The function get_keys(self) returns all keys in the form ['A', 'B', etc]
- The function get_as_str(self) returns the hashmap in the form "[('A', 1)][('B', 2)][][][]" (for key 'A' = value 1 and key 'B' = value 2) note if 2 values share a hash than it would look like "[('A', 1), ('F', 6)][][][][]" (for key 'A' = value 1 and 'F' = value 6)
- The function get_as_dict(self) returns the hashmap in the form {0: {'Z': 36}, 3: {'X': 12}, 4: {'Y': 24}}
    - Note: 0 is the index into the array
- The function get_space_complexity() returns the space complexity of the data structure
- The function get_time_complexity() returns the time complexity of get_value in the data structure
- You must use the following hash function:
```python
    def _get_hash(self, key):
        """Get hash value of key."""
        user_hash = 0
        for char in str(key):
            user_hash += ord(char)
        return user_hash % self.size
```

## Tests

- Addition and deletion of keys and values
- Addition of existing keys with updated values
- Check for all the keys and values present in the hashmap
- Obtaining values from a specific key
- Display all the entries in the array
- Obtain space and time complexity

## Corner Cases

- Delete a nonexistent key and add a key that already exists in the hashmap

## Library

You can only use basic python libraries (no special imports).
