"""This Array Module can be used to modularize the array class."""


class Array:
    """Class represents the array algorithm data structure."""

    def __init__(self):
        """Construct a new instance."""
        self.array = []

    def insert(self, value, index=-1):
        """When index >= 0 insert into that specific index otherwise append to the end."""
        if index >= 0:
            list2 = [value]
            self.array = self.array[:index] + list2 + self.array[index:]
        else:
            self.array.append(value)

    def print_array(self):
        """Print array."""
        print("\n")
        print(self.array)


def get_value(index):
    """Return the value at the specific index, return None if index does not exist."""
    if index >= len(Array.array) or index < 0:
        return None
    lst = Array.array
    return lst[index]


def get_index(value):
    """Return the index for the specific value, return None if value does not exist."""
    for i, num in enumerate(Array.array):
        if num == value:
            return i
    return None


def remove(value):
    """Remove value and return the value, return None if value does not exist."""
    if not get_index(value) or len(Array.array) == 0:
        return None
    idx = get_index(value)
    Array.array = Array.array[:idx] + Array.array[idx+1:]
    return value


def empty():
    """Remove all values from array."""
    Array.array = []


def is_empty():
    """Return true if the array is empty."""
    if len(Array.array) == 0:
        return True
    return False


def exists(value):
    """Return true if the array contains value."""
    if value not in Array.array:
        return False
    return True


def get_size():
    """Return the number of elements in the array."""
    return len(Array.array)


def get_space_complexity():
    """Return the space complexity of the data structure as a string."""
    return 'O(n)'
