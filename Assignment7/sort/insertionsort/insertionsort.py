"""This module is for the insertion sort."""
# Citation: Adapted from GeeksforGeeks
# pylint: disable = R0903


class InsertionSort:
    """Class implementation for InsertionSort."""

    def __init__(self):
        """Construct the data structure."""
        self.array = []

    def sort(self, array):
        """Sort the array passed in the argument."""
        self.array = array
        for i in range(1, len(array)):
            val = array[i]
            data_type = type(array[i])
            k = i-1
            temp_type = type(array[k])
            if temp_type != data_type:
                return False
            while k >= 0 and array[k] > val:
                array[k+1] = array[k]
                k = k-1
            array[k+1] = val
        self.array = array
        return True


def get_time_complexity():
    """Get the time complexity of the data structure."""
    return 'O(N^2)'


def get_space_complexity():
    """Get the space complexity of the data structure."""
    return 'O(N)'
